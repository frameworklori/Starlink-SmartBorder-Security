# Sensor Calibration Guide

This guide ensures all onboard sensors are accurately calibrated for cross-environment operations (desert, forest, urban).

## Calibration Types

| Sensor Type | Calibration Method |
|----------------|---------------------------|
| Thermal IR | Black-body reference @ 37°C |
| Acoustic | White noise baseline tests |
| Motion/LiDAR | Grid-walk auto alignment |
| Radar/Heartbeat| Humanoid pulse baseline |

## Auto-Calibration Trigger

- On first boot
- Every 72h
- After temperature delta > 20°C

## Manual Trigger

```bash
sudo ./calibrate_all.sh --force

