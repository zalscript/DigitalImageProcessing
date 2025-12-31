Analisis singkat

Program `restorasi.py` bertujuan memperlihatkan efek beberapa metode restorasi citra dalam domain spasial terhadap citra yang diberikan noise sintetis. Pendekatan yang digunakan meliputi: pembacaan citra, konversi ke skala abu-abu, penambahan noise Gaussian aditif, serta penerapan tiga operator restorasi—Gaussian smoothing, median filter, dan averaging (konvolusi 3×3). Hasil ditampilkan secara visual untuk perbandingan.

Penjelasan  per bagian kode:
- Pembacaan dan validasi file: Menjamin citra dapat dibaca dari folder proyek; kegagalan baca dihentikan dengan pesan yang jelas.
- Konversi ke grayscale: Menggunakan bobot luminansi standar (0.299, 0.587, 0.114) untuk memperoleh representasi intensitas yang sesuai persepsi.
- Tipe data `float64`: Dipilih untuk mengurangi pembulatan selama operasi numerik (penambahan noise dan filtering).
- Simulasi noise: Noise Gaussian aditif (μ=0, σ=15) ditambahkan ke citra sebagai model degradasi sederhana.
- Gaussian filter: Operator linear low-pass yang mereduksi komponen frekuensi tinggi secara bertahap; parameter `sigma` mengatur besaran smoothing.
- Median filter: Operator non-linear yang mengganti nilai pixel dengan median tetangganya; efektif terhadap noise impuls (salt-and-pepper) dan lebih menjaga tepi.
- Averaging (konvolusi 3×3): Filter linear sederhana yang meratakan intensitas lokal; implementasinya dengan `convolve2d` dan padding simetri untuk mengurangi artefak tepi.
- Visualisasi: Enam subplot menyajikan citra asli, citra ber-noise, hasil Gaussian, median, averaging, serta perbandingan sebelum/sesudah.

Interpretasi hasil:
- Gaussian menurunkan noise terdistribusi tetapi mengaburkan detail halus dan tepi.
- Median menjaga tepi relatif lebih baik pada noise impuls, namun kurang efektif terhadap noise Gaussian halus.
- Averaging menghasilkan blur yang paling nyata di antara ketiganya, namun mudah dan cepat.
- Penilaian visual membantu memahami perilaku metode, namun kesimpulan ilmiah memerlukan pengukuran kuantitatif.

Keterbatasan:
- Hanya menangani kasus grayscale (warna diproyeksikan ke luminansi).
- Noise yang diuji tunggal (Gaussian aditif); kondisi nyata dapat lebih kompleks.
- Parameter filter bersifat tetap (hard-coded), sehingga tidak ada analisis sensitivitas.
- Tidak ada metrik kuantitatif (MSE/PSNR/SSIM) untuk evaluasi objektif.

Petunjuk singkat menjalankan program:
1. Pasang dependensi: `pip install imageio numpy matplotlib scipy`
2. Letakkan gambar di folder `image` dan beri nama sesuai yang dipanggil oleh skrip.
3. Jalankan: `python restorasi.py`

File kode terkait: `restorasi.py`
