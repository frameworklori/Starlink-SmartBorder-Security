# Carrier API Specification
© LORI Framework | airline-link/Carrier_API_Spec.md

This specification defines how airlines transmit passenger manifest and receive alert feedback from the SmartBorder gateway.

---

## Endpoint 1: Manifest Submission
`POST /api/v1/carrier/manifest`

### Required Fields:
- flight_number
- date_time_departure
- carrier_id
- passenger_list [ { name, passport, nationality, dob, ticket_ref } ]

### Response:
- `202 Accepted`
- `200 GreenListProcessed`
- `400 Malformed Manifest`

---

## Endpoint 2: Risk Flag Feedback
`GET /api/v1/risk-review/:passenger_id`

### Returns:
```json
{
"passenger_id": "ABC123456",
"risk_flag": "YELLOW",
"flag_reason": "Thermal+Gait match at crossing node",
"review_required": true
}

