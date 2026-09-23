# Threat Hunting - Google Dork Collection

Google Dork queries specifically designed for **proactive threat hunting** -- identifying active compromises, C2 infrastructure, malware panels, phishing kits, and threat intelligence resources.

## Overview

| Metric | Value |
|--------|-------|
| **Total Dorks** | 272 |
| **Risk Levels** | Critical, High, Medium, Informational |
| **CSV File** | [GoogleDork-ThreatHunting.csv](GoogleDork-ThreatHunting.csv) |

## Categories

### C2 Framework Detection

Dorks for identifying exposed Command & Control infrastructure from frameworks commonly used in red team operations and by threat actors.

| Target | Description |
|--------|-------------|
| Cobalt Strike | Team server listeners, Beacon configs, Malleable C2 profiles, jQuery CDN impersonation |
| Metasploit | MSFRPC web consoles, Metasploit Pro login pages, self-signed CA detection |
| PowerShell Empire | C2 web interfaces, Starkiller GUI with Listeners/Agents panels |
| Havoc | Team server interfaces, X_Havoc header detection, Demon agent references |
| Sliver | C2 implant binaries in open directories, sliver-client payloads |
| Mythic | React-based web UI, Laravel/Inertia panels, c2backend_session cookies |
| Covenant | Blazor-based UI, covenant.css fingerprinting |
| Brute Ratel C4 | Adversary simulation panels, badger implant references |
| PoshC2 | Default SSL certificate organization strings (P18055077, Pajfds, Jethpro) |
| SILENTTRINITY / Villain | Python-based C2 framework login pages |
| DeimosC2 / Merlin | Golang-based C2 framework interfaces |
| Nighthawk | MDSec commercial C2 tool infrastructure |
| SuperShell | SuperShell C2 reverse shell functionality |
| Pyramid C2 | Python-based C2 framework with listener/agent panels |
| Viper | Chinese-origin C2 framework with msfvenom integration |
| Hak5 Cloud C2 | Red team device fleet management panels |

```
intitle:"Cobalt Strike" "Listener"
intitle:"Mythic" "Active Callbacks" "Active Payloads"
intitle:"Havoc" "Teamserver" "Listeners"
intitle:"C2 Panel" intext:"c2backend_session"
intitle:"65 Cloud C" | intitle:"125 Cloud"
intitle:"Viper" intext:"C2" intext:"Session" intext:"Payload"
```

### Remote Access Trojans (RATs)

Dorks for finding exposed RAT control panels, builder interfaces, and C2 server certificates.

| Target | Description |
|--------|-------------|
| njRAT / DarkComet | Classic RAT builder and connection panels |
| Quasar RAT / AsyncRAT | Open-source .NET RAT control interfaces, server CA detection |
| Remcos RAT | Commercial RAT dashboard and connection panels |
| Orcus RAT | Server certificate (OrcusServerCertificate) and panel detection |
| DcRAT (Dark Crystal) | DcRat Server panel interfaces |
| VenomRAT | Panel and builder interfaces with payload generation |
| BitRAT | C2 panels and infrastructure detection |
| XtremeRAT | Legacy RAT trojan panel detection |
| Gh0st RAT | Chinese-origin APT remote administration tool |
| NanoCore | .NET RAT control panels and server detection |
| Pupy RAT | Cross-platform (Python) RAT framework |
| CHAOS RAT | Go-based RAT with reverse shell capability |
| XWorm | RAT control panels and builder/binder interfaces |
| NetSupport RAT | Legitimate tool abused by threat actors for remote access |

```
intitle:"njRAT" "Connection" "Builder"
intitle:"AsyncRAT" | intext:"AsyncRAT Server"
intitle:"DcRat" | intext:"DcRat Server"
intitle:"VenomRAT" | intext:"VenomRAT"
intitle:"XWorm" | intext:"XWorm" intext:"RAT"
intitle:"Gh0st RAT" | intext:"Gh0st RAT"
```

### Stealer & Botnet Panels

