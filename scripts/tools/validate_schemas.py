# validate_schemas.py
# Module: JSON Schema Validator for Event Data Structures
# © 2025 – LORI Framework. All Rights Reserved.

import json
import jsonschema
from jsonschema import validate

EVENT_SCHEMA = {
"type": "object",
"properties": {
"timestamp": {"type": "string"},
"event_id": {"type": "string"},
"type": {"type": "string"},
"device_id": {"type": "string"},
"user_ref": {"type": "string"}
},
"required": ["timestamp", "event_id", "type", "device_id", "user_ref"]
}

def validate_event_file(file_path):
with open(file_path, 'r') as f:
events = json.load(f)

for idx, event in enumerate(events):
try:
validate(instance=event, schema=EVENT_SCHEMA)
except jsonschema.exceptions.ValidationError as ve:
print(f"[!] Validation error in event #{idx}: {ve.message}")
else:
print(f"[✓] Event #{idx} valid.")

if __name__ == "__main__":
validate_event_file("mock_event_log.json")

