import numpy as np
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def extract_respiration_signal(frame, fs=30, lowcut=0.1, highcut=0.5):
    signal = np.mean(frame, axis=1)
    filtered_signal = bandpass_filter(signal, lowcut, highcut, fs)
    return filtered_signal[-1]  # Ambil nilai terbaru
