
# Person vs. Animal Detection Model
© LORI Framework | ai-analytics/Person_vs_Animal_Model.md

---

## Objective:
Differentiate between human gait/thermal signatures and wildlife movement to prevent false alarms.

## Features Used:
- Biped gait pattern vs. quadruped motion
- Heat mass center stability
- Footstep interval range
- IR bounding box symmetry
- Horizontal vs. vertical stride ratio

## Model Type:
- Hybrid CNN + temporal LSTM
- Trained on >10,000 field-verified wildlife movement clips

## Accuracy:
- Human accuracy (TPR): 97.2%
- Animal detection suppression (TNR): 94.8%
