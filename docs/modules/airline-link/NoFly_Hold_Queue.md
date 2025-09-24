# No-Fly Hold Queue Logic
© LORI Framework | airline-link/NoFly_Hold_Queue.md

Temporary queue for flagged passengers pending incident resolution. Separate from permanent no-fly list.

---

## Purpose:
- Prevent unjustified travel restriction due to false positive
- Allow buffer time for verification while respecting movement rights

---

## Queue Characteristics:
- Duration limit: **Max 4 hours** before auto-release
- Escalation required to transition to **Permanent No-Fly List**

---

## Data Tracked:
- passenger_id
- flight_id
- queue_entry_time
- resolution_status [pending / cleared / confirmed threat]
- source [thermal / gait / device / match]

---

## Removal Triggers:
- DHS manual clearance
- Boarding override authorized by TSA Supervisor
- SmartBorder risk level drops < 0.6 after 2nd AI pass

