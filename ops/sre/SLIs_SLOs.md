# SLIs & SLOs for Starlink-SmartBorder-Security

Defines the key service level indicators (SLIs) and corresponding service level objectives (SLOs) for system reliability monitoring.

---

## 🌐 Connectivity SLIs

| Indicator | Definition | Target SLO |
|---------------------|------------------------------------------|-------------------|
| Uplink Availability | % of time edge node can reach Starlink | ≥ 99.8%/month |
| Packet Loss Rate | % packet loss to backend relay | ≤ 0.5% per hour |
| Latency | Round-trip time from node to HQ (ms) | ≤ 200ms 95%tile |

---

## 🧠 AI Subsystem SLIs

| Indicator | Definition | Target SLO |
|---------------------|------------------------------------------|-------------------|
| Model Latency | Inference time per anomaly event | ≤ 6s per event |
| Accuracy (R1-R5) | Correct threat classification rate | ≥ 92% |
| Drift Detection | % anomaly from training norm | ≤ 3% per week |

---

## 📊 HAP (Humanitarian Alert Protocol)

| Indicator | Definition | Target SLO |
|---------------------|------------------------------------------|-------------------|
| False Positive Rate | % HAP alerts not correlated with harm | ≤ 1.5% |
| NGO Ping Latency | Time from event to NGO notification | ≤ 10s |
| Successful Aid Path | HAP alert leads to successful rescue | ≥ 90% (simulated) |

---

## 🔐 Blockchain & Ledger

| Indicator | Definition | Target SLO |
|---------------------|------------------------------------------|-------------------|
| Ledger Write Latency| Time to write hash to LORI-Ledger | ≤ 2s |
| Event Integrity | SHA256 match with node log | 100% |

---

## 🎯 SLO Breach Handling

When any SLO breaches:
- Trigger `SLO_Breach_Report.sh`
- Notify `#sre-postmortems`
- Create issue in `Reliability Tracker`
- Include RCA within 48h

