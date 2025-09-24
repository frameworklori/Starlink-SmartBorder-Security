# Data Flow Diagram – Starlink-SmartBorder-Security

This document maps the end-to-end data journey from edge collection to cloud escalation.

---

## Flow Path:
1. Sensor Trigger → Thermal/Gait/Device anomaly
2. Local AI scoring → Alert flag
3. Starlink uplink → Cloud Command Center
4. DHS review → FBI/CBP escalation (if needed)

## Diagram Notes:
- Data-at-rest encryption (AES-256)
- Data-in-motion secured by TLS 1.3
- Time-to-live for transient packets: 6 minutes

