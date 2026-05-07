import sounddevice as sd
import soundfile as sf

data, samplerate = sf.read("./bell.wav")
# data, samplerate = sf.read("./output_record.wav")

print("Playing...")
data_loud = data * 2
sd.play(data_loud, samplerate, device=2)
sd.wait()  # 재생 완료까지 대기
print("Done")