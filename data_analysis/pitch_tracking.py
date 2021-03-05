import librosa
import numpy as np
import matplotlib.pyplot as plt

sr = 48000
y, sr = librosa.load("voice_samples/sample_5.wav", sr=sr)
pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr, n_fft=1000, fmin=75, fmax=2000, threshold=0.1)
np.set_printoptions(threshold=0)
print(pitches[np.nonzero(pitches)])
plt.plot(pitches[np.nonzero(pitches)])