# LoRa / UWB / RFID Passive Tagging – Deployment Notes
© LORI Framework | offgrid-tracking/LoRa_UWB_RFID_Tags.md

---

## Purpose:
Enable ultra-low-power geolocation, boundary-breach alerts, and temporary identification using passive or energy-scavenging tags.

---

## Supported Tag Types:

| Tag Type | Range | Power | Use Case |
|----------|------------|-------------|-----------------------------|
| RFID | <10m | Passive | Checkpoint item scan |
| LoRa | up to 10km | Solar+coin | Field-deployed zone tracking|
| UWB | 100m-200m | Rechargeable| Gait motion profile logging |

---

## Design Features:
- No embedded microphones or cameras
- Biometric-free signaling (only location & timestamp)
- Auto-expiry (3–14 days default lifespan)
- Tamper-resistant but **user-removable**

---

## Ethical Compliance:
- Tags do **not contain identity or personal info**
- No backdoor activation
- Only track movement across predefined humanitarian corridors, fire zones, or border entry gaps

