
# Data Exfiltration Detection
© LORI Framework | outflow-control/Data_Exfiltration_Detection.md

---

## Purpose:
To detect attempts at smuggling sensitive data across the border using personal or corporate devices.

---

## Detection Techniques:
- Cross-match high entropy volume spikes (USB, SD, laptop)
- Detect presence of `exfil-indicator files` (compressed, obfuscated, or non-standard encodings)
- AI flagging of suspicious MAC address reuse
- Air-gapped sniffers in gate zones for passive radio scan

---

## Alert Thresholds:
| Flag Level | Indicators Detected |
|------------|---------------------|
| Yellow | Obfuscated ZIP + script file on USB
| Orange | AirDrop/Bluetooth triggered + unpaired device in proximity
| Red | Device shows covert OS partition / encrypted partition + velocity match to flagged person

---

## Mitigation:
- Temporary device quarantine
- Option to decline entry/re-entry
- Full forensic scan (with warrant)
