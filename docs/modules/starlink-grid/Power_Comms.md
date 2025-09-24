# Power and Communication Protocols
© LORI Framework | starlink-grid/Power_Comms.md

---

## Power Architecture:
- Primary: 60W photovoltaic panel
- Backup: Li-Ion 90Wh + 12V regulator
- MTBF: 1100+ hrs under desert sun conditions
- Auto-shutdown at 7.5V threshold

---

## Communication Protocols:
- Uplink:
- Starlink Gen2 → Public cloud relay (AWS GovCloud / Azure Gov)
- VPN encrypted tunnel w/ rotating keys

- Downlink:
- OTA config from Command Center
- Alert triggers to DHS / CBP dashboard

- Failover:
- Mesh LoRa-to-LoRa alert fallback (≤ 5 hops)

---

## Latency Goals:
- Alert to cloud: ≤ 2.4 sec
- Heartbeat check: every 15 min

