# AI Risk Scoring Model
© LORI Framework | ai-analytics/Risk_Scoring.md

---

## Purpose:
Assign probabilistic risk values to observed crossing behavior for prioritization by human reviewers.

## Scoring Inputs:
- Gait anomaly score (0–1)
- Thermal profile deviation
- Cross-zone velocity
- Device presence / signal irregularity
- Location historical risk weight

## Score Formula:
Rᵢ = α₁·G + α₂·T + α₃·V + α₄·D + α₅·L

Where:
- G: Gait abnormality
- T: Thermal shift
- V: Velocity abnormality
- D: Device signal abnormality
- L: Location risk weight

## Thresholds:
- Rᵢ < 0.65 → Discard or log
- 0.65 ≤ Rᵢ < 0.82 → Queue for human review
- Rᵢ ≥ 0.82 → Alert escalation path
