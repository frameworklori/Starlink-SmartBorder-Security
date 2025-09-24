# Voice Ingest Pipeline (for Live & Passive Surveillance)

---

## Input Channels

- Public zones: airport terminals, checkpoints, buses
- Input types:
- Live mic (via edge node)
- Streamed file uploads from federated partners

---

## Processing Stages

1. **Noise Filtering**
- Apply VAD (voice activity detection)
- Discard non-human signals
- Compress into `.opus` format

2. **Voiceprint Extraction**
- Convert into 512D embedding
- Compare against:
- Watchlist embeddings
- Known cleared profiles
- Threshold: cosine similarity > 0.87

3. **Voice Indexing**
- ID hashed, indexed
- Timestamped for replay lookup
- Can flag anomalies for behavioral review

---

## Output Schema

- `VoiceprintIndex.json` → full record with risk tags
- Alert routes to `LawEnforcement_Intake_API.yaml` if matched

