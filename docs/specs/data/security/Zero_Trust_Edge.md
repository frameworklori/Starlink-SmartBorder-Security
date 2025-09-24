# Zero Trust at Starlink Edge Nodes

## Principles
- Trust no device by default (even within Starlink)
- Enforce token + biometric + geo-location auth

## Controls
- Device fingerprinting per boot
- Behavior anomaly detection model
- Edge-side policy enforcement (micro-firewall)

## Federation
- Federated node-to-node token negotiation every 6h
