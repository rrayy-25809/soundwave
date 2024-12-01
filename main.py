import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

duration = 3  # 신호 길이 (초)
sample_rate = 44100  # 샘플링 주파수 (Hz)
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False) # 시간 축

octave = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247] # 옥타브에 따른 주파수
freq1 = octave[5]*2
freq2 = octave[9]*2

wave1 = 0.5 * np.sin(2 * np.pi * freq1 * t)  # 첫 번째 파형
wave2 = 0.5 * np.sin(2 * np.pi * freq2 * t)  # 두 번째 파형
interference_wave = wave1 + wave2 # 간섭 파형

# 5. 시각화
plt.figure(figsize=(10, 6))

# 첫 번째 파형
plt.subplot(3, 1, 1)
plt.plot(t[:1000], wave1[:1000])
plt.title("Wave 1 (440 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# 두 번째 파형
plt.subplot(3, 1, 2)
plt.plot(t[:1000], wave2[:1000])
plt.title("Wave 2 (444 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# 간섭 파형
plt.subplot(3, 1, 3)
plt.plot(t[:1000], interference_wave[:1000])
plt.title("Interference Wave (Sum of Wave 1 and Wave 2)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# 6. 소리 재생
print("Playing Interference Wave...")
sd.play(interference_wave, sample_rate)
sd.wait()
print("Done!")