Dorks for detecting exposed information stealer and botnet Command & Control panels.

| Target | Description |
|--------|-------------|
| Agent Tesla / RedLine | Stealer panel dashboards with stolen credentials |
| Raccoon / Vidar / AZORult | Info stealer C2 panels and log viewers |
| FormBook / LokiBot | Malware C2 panels with bot tracking |
| Titan Stealer | C2 panel with known branding typo variant |
| Meduza Stealer | C2 panel with stolen credential log viewers |
| StealC v2 | Information stealer panels with active log interfaces |
| Panda Stealer | Collector Stealer variant, Dream Commerce decoy pages |
| Shadow C2 | Info stealer with password/wallet/Telegram collection |
| Stealth C2 | Banking trojan panels with cookie theft functionality |
| HookBot | Android banking trojan C2 panels |
| Emotet / TrickBot | Banking trojan and loader botnet panels |
| IcedID / Gozi / BokBot | Banking trojan C2 with LlamaHQ-Swoole infrastructure |
| Mirai / Mozi | IoT botnet scanner and bruter panels |
| Andromeda / ZeroAccess | Legacy botnet C&C infrastructure |

```
intitle:"Titan Stealer" | intext:"Titan Stealer"
intitle:"Meduza Stealer" | intext:"Meduza Stealer"
intitle:"StealC" | intext:"StealC" intext:"Panel"
intitle:"Shadow C2 Panel" | intext:"Shadow C2 Command Center"
intitle:"Stealth C2 Panel" | intext:"Stealth Command & Control Panel"
intitle:"HOOKBOT PANEL" | intext:"HOOKBOT"
```

### Ransomware Infrastructure

Dorks for finding ransomware payment portals, leak sites, and related infrastructure.

| Target | Description |
|--------|-------------|
| Generic Ransomware | Payment/decryption pages with Bitcoin addresses |
| LockBit / BlackCat (ALPHV) | Leak site mirrors and blog posts |
| Conti / REvil | Ransomware group leak site content |
| RansomHub | Leak site mirrors and decryption portals |
| BianLian | Go-based ransomware leak site infrastructure |

```
intitle:"Ransomware" "decrypt" "bitcoin" | "BTC"
intitle:"LockBit" "Leaked Data" | "Blog"
intitle:"RansomHub" | intext:"RansomHub"
intitle:"BianLian" intext:"leak" | intext:"ransomware"
```

### Phishing Infrastructure

Dorks for detecting phishing kits, credential harvesting pages, and social engineering campaigns.

| Target | Description |
|--------|-------------|
| GoPhish | Open-source phishing framework admin panels and campaign dashboards |
| Evilginx2 | Adversary-in-the-middle phishing proxy with phishlet configs |
| EvilGoPhish | Combined Evilginx + GoPhish framework |
| ClickFix Campaign | Fake CAPTCHA pages tricking users into running clipboard commands |
| WordPress-hosted Phish | Phishing pages in wp-content/wp-includes directories |
| Brand Impersonation | Fake Google, PayPal, Apple, Microsoft, Netflix, O365 login pages |
| Phishing Kit Archives | Uploaded ZIP kits on compromised servers |

```
intitle:"Gophish - Login"
intitle:"evilginx" intext:"phishlet"
intitle:"Checking if you are human" intext:"Ctrl" intext:"clipboard"
inurl:"/wp-content/uploads/" intitle:"Sign in" "Google"
inurl:"/scam/" | inurl:"/phish/" | inurl:"/kit/" ext:zip
```

### Web Shells & Backdoors

Dorks for hunting deployed web shells and backdoor scripts on compromised servers.

| Target | Description |
|--------|-------------|
| PHP Shells | c99, r57, b374k, WSO, FilesMan, p0wny-shell |
| ASP.NET Shells | ASPXSpy, SharPyShell |
| Java Shells | JspSpy web shell |
| Encrypted Shells | China Chopper, Behinder (IceScorpion), Godzilla |
| Shell Managers | AntSword, Weevely |
| Obfuscated Backdoors | GIF header tricks, base64+eval patterns |

