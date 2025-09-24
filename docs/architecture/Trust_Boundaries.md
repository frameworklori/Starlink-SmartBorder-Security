# Trust Boundaries – Network & Data Segmentation

Describes zones of control and containment to prevent lateral movement in compromise events.

---

## Zones:
- Edge Zone: Sensor & local AI
- Relay Zone: Starlink uplink only
- Cloud Zone: Risk modeling & scoring
- Command Zone: Human decision only

## Boundaries:
- Encrypted packet jump only (no raw flow)
- Each layer blind to full system map
- Kill-switch segmentation at each node

## Diagram Option:
🛑 ← Edge Node → 🔒 → Cloud → 🧠 → Human Operator
