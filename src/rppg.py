import numpy as np
from scipy.signal import detrend

def extract_rppg_signal(frame):
    """
    Ekstrak sinyal rPPG dari frame video.
    Args:
        frame: Frame video dalam format array NumPy (BGR).
    Returns:
        Sinyal rPPG terdeteksi (float).
    """
    green_channel = frame[:, :, 1]  # Ambil channel hijau
    avg_signal = np.mean(green_channel, axis=0)  # Hitung rata-rata tiap kolom
    detrended_signal = detrend(avg_signal)  # Hilangkan tren linear
    return np.mean(detrended_signal)  # Kembalikan rata-rata sinyal setelah detrending
