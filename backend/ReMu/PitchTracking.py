import crepe
from scipy.io import wavfile
import io
import wave
import MM
import ffmpeg
import os

def get_pitch(file):
    outname = file.name.replace('.webm', '.wav')
    (
        ffmpeg
        .input('media/'+file.name)
        .output('media/'+outname, format='wav', ac=1)
        .run()
    )
    sr, audio = wavfile.read('media/'+outname)
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
    os.remove("media/"+file.name)
    os.remove("media/"+outname)
    return max(frequency)

def get_pitch_file(file):
    sr, audio = wavfile.read('media/'+file.name)
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
    os.remove("media/"+file.name)
    return max(frequency)