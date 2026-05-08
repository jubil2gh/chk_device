import sounddevice as sd
import numpy as np

samplerate = 16000
channels = 6
rms_tbl = [0 for i in range(channels)]

# 1) Check Device ID
print(sd.query_devices())
dev_id = int(input('Insert 6ch-Mic Device ID >> '))

# 2) Insert Recording Time
recording_time = int(input('Insert Recording Time >> '))

def callback(indata, frames, time, status):
    if status:
        print(status)

    # indata shape: (frames, channels)
    
    # 채널별 분리
    for ch in range(channels):
        channel_data = indata[:, ch]
        
        # 예시: RMS 값 계산
        rms = np.sqrt(np.mean(channel_data**2)) * 10
        rms_tbl[ch] = rms
        # if ch == 0:
        #     print(f"Channel {ch+1} RMS: {rms:.8f}")
    print(f'[1]:{rms_tbl[0]:.3f} [2]:{rms_tbl[1]:.3f} [3]:{rms_tbl[2]:.3f} [4]:{rms_tbl[3]:.3f} [5]:{rms_tbl[4]:.3f} [6]:{rms_tbl[5]:.3f}')
    # print(f'[1]:{rms_tbl[0]:10.3f} [2]:{rms_tbl[1]:10.3f} [3]:{rms_tbl[2]:3.3f} [4]:{rms_tbl[3]:3.3f} [5]:{rms_tbl[4]:3.3f} [6]:{rms_tbl[5]:3.3f}')
with sd.InputStream(channels=channels,
                    samplerate=samplerate,
                    dtype='float32',
                    device=dev_id,
                    callback=callback):

    print(f"{recording_time}s Recording...DEV_ID={dev_id} (Ctrl+C로 종료)")
    try:
        while True:
            sd.sleep(recording_time)
    except KeyboardInterrupt:
        print("Stopped")