```
inurl:"/shell.php" | inurl:"/cmd.php" | inurl:"/exec.php"
intext:"GIF89a" intext:"<?php" intext:"eval" ext:php
intitle:"ASPXSpy"
intitle:"Behinder" | intext:"behinder" "shell"
```

### DDoS & Cryptominer Panels

Dorks for finding exposed DDoS tools and cryptominer C2 infrastructure.

| Target | Description |
|--------|-------------|
| Locust DDoS | HTTP flood tool panels with attack/RPS monitoring |
| IMMORTAL DROPPER | XMRig cryptominer C2 panel with SupportXMR pool connections |
| Coinhive / CoinImp / Crypto-Loot | Web-based cryptominer script injections |
| XMRig Web Miners | Browser-based Monero mining injections |

```
intitle:"Locust" intext:"HTTPFloodUser"
intitle:"IMMORTAL DROPPER C2 Panel"
intext:"pool.supportxmr.com" intext:"DeployMiner"
intext:"CoinHive.Anonymous"
```

### Compromised Server Indicators

Dorks for identifying servers showing signs of active compromise.

| Target | Description |
|--------|-------------|
| Website Defacement | "Hacked by" pages, leet-speak defacement titles |
| Web Skimmers (Magecart) | Payment card skimmer scripts on checkout pages |
| SEO Spam/Pharma Hack | Japanese keyword hack, pharma injection campaigns |
| Post-Exploitation Tools | Exposed Mimikatz, BloodHound, Rubeus, tunneling tools |
| Credential Dumps | NTDS, SAM, LSASS dumps in open directories |
| Open Dir Payload Hosting | Directories with XWorm, Cobalt Strike, AnyDesk, Rclone payloads |

```
intitle:"Hacked by" "Greetz"
intitle:"Magecart" | intext:"skimmer" intext:"checkout" ext:js
intitle:"Index of" intext:"xworm" | intext:"XWorm"
intitle:"Index of" intext:"cobaltstrike" | intext:"beacon"
```

### Threat Intelligence Resources

Dorks for finding published threat reports, IOC feeds, detection rules, and sandbox analysis.

| Target | Description |
|--------|-------------|
| Malware Analysis | Reports from ANY.RUN, Triage, Hybrid Analysis |
| IOC Feeds | AlienVault OTX, ThreatFox, URLhaus, MalwareBazaar |
| Detection Rules | YARA rules, Sigma rules, STIX indicators |
| Threat Reports | APT campaign reports, IOC lists (PDF/CSV) |
| APT Groups | APT41/Winnti, Geacon Pro tracking and IOC references |

```
filetype:yar "rule" "meta" "strings" "condition"
filetype:yml "sigma" "detection" "condition" "logsource"
site:urlhaus.abuse.ch "online" "malware_download"
intitle:"APT" "Campaign" "IOC" filetype:pdf
```

### Security Tool Exposure

Dorks for finding exposed security monitoring, IR, and threat intel platforms.

| Target | Description |
|--------|-------------|
| IDS/IPS | Suricata alerts, Snort dashboards, ModSecurity logs |
| HIDS/SIEM | OSSEC alerts, Wazuh dashboards, WAF logs |
| Incident Response | TheHive cases, GRR hunts, Velociraptor clients |
| Threat Intel Platforms | MISP events, OpenCTI dashboards, Cortex analyzers |
| Honeypots | Cowrie, Dionaea, T-Pot, Kippo, HoneyDB dashboards |
| KVM Tools | PiKVM, TinyPilot, NanoKVM, GLKVM remote access interfaces |
| Keycloak | Admin consoles potentially used for C2 auth infrastructure |

```
intitle:"Wazuh" "Security Events" "Agents"
intitle:"TheHive" "Cases" "Observables"
intitle:"MISP" "Events" "Attributes" "Galaxy"
intitle:"PiKVM" intext:"KVM" | intext:"Virtual Keyboard"
```

