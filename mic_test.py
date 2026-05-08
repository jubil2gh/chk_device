import sounddevice as sd
import numpy as np

samplerate = 16000
channels = 6

print(sd.query_devices())
dev_id = 32

def callback(indata, frames, time, status):
    if status:
        print(status)

    # indata shape: (frames, channels)
    
    # 채널별 분리
    for ch in range(channels):
        channel_data = indata[:, ch]
        
        # 예시: RMS 값 계산
        rms = np.sqrt(np.mean(channel_data**2)) * 10000
        if ch == 0:
            print(f"Channel {ch+1} RMS: {rms:.8f}")

with sd.InputStream(channels=channels,
                    samplerate=samplerate,
                    dtype='float32',
                    device=dev_id,
                    callback=callback):

    print("Recording...DEV_ID={dev_id} (Ctrl+C로 종료)")
    try:
        while True:
            sd.sleep(1000)
    except KeyboardInterrupt:
        print("Stopped")