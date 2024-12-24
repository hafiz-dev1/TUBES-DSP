import numpy as np
from scipy.signal import detrend

def extract_rppg_signal(frame):
    green_channel = frame[:, :, 1]
    avg_signal = np.mean(green_channel)
    detrended_signal = detrend(avg_signal)
    return detrended_signal
