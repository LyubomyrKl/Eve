import wave as wv
import numpy as np
import matplotlib.pyplot as plt
import pyaudio

# The sample means the number of times the sound is sampled per second. Since analogue audio is signal
# we represent it with a number of samples. The more samples we have, the more accurate the sound is.
# The higher the sample rate, the higher the frequency of the sound. The sample rate is measured in Hertz (Hz).
# The sample rate is also called the sample frequency or the sampling frequency.

wav_obj = wv.open('Television.wav', 'r')\

# - sample width - number of bits for each sample
sample_width = wav_obj.getsampwidth()
print('Sample width:', sample_width)

# - number of channels - mono or stereo. Stereo means that sound comes from two different directions.
n_channels = wav_obj.getnchannels()
print('Number of channels:', n_channels)

# - framerate/sample rate/sample frequency - this means the number of sample for each second (44.100 Hz for example )
sample_freq = wav_obj.getframerate()
print('Frequency:', sample_freq)

# - number of frames (samples) - a.k.a all frames in audio. number of frames = seconds * framerate
n_samples = wav_obj.getnframes()
print('Count of samples:', n_samples)

# - signal wave - this is the actual sound wave. It is a string of bytes representing the sound.
signal_wave = wav_obj.readframes(n_samples)
# print('Signal wave:', signal_wave)

# - signal array - this is the signal wave converted to a numpy array
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
print('Signal array:', signal_array)

# - time array - this is the time array for one second
t_audio = n_samples / sample_freq
times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


recorder = pyaudio.PyAudio()
stream = recorder.open(format=pyaudio.paInt16, channels=1, rate=sample_freq, input=True, frames_per_buffer=1024)
frames = []

for i in range(0, int(sample_freq / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

stream.stop_stream()








