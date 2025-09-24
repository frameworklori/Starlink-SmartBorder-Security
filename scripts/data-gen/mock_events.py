# mock_events.py
# Module: Synthetic Event Generator for Border Scenario Simulations
# © 2025 – LORI Framework. All Rights Reserved.

import random
import json
from datetime import datetime, timedelta

EVENT_TYPES = ["ENTRY_ATTEMPT", "CALLBACK_ALERT", "FRAUD_FLAG", "BIOMETRIC_FAIL", "DOCUMENT_MISMATCH"]

def generate_event():
event = {
"timestamp": (datetime.utcnow() - timedelta(minutes=random.randint(0, 5000))).isoformat() + "Z",
"event_id": f"EVT-{random.randint(100000,999999)}",
"type": random.choice(EVENT_TYPES),
"device_id": f"DEVICE-{random.randint(1000,9999)}",
"user_ref": f"user_{random.randint(1, 100)}"
}
return event

def generate_batch(n=100):
return [generate_event() for _ in range(n)]

if __name__ == "__main__":
events = generate_batch(50)
with open("mock_event_log.json", "w") as f:
json.dump(events, f, indent=2)
print("[+] Generated mock events to mock_event_log.json")

