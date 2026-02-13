# IoT Devices - Google Dork Queries

Dork queries designed to find internet-connected IoT devices including IP cameras, printers, NAS storage, routers, DVRs, and smart home controllers.

## Summary

| Risk Level | Count |
|------------|-------|
| Critical | 1 |
| High | 42 |
| Medium | 12 |

**Total: 778 dorks**

## Coverage

| Device Type | Description |
|------------|-------------|
| IP Cameras | Axis, Sony, Toshiba, Linksys, D-Link, Intellinet, IQeye, Mobotix, webcams |
| Printers | HP, Epson, Lexmark, Dell, Brother, Canon, Samsung, Ricoh, Tektronix |
| NAS Devices | Iomega NAS, Network Attached Storage utilities |
| Routers/Modems | SpeedStream, Actiontec, ADSL configuration, Linksys |
| DVR/NVR | DVR clients, EDR remote viewers, NETSurveillance, Divar |
| Smart Home | HomeSeer controllers, PacketShaper, Flash Operator Panel |
| Access Points | 3Com OfficeConnect wireless access points |

## Example Usage

```
# Find Axis camera live views with tilt control
tilt intitle:"Live View / - AXIS" | inurl:view/view.shtml

# Find HP printer web interfaces
inurl:hp/device/this.LCDispatcher

# Find NAS management interfaces
intitle:"Iomega NAS Manager"

# Find DVR web clients
intitle:"DVR Client" -the -free -pdf
```

## Why IoT Devices Matter

Exposed IoT devices represent significant security risks:

- **IP cameras** can be used for surveillance or as pivot points
- **Printers** may store cached documents and provide network access
- **NAS devices** often contain sensitive business data
- **Routers** with default credentials enable network infiltration

## Data Source

CSV file: [`GoogleDork-IoTDevices.csv`](GoogleDork-IoTDevices.csv)
