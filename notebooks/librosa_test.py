import librosa
import sounddevice as sd

fs = 48000
bs=2048
sd.default.samplerate = fs
sd.default.channels = 1

def test_callback(indata, frames, time, status):
    pitch = librosa.yin(indata[:,0], fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=fs, frame_length=frames)
    print(pitch[0])

with sd.InputStream(callback = test_callback, blocksize=bs):
    input("Press Enter to continue")
