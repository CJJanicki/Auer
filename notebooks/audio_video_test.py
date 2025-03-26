import numpy as np
import cv2 as cv
import sounddevice as sd
import librosa

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

fs = 48000
bs=2048
sd.default.samplerate = fs
sd.default.channels = 1

def test_callback(indata, frames, time, status):
    pitch = librosa.yin(indata[:,0], fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=fs, frame_length=frames)
    print(pitch[0])

with sd.InputStream(callback = test_callback, blocksize=bs):
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break


sd.stop()
cap.release()
cv.destroyAllWindows()