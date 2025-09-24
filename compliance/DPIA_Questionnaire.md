# DPIA Questionnaire – Starlink-SmartBorder-Security
© LORI Framework | compliance/DPIA_Questionnaire.md

This DPIA questionnaire is designed to assess the privacy risks associated with the implementation of the Starlink-SmartBorder system.

---

## Section A: Data Types Collected
- [x] Thermal signatures
- [x] Device MAC addresses
- [x] Voiceprint / gait patterns
- [ ] Facial imagery (if available)
- [ ] Biometric correlation to databases

---

## Section B: Data Purpose
- Intrusion detection (border entries)
- IP exfiltration alert
- Cross-border device audit
- Aggregated analytics only

---

## Section C: Access Controls
- Role-based data access (CBP/FBI only)
- Time-expiry on logs (≤ 30 days unless escalated)
- Full chain-of-custody audit trail stored on secure server

---

## Section D: User Rights
- Not applicable (non-citizen intercept zones)
- Human-in-the-loop escalation for all AI alerts

