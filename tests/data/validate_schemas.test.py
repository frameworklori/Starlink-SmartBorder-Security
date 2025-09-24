import json
import jsonschema
import unittest
from pathlib import Path

class TestSchemaValidation(unittest.TestCase):
def setUp(self):
self.schema_dir = Path("docs/specs/data/entities/schemas")
self.data_dir = Path("examples/Sample_Alerts")

with open(self.schema_dir / "AlertSchema.json") as f:
self.alert_schema = json.load(f)

def test_alert_airline_gate_hold(self):
with open(self.data_dir / "alert_airline_gate_hold.json") as f:
alert = json.load(f)
jsonschema.validate(instance=alert, schema=self.alert_schema)

def test_alert_border_crossing(self):
with open(self.data_dir / "alert_border_crossing.json") as f:
alert = json.load(f)
jsonschema.validate(instance=alert, schema=self.alert_schema)

def test_alert_university_leak(self):
with open(self.data_dir / "alert_university_leak.json") as f:
alert = json.load(f)
jsonschema.validate(instance=alert, schema=self.alert_schema)

if __name__ == "__main__":
unittest.main()
