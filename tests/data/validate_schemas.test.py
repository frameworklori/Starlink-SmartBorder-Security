### Trigger Border Event
POST http://localhost:8000/api/border-event
Content-Type: application/json

{
"event_id": "EVT-20250925-0001",
"timestamp": "2025-09-25T13:45:00Z",
"location": {
"lat": 31.332,
"lon": -110.938
},
"detected_object": "human",
"risk_score": 0.87,
"thermal_signature": "high",
"voiceprint_id": "VP-449a8ff",
"source": "Starlink-Edge-Node-57"
}
