# Blue-Green Deployment Strategy

## Rationale
To ensure rollback-safe deployment of edge nodes in volatile or multi-national zones.

## Process
- Green: Current verified stable version
- Blue: Experimental patch with failover logic
- Canary test using 2 edge-nodes per country
- Rollback if false alert ratio > 0.1%

## Auditable Step:
✔ Logs hashed and stored on LORI-Ledger via ZTV
