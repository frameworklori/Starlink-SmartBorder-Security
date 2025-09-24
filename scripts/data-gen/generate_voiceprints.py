# generate_voiceprints.py
# Module: Voiceprint Data Generator for Zero-Trust Biometric Verification
# © 2025 – LORI Framework. All Rights Reserved.

import os
import uuid
import numpy as np
import soundfile as sf

def generate_synthetic_voiceprint(duration=3.0, samplerate=16000):
"""Generates a mock voiceprint as a sine wave audio file"""
freq = np.random.uniform(100, 1000)
t = np.linspace(0, duration, int(samplerate * duration), False)
signal = 0.5 * np.sin(2 * np.pi * freq * t)
return signal, samplerate

def save_voiceprint(user_id, output_dir):
voiceprint, sr = generate_synthetic_voiceprint()
filename = f"{user_id}_{uuid.uuid4().hex}.wav"
path = os.path.join(output_dir, filename)
sf.write(path, voiceprint, sr)
print(f"[+] Saved voiceprint: {path}")

if __name__ == "__main__":
output_dir = "./voiceprints"
os.makedirs(output_dir, exist_ok=True)
for user_id in range(10):
save_voiceprint(f"user{user_id}", output_dir)

