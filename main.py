import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

duration = 3  # 신호 길이 (초)
sample_rate = 44100  # 샘플링 주파수 (Hz)
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False) # 시간 축
# matplotlib 폰트 설정
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

octave_freq = [131, 139 , 147, 156,  165, 175, 185, 196 , 208, 220, 233 , 247] # 옥타브에 따른 주파수
octave_name = ['도','도#','레','레#','미','파','파#','솔','솔#','라','라#','시'] # 옥타브에 따른 계이름
notes = [2,7]
# np.sign()
wave1 = 0.5 * np.sin(4 * np.pi * octave_freq[notes[0]] * t)  # 첫 번째 파형
wave2 = 0.5 * np.sin(4 * np.pi * octave_freq[notes[1]] * t)  # 두 번째 파형
waves = [wave1, wave2]
interference_wave = wave1 + wave2 # 간섭 파형

# 시각화
plt.figure(figsize=(10, 6))

for i in range(2): # 파형 2개 반복문 돌리기
    plt.subplot(3, 1, i+1)
    plt.plot(t[:1000], waves[i][:1000])
    plt.title(f"파형 {i+1} ({octave_freq[notes[i]]*2} Hz, {octave_name[notes[i]]})")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

# 간섭 파형
plt.subplot(3, 1, 3)
plt.plot(t[:1000], interference_wave[:1000])
plt.title("간섭 파형(두 파형을 더한 화음)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# 소리 재생
print("Playing Interference Wave...")
sd.play(interference_wave, sample_rate)
sd.wait()
print("Done!")
