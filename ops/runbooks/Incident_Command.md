---

### 📘 `Incident_Command.md`

```markdown
# Incident Command Protocol

Defines the command structure and roles for responding to border-related alerts triggered by the system.

## Command Roles

- **Incident Commander (IC)** – primary decision-maker.
- **Comms Lead (CL)** – handles NGO/government liaisons.
- **Technical Lead (TL)** – manages sensor diagnostics + AI review.
- **Humanitarian Liaison (HL)** – ensures HAP signals are addressed.

## Activation Triggers

- `Level 3+` alerts (e.g., border crossing anomaly, hypothermia cluster)
- Manual override via `/admin/escalate`

## Response Phases

1. **Assess**
- Confirm alert authenticity.
- Pull context (e.g., location, risk score, weather).

2. **Coordinate**
- Notify stakeholders (CBP, UNHCR, etc.).
- Deploy drones or ground response teams.

3. **Contain**
- Enforce soft geo-fence if applicable.
- Record all events on the LORI-Ledger.

4. **Report**
- Generate blockchain-auditable incident report.
- Archive snapshot for audit & review.

