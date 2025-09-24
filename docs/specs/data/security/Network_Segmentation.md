# Network Segmentation Protocol

## Purpose
Minimize attack surface by strictly isolating Starlink modules and sensor grids.

## Zones
- **Zone A**: Sensor grid → no internet access
- **Zone B**: Edge compute nodes → direct sensor feed
- **Zone C**: Command Center → control & analytics
- **Zone D**: Law Enforcement gateway API

## Rules
- No lateral traffic across zones without Zero Trust token
- VPN tunneling forbidden between Edge and Cloud
