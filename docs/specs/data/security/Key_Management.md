# Key Management Strategy

## Objectives
- Secure encryption/decryption keys across distributed Starlink Edge + Cloud
- Avoid key reuse, enforce rotation, and segment privileges

## Components
- 🔐 Hardware Security Module (HSM) on core Starlink nodes
- 🔄 Rotation Interval: 90 days or upon personnel change
- 🔑 Separate keys per module: Gait, Voiceprint, Cloud Log

## Storage
- Keys encrypted at rest with master root key (stored offline)
- Edge keys cached short-term in TPM-backed memory

## Access Controls
- Only cert-authenticated operators
- Full audit trail logged to immutable ledger

