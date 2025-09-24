# Red Flag Rule Set
© LORI Framework | ai-analytics/Red_Flag_Rules.md

---

## Purpose:
Define hard-coded rules that trigger mandatory human review or automatic escalation to DHS/FBI.

## Rule Categories:

### Category A: Immediate Escalation
- High heat + gait match + device anomaly
- Border crosser exiting with flagged device

### Category B: Review Required
- Night crossing + no thermal signature
- Repeated detection in same zone within 24h

### Category C: Optional (Logged)
- Crossing near known wildlife corridor (low score)
- Audible disruption without movement

## Notes:
Rules are transparent and version-controlled via audit log.

