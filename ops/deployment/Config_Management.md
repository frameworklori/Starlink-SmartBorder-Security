# Configuration Management Layer

- Uses JSON/YAML configs per node (`sample_edge_config.yaml`)
- Versioned updates via GitOps
- Environment secrets handled via Vault (not included)
- Config channels split by region (`/ops/environments/US_Southwest/`, etc.)
