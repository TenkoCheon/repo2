import cv2

# Muat gambar
image = cv2.imread('alat-tulis.jpg')

# Ubah gambar menjadi skala abu-abu
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deteksi tepi menggunakan Canny
edges = cv2.Canny(gray, 30, 150)

# Temukan kontur dari tepi yang telah dideteksi
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Inisialisasi jumlah pensil
jumlah_pensil = 0

# Loop melalui setiap kontur
for contour in contours:
    # Hitung luas kontur
    area = cv2.contourArea(contour)
    
    # Tentukan apakah kontur sesuai dengan kriteria pensil
    if area > 1000:  # Misalnya, kontur dengan luas di atas 1000 piksel dianggap sebagai pensil
        jumlah_pensil += 1

# Tampilkan jumlah pensil
print("Jumlah pensil : ", jumlah_pensil)

# Tampilkan gambar dengan kontur yang ditemukan (opsional)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('2D Object Scanner', image)
cv2.waitKey(0)
cv2.destroyAllWindows()