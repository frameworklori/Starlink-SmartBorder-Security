# Media ASR Pipeline

---

## Purpose

Process audio/video streams intercepted near border nodes for automatic speech recognition (ASR) using multilingual models (support: en, es, zh, fa).

---

## Flow

1. **Ingest Media**
- Format: `.mp4`, `.wav`, `.webm`
- Stream size ≤ 90 seconds
- Route: Edge node cache → ASR queue (Kafka)

2. **ASR Processing**
- Model: Whisper XL (locally fine-tuned)
- Output: `asr_transcript.json`
- Flags:
- Language confidence < 70% → retry in fallback
- Keywords matched → escalation level appended

3. **Post-Processing**
- Named Entity Recognition (NER): extract names/orgs
- Sentiment + urgency scoring
- Secure log to Command Center cloud with SHA-512 digest

---

## Retention
- ASR transcripts: 48h (unless flagged)
- Source audio: deleted post-transcribe unless `preserve_flag = true`

