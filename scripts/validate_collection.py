"""Validate the collection's CSV schema, uniqueness, descriptions, and counts.

Run from the repository root: python3 scripts/validate_collection.py
"""

import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HEADERS = ["Query", "Description", "RiskLevel"]
RISKS = {"Critical", "High", "Medium", "Low", "Informational"}
GENERIC = re.compile(r"^Google dork query for .* reconnaissance$", re.IGNORECASE)
QUOTES = str.maketrans({"“": '"', "”": '"', "„": '"', "‘": "'", "’": "'", "″": '"', "\u00a0": " "})


def normalize(query):
    """Treat quote typography, case, and spacing as equivalent for deduplication."""
    return " ".join(unicodedata.normalize("NFC", query).translate(QUOTES).split()).casefold()


def validate(root):
    root = Path(root)
    errors = []
    seen = {}
    category_counts = {}
    for path in sorted(root.glob("*/GoogleDork-*.csv")):
        category = path.parent.name
        risks = Counter()
        count = 0
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != HEADERS:
                errors.append(f"{path}: expected CSV header {HEADERS}, got {reader.fieldnames}")
                continue
            for line, row in enumerate(reader, 2):
                count += 1
                where = f"{path}:{line}"
                if None in row or row.get(None):
                    errors.append(f"{where}: unexpected extra CSV field")
                for column in HEADERS:
                    if not (row.get(column) or "").strip():
                        errors.append(f"{where}: missing {column}")
                query = (row.get("Query") or "").strip()
                description = (row.get("Description") or "").strip()
                risk = (row.get("RiskLevel") or "").strip()
                if query:
                    key = normalize(query)
                    if key in seen:
                        errors.append(f"{where}: duplicate query (first at {seen[key]})")
                    else:
                        seen[key] = where
                if description and (GENERIC.fullmatch(description) or len(description) < 30):
                    errors.append(f"{where}: generic or too-short description")
                if risk not in RISKS:
                    errors.append(f"{where}: invalid RiskLevel {risk!r}")
                else:
                    risks[risk] += 1
        category_counts[category] = count
        readme = path.parent / "README.md"
        if not readme.is_file():
            errors.append(f"{readme}: missing category README")
            continue
        text = readme.read_text(encoding="utf-8")
        total = re.search(r"\*\*Total:\s*([\d,]+)\s+dorks\*\*|\|\s*\*\*Total\*\*\s*\|\s*\*\*([\d,]+)\*\*", text, re.I)
        if not total or int(next(value for value in total.groups() if value).replace(",", "")) != count:
            errors.append(f"{readme}: README total does not match {count} CSV rows")
        for heading in ("## Summary", "## Risk Level Distribution"):
            if heading not in text:
                continue
            section = text.split(heading, 1)[1].split("## ", 1)[0]
            stated_risks = {
                level: int(stated.replace(",", ""))
                for level, stated in re.findall(
                    r"^\|\s*(Critical|High|Medium|Low|Informational)\s*\|\s*([\d,]+)\s*\|",
                    section, re.M,
                )
            }
            for level, actual in risks.items():
                if level not in stated_risks:
                    errors.append(f"{readme}: {level} missing from risk distribution")
                elif stated_risks[level] != actual:
                    errors.append(f"{readme}: {level} summary says {stated_risks[level]}, CSV has {actual}")
            for level, stated in stated_risks.items():
                if level not in risks and stated != 0:
                    errors.append(f"{readme}: {level} summary says {stated}, CSV has 0")
    readme = root / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        stated_categories = {
            name: int(stated.replace(",", ""))
            for name, stated in re.findall(r"\]\(([^/)]+)/\)\s*\|[^\n]*?\|\s*([\d,]+)\s*\|", text)
        }
        for name, actual in category_counts.items():
            if name not in stated_categories:
                errors.append(f"{readme}: {name} missing from category table")
            elif stated_categories[name] != actual:
                errors.append(f"{readme}: {name} table count does not match {actual}")
        for name in stated_categories.keys() - category_counts.keys():
            errors.append(f"{readme}: {name} table category has no CSV")
        total = re.search(r"\*\*Total:\s*([\d,]+)\s+unique dorks\*\*\s+across\s+(\d+)\s+categories", text)
        if not total or (int(total[1].replace(",", "")) != len(seen) or int(total[2]) != len(category_counts)):
            errors.append(f"{readme}: overall total/category count does not match {len(seen)}/{len(category_counts)}")
    return errors


if __name__ == "__main__":
    problems = validate(Path(__file__).resolve().parents[1])
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("Collection valid: unique queries, non-empty descriptions, risk levels, and README counts match.")
