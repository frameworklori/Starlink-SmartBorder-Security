 Oncall Playbook

This document outlines protocols for SRE (Site Reliability Engineering) oncall responders for Starlink-SmartBorder-Security deployments.

## 📅 Oncall Rotations

| Role | Duration | Notes |
|--------------------|----------|--------------------------------|
| Primary Responder | 1 week | 24/7 pager duty |
| Secondary Backup | 1 week | Escalated only if Primary fails|

Oncall is coordinated via PagerDuty. Slack alerts routed to `#sre-oncall` with `@here` mentions for Priority-1 issues.

---

## 🚨 Alert Classification

| Severity | Description | Response SLA |
|----------|-------------------------------------|--------------|
| P1 | Border sensor outage, data leak | 15 mins |
| P2 | Latency > 5s, degraded Starlink link| 1 hour |
| P3 | Non-blocking alerts (e.g., disk) | 4 hours |

---

## 🧰 Oncall Tools

- `Starlink Telemetry Dashboard`
- `LORI-Ledger Audit Console`
- `AI Anomaly Validator`
- `Edge Node Pinger` (`/scripts/tools/ping_node.sh`)

---

## 🧭 Standard Response Flows

### P1: Sensor Offline

1. Run `diag --zone=X`
2. Trigger failover node with `edge_promote.sh`
3. Notify Incident Commander via `/ic alert`

---

### P2: Uplink Jitter

1. Validate link speed (`./check_satlink.sh`)
2. Attempt remote Starlink terminal reboot
3. Alert SRE Secondary if >2 retries fail

---

## 🧾 Shift Handoff Template

Zone Coverage: SE/NE border zones

Open Incidents: 2 (sensor drift, LTE fallback active)

Pending Fixes: awaiting config push to node-49

Notes: Firmware patch v2.4 beta tested successfully

---

## ☎️ Emergency Contact Tree

- Lead SRE: +1-XXX-XXX-XXXX
- Platform Engineer: +1-XXX-XXX-XXXX
- NGO Liaison (for HAP): +1-XXX-XXX-XXXX

