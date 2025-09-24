# SmartBorder Edge Node Specification
© LORI Framework | starlink-grid/Node_Spec.md

---

## Physical:
- Dimensions: 38cm × 38cm × 55cm
- Weight: 7.2 kg
- Weatherproof: IP67 rated

---

## Core Components:
| Component | Spec |
|------------------|--------------------------------------------|
| Edge CPU | Jetson Orin Nano / Rockchip RK3588 |
| Sensor Bus | UWB, IR, Thermal, LoRa, Microphone (passive) |
| Connectivity | Starlink + LoRa fallback |
| Storage | 512GB eMMC + 1TB encrypted NVMe |
| Power System | 60W solar + 90Wh lithium backup |

---

## Safety:
- EMI-shielded
- No local facial database stored
- LED indicator: red (offline), green (secure), blue (human override)

