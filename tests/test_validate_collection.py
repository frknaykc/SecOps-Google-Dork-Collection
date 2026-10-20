import csv
import tempfile
import unittest
from pathlib import Path

from scripts.validate_collection import validate


class CollectionValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def category(self, name, rows, *, stated_total=None):
        folder = self.root / name
        folder.mkdir()
        with (folder / f"GoogleDork-{name}.csv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(("Query", "Description", "RiskLevel"))
            writer.writerows(rows)
        total = len(rows) if stated_total is None else stated_total
        (folder / "README.md").write_text(
            f"# {name}\n\n| Risk Level | Count |\n|---|---|\n| Low | {total} |\n"
            f"\n**Total: {total} dorks**\n", encoding="utf-8"
        )

    def test_valid_collection(self):
        self.category("First", [("intitle:Portal", "Find indexed portal pages for asset inventory.", "Low")])
        self.assertEqual(validate(self.root), [])

    def test_normalized_duplicate_across_categories(self):
        self.category("First", [('intitle:"Portal"', "Identify indexed portals on authorized sites.", "Low")])
        self.category("Second", [('intitle:“portal”', "Locate indexed portals for authorized review.", "Low")])
        self.assertTrue(any("duplicate" in error for error in validate(self.root)))

    def test_generic_description_and_invalid_risk(self):
        self.category("First", [("inurl:/admin", "Google dork query for recon reconnaissance", "Severe")])
        errors = validate(self.root)
        self.assertTrue(any("description" in error for error in errors))
        self.assertTrue(any("RiskLevel" in error for error in errors))

    def test_readme_counts_and_missing_fields(self):
        self.category("First", [("inurl:/admin", "", "Low")], stated_total=2)
        errors = validate(self.root)
        self.assertTrue(any("missing Description" in error for error in errors))
        self.assertTrue(any("README" in error for error in errors))

    def test_root_readme_requires_every_category_and_total(self):
        self.category("First", [("intitle:Portal", "Find indexed portals for asset inventory.", "Low")])
        (self.root / "README.md").write_text(
            "| Category | Folder | Description | Dork Count |\n"
            "|---|---|---|---:|\n", encoding="utf-8"
        )
        errors = validate(self.root)
        self.assertTrue(any("First" in error and "table" in error for error in errors))
        self.assertTrue(any("overall total" in error for error in errors))

    def test_readme_risk_distribution_requires_all_levels(self):
        self.category("First", [("intitle:Portal", "Find indexed portals for asset inventory.", "Low")])
        readme = self.root / "First" / "README.md"
        readme.write_text("## Summary\n\n| Risk Level | Count |\n|---|---:|\n\n**Total: 1 dorks**\n", encoding="utf-8")
        self.assertTrue(any("risk distribution" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
