Analisa Perbandingan:

Hasil deteksi tepi pada citra menunjukkan perbedaan karakter yang jelas antara kernel Roberts dan operator Sobel. Kernel Roberts menghasilkan garis tepi yang tampak lebih tipis dan tajam karena menggunakan operasi 2×2 yang bekerja pada perubahan intensitas diagonal. Karakter ini membuat tepi dapat muncul dengan cepat dan responsif terhadap variasi kontras, namun efek sampingnya adalah munculnya noise halus pada area gelap maupun tekstur yang tidak terlalu jelas. Sebaliknya, operator Sobel menggunakan kernel 3×3 dengan pembobotan sehingga proses smoothing terjadi secara alami. Dampaknya dapat dilihat pada tepi yang lebih tebal, stabil, dan mudah diinterpretasikan, khususnya pada bagian kontur wajah, pakaian, serta transisi cahaya pada citra.

Secara komparatif, dapat disimpulkan:
- Kernel Roberts bersifat sangat sensitif terhadap perubahan kecil, namun rentan terhadap noise karena tidak adanya mekanisme peredaman.
- Sobel mampu menghasilkan hasil yang lebih halus dan konsisten melalui bobot kernel, sehingga bentuk dan kontur objek menjadi lebih jelas.
- Pada citra manusia, Sobel memberikan kualitas deteksi yang lebih informatif, terutama ketika diperlukan stabilitas visual.
- Roberts tetap relevan ketika kecepatan dan sensitivitas menjadi prioritas, misalnya untuk deteksi sederhana atau citra dengan kontras tinggi.
- Secara umum, Sobel menjadi pilihan yang lebih seimbang antara akurasi dan ketahanan terhadap noise, sedangkan Roberts menonjol dalam detail lokal namun kurang robust.

Dengan demikian, perbedaan ini menunjukkan bahwa pemilihan operator deteksi tepi sebaiknya mempertimbangkan konteks penggunaan, karakter citra, serta kebutuhan stabilitas atau sensitivitas yang ingin dicapai.