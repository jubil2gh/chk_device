import sounddevice as sd
import soundfile as sf
print(sd.query_devices())

dev_id = 37
data, samplerate = sf.read("./bell.wav")
# data, samplerate = sf.read("./output_record.wav")

print(f"Playing...DEV_ID={dev_id}")
data_loud = data * 2
sd.play(data_loud, samplerate, device=dev_id)
sd.wait()  # 재생 완료까지 대기
print("Done")
