import numpy as np
import pyaudio
import sys

# Set the parameters for the PyAudio stream
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Define a function to calculate the frequency of a signal
def frequency(signal):
    fourier = np.fft.fft(signal)
    magnitude = np.abs(fourier)
    index = np.argmax(magnitude)
    length = len(signal)
    frequency = index * RATE / length
    return frequency

# Define a function to determine the musical note based on its frequency
def musical_note_frequency(frequency):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_index = int(round(12 * np.log2(frequency / 440))) % 12
    return notes[note_index]

# Create a PyAudio stream
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Continuously record and analyze the microphone input
while True:
    data = stream.read(CHUNK)
    signal = np.frombuffer(data, dtype=np.int16)
    frequency = frequency(signal)
    musical_note = musical_note_frequency(frequency)
    print(musical_note)

# Close the PyAudio stream
stream.stop_stream()
stream.close()
p.terminate()