### C2 Tunneling & Infrastructure

Dorks for detecting tunneling services, tools, and bulletproof hosting used for C2 communication.

| Target | Description |
|--------|-------------|
| DNS Tunneling | dnscat2, iodine DNS tunnel tools |
| Reverse Proxies | FRP (Fast Reverse Proxy) exposed configs |
| Tunnel Services | ngrok, Serveo SSH tunnel endpoints |
| Chisel / Ligolo-ng | SOCKS proxy and tunneling tools in open directories |
| wstunnel | WebSocket tunneling for C2 evasion |
| Reverse SSH | Reverse SSH tunnel tools and configurations |
| Flask/Werkzeug C2 | Generic Python-based C2 panels with bot/target APIs |
| Bulletproof Hosting | SERV.HOST and offshore VPS providers for malicious infrastructure |
| Interactsh | OOB interaction servers for vulnerability testing |

```
intext:"DNS Tunnel" | intext:"iodine" | intext:"dnscat2"
inurl:".ngrok.io" | inurl:".ngrok-free.app"
intitle:"Index of /" intext:"chisel" | intext:"ligolo" | intext:"frp"
intext:"wstunnel" intext:"websocket tunnel"
intitle:"Interactsh" | intext:"interactsh-server"
intext:"Werkzeug" intext:"/api/bots" | intext:"/api/targets"
```

### Generic C2 Indicators

Dorks for detecting generic C2 panel patterns and botnet infrastructure.

| Target | Description |
|--------|-------------|
| C2 Panel Login | Generic C2/Bot panel login pages |
| Bot Statistics | Panels exposing active bot counts |
| Default Auth | Panels with default Basic Auth realm configs |
| SectopRAT | ArechClient2 C2 infrastructure |
| Oyster C2 | Oyster backdoor panel interfaces |
| QakBot / PikaBot | Banking trojan and loader C2 references |

```
intitle:"C2 Panel" | intitle:"C2 Dashboard" inurl:"/login"
intitle:"Bot Panel" intext:"Online" intext:"Commands" ext:php
intitle:"SectopRAT" | intext:"SectopRAT"
intext:"QakBot" | intext:"Qbot" intext:"C2" intext:"panel"
```

## Risk Level Distribution

| Risk Level | Count | Description |
|------------|-------|-------------|
| **Critical** | 194 | Active C2 panels, malware infrastructure, web shells, ransomware, credential dumps, stealer panels |
| **High** | 47 | Phishing pages, defacements, cryptominers, compromised indicators, exposed IR tools, tunneling |
| **Medium** | 18 | Honeypots, detection rules, DNS tunneling, IDS/IPS logs, STIX/IOC feeds |
| **Informational** | 13 | Threat intelligence reports, sandbox analysis, malware repositories, APT tracking |
| **Total** | **272** | |

## Usage Tips

### Threat Hunting Workflow

1. **Infrastructure Discovery**: Start with C2 framework dorks to find exposed attacker infrastructure
2. **Compromise Detection**: Use web shell and defacement dorks to identify compromised assets
3. **Phishing Campaigns**: Track active phishing infrastructure (GoPhish, Evilginx, ClickFix)
4. **Stealer Tracking**: Monitor for exposed stealer panels leaking stolen credentials
5. **IOC Enrichment**: Cross-reference findings with threat intel platform dorks
6. **Detection Engineering**: Find YARA/Sigma rules to improve your detection coverage

### Combining with Target Scope

Many of these dorks can be combined with `site:` to scope to your organization:

```
site:example.com intext:"eval(Request" ext:php
site:example.com inurl:"/shell.php" | inurl:"/cmd.php"
site:example.com intext:"CoinHive.Anonymous"
```

## Disclaimer

These dorks are intended for **authorized threat hunting and security research only**. Always ensure you have proper authorization before investigating any infrastructure. Report findings through responsible disclosure channels.
