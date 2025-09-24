
# Deployment Playbook
© LORI Framework | starlink-grid/Deployment_Playbook.md

---

## Objective:
Guide field teams in deploying SmartBorder Starlink nodes across rural or high-traffic zones.

---

## Pre-Deployment Checklist:
- 📦 Node inventory (thermal cam, UWB, edge GPU, solar)
- 🛰 Starlink dish (Gen2 or later)
- 🔋 Power buffer units
- 📍 GPS triangulation tablet
- 📑 Local legal compliance form

---

## Setup Steps:
1. Position node on 2.5m pole
2. Align Starlink to clear sky azimuth 15°–75°
3. Power on sequence (solar + battery failover test)
4. Establish ping with cloud controller
5. Run diagnostic mode: `diag_start --geo-hash`

---

## Notes:
- All nodes must be **decommissionable** in < 5 mins
- Default Starlink latency target: ≤ 45ms
