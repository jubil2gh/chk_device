# 6-CH Array Mic Recorder

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

print(sd.query_devices())

samplerate = 44000        
duration = 15              # 녹음 시간 (초)
channels = 6              # 마이크 채널수

# 녹음
print("Recording...")
audio = sd.rec(int(duration * samplerate),
               samplerate=samplerate,
               channels=channels,
               device=0,
               dtype='int16')
sd.wait()
print("Recording finished")

# 파일 저장
write("output_record.wav", samplerate, audio)

print(f"Saved as output_record.wav @ {channels}CH")