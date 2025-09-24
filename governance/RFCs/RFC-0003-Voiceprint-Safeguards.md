# RFC-0003: Safeguards for ZTV Voiceprint Module

## Problem
Voiceprint matching may trigger ethical/legal controversy in multilingual or trauma contexts.

## Proposal
- Add `consent_layer` on all NGO-triggered scans
- Apply accent drift compensation via multicultural phoneme libraries
- Flag rare dialects for human review

## Required by
- Humanitarian Alert Protocol (HAP)
- Alert_Scenarios.json
