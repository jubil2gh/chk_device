import sounddevice as sd
import soundfile as sf

data, samplerate = sf.read("./bell.wav")

# 1) Check Device ID
print(sd.query_devices())
dev_id = int(input('Insert Audio Device ID >> '))

# 2) Insert Repeat Num
num_repeat = int(input('Insert Repeat Num >> '))

# 3) Volume Gain
vol_gain = int(input('Insert Volume Gain(1 ~ 10) >> '))

print('>> Select Device ID = ', dev_id)
print('>> Repeat Num = ', num_repeat)

print(f"Playing...DEV_ID = {dev_id}")
data_loud = data * vol_gain
for i in range(num_repeat):
    sd.play(data_loud, samplerate, device=dev_id)
    sd.wait()  # 재생 완료까지 대기
    
print("Done")
