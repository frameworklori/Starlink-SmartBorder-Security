# Edge Node Provisioning

This document outlines the procedure for securely provisioning and configuring an edge node for Starlink-SmartBorder-Security deployments.

## Objectives

- Ensure consistent node setup across border environments.
- Apply Zero Trust security baselines.
- Enable Starlink uplink with fallback LTE.

## Procedure

1. **Boot from Verified Image**
- SHA256-verify LORI-EdgeOS.
- Install on hardened hardware.

2. **Assign Node Identity**
- Generate keypair (Ed25519).
- Register node with LORI-Ledger.

3. **Establish Connectivity**
- Primary: Starlink terminal activation.
- Backup: Cellular (4G/5G) fallback.

4. **Configure Sensors**
- Thermal, acoustic, and motion drivers.
- Auto-calibration routines run post-deployment.

5. **Secure the Node**
- Apply STRIDE Threat Model compliance.
- Enable full-disk encryption + TPM lock.

## Verification

Run:
```bash
./validate_node.sh --full

