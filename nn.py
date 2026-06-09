import cv2

# Menginisialisasi akses ke kamera bawaan (indeks 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak dapat mengakses kamera.")
    exit()

print("Kamera berhasil diakses. Tekan 'q' untuk keluar.")

while True:
    # Membaca frame demi frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Gagal menerima gambar dari kamera.")
        break

    # Menampilkan frame ke dalam jendela visual
    cv2.imshow('Aplikasi Kamera Sah', frame)

    # Menunggu input tombol 'q' untuk menutup aplikasi
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan resource kamera dan menutup semua jendela
cap.release()
cv2.destroyAllWindows()
