import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from scipy.ndimage import gaussian_filter, median_filter
from scipy.signal import convolve2d

# KERNEL FILTER
# Kernel averaging 3x3 untuk smoothing gambar
# Setiap pixel diganti dengan rata-rata pixel tetangganya
averaging_kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# BACA GAMBAR
# Tentukan direktori base dan path gambar
BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, 'image', 'al.jpeg')

# Validasi file ada
if not os.path.exists(image_path):
    print(f"File tidak ditemukan: {image_path}")
    sys.exit(1)

# Baca gambar dalam format RGB
image_color = img.imread(image_path)

# KONVERSI KE GRAYSCALE
# Jika gambar berwarna (3 channel), konversi ke grayscale
# Menggunakan weighted average: R*0.299 + G*0.587 + B*0.114
if image_color.ndim == 3:
    image_gray = np.dot(image_color[...,:3], [0.299, 0.587, 0.114])
else:
    image_gray = image_color

# Ubah ke float64 untuk kalkulasi
image_gray = image_gray.astype(np.float64)

# TAMBAHKAN NOISE (SIMULASI GAMBAR RUSAK)
# Tambahkan Gaussian noise untuk simulasi gambar yang terdegradasi
# Noise dibuat dengan distribusi normal (mean=0, std=15)
noise = np.random.normal(0, 15, image_gray.shape)
image_noisy = image_gray + noise
image_noisy = np.clip(image_noisy, 0, 255)

# RESTORATION - GAUSSIAN FILTER
# Filter Gaussian untuk smoothing gambar
# sigma=1.0 mengontrol tingkat smoothing
# Efektif untuk menghilangkan Gaussian noise
image_gaussian = gaussian_filter(image_noisy, sigma=1.0)

# RESTORATION - MEDIAN FILTER
# Median filter sangat efektif untuk salt-and-pepper noise
# Mengganti setiap pixel dengan median nilai tetangganya
# size=3 berarti menggunakan kernel 3x3
image_median = median_filter(image_noisy, size=3)

# RESTORATION - AVERAGING FILTER
# Convolve gambar dengan averaging kernel
# Setiap pixel dirata-ratakan dengan tetangganya
# mode='same' = output ukuran sama dengan input
# boundary='symm' = padding simetri
image_averaging = convolve2d(image_noisy, averaging_kernel, mode='same', boundary='symm')
image_averaging = np.clip(image_averaging, 0, 255)

# VISUALISASI HASIL
# Buat figure dengan 6 subplot untuk perbandingan
plt.figure(figsize=(16, 12))

# Subplot 1: Gambar original (tanpa noise)
plt.subplot(2, 3, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Gambar Original (Tanpa Noise)', fontsize=12, fontweight='bold')
plt.axis('off')

# Subplot 2: Gambar dengan noise (rusak)
plt.subplot(2, 3, 2)
plt.imshow(image_noisy, cmap='gray')
plt.title('Gambar Rusak (Dengan Noise)', fontsize=12, fontweight='bold')
plt.axis('off')

# Subplot 3: Hasil restoration dengan Gaussian filter
plt.subplot(2, 3, 3)
plt.imshow(image_gaussian, cmap='gray')
plt.title('Restoration: Gaussian Filter', fontsize=12, fontweight='bold')
plt.axis('off')

# Subplot 4: Hasil restoration dengan Median filter
plt.subplot(2, 3, 4)
plt.imshow(image_median, cmap='gray')
plt.title('Restoration: Median Filter', fontsize=12, fontweight='bold')
plt.axis('off')

# Subplot 5: Hasil restoration dengan Averaging filter
plt.subplot(2, 3, 5)
plt.imshow(image_averaging, cmap='gray')
plt.title('Restoration: Averaging Filter', fontsize=12, fontweight='bold')
plt.axis('off')

# Subplot 6: Perbandingan sebelum dan sesudah restoration
plt.subplot(2, 3, 6)
combined = np.hstack([image_noisy, image_gaussian])
plt.imshow(combined, cmap='gray')
plt.title('Sebelum (kiri) vs Sesudah Gaussian (kanan)', fontsize=12, fontweight='bold')
plt.axis('off')

# Tata letak subplot
plt.tight_layout()

# Tampilkan semua subplot
plt.show()

print("Program selesai!")
