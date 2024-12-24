# File: main.py
import cv2
import numpy as np
from respiration import extract_respiration_signal
from rppg import extract_rppg_signal
import matplotlib.pyplot as plt

# Fungsi utama untuk membaca video dari webcam dan memproses frame secara real-time
def main():
    cap = cv2.VideoCapture(0)  # Membuka akses ke webcam (kamera default perangkat).


    if not cap.isOpened():  # Memastikan webcam dapat diakses.

        print("Error: Tidak dapat mengakses webcam.")
        return

    plt.ion() # Mengaktifkan mode interaktif untuk pembaruan grafik secara real-time.
    fig, (resp_ax, rppg_ax) = plt.subplots(2, 1) # Membuat dua subplot untuk sinyal respirasi dan rPPG.
    resp_ax.set_title("Sinyal Respirasi")
    rppg_ax.set_title("Sinyal rPPG")

    respiration_signal = []
    rppg_signal = []

    while True: # Loop utama untuk membaca dan memproses frame webcam.
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak dapat membaca frame dari webcam.")
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Mengubah frame ke grayscale.
        resp_signal = extract_respiration_signal(frame_gray)
        rppg_signal.append(extract_rppg_signal(frame))

        respiration_signal.append(resp_signal)
        
        if len(respiration_signal) > 100: # Jika panjang data sinyal respirasi melebihi 100 sampel
            respiration_signal.pop(0) # Hapus data terlama untuk menjaga jumlah maksimum sampel tetap 100

        if len(rppg_signal) > 100: # Jika panjang data sinyal rPPG melebihi 100 sampel
            rppg_signal.pop(0) # Hapus data terlama untuk menjaga jumlah maksimum sampel tetap 100

        resp_ax.clear()
        resp_ax.plot(respiration_signal, label="Respiration")
        resp_ax.legend()

        rppg_ax.clear()
        rppg_ax.plot(rppg_signal, label="rPPG")
        rppg_ax.legend()

        plt.pause(0.01) # Memberikan jeda kecil untuk memperbarui grafik matplotlib.
        
        cv2.imshow('Webcam Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): # Tekan 'q' untuk keluar dari program.
            break

    cap.release() # Melepaskan resource webcam yang digunakan.
    cv2.destroyAllWindows() # Tutup semua jendela OpenCV yang terbuka.

if __name__ == "__main__":
    main()
