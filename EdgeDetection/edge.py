import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

robert_x = np.array([
    [1, 0],
    [0, -1]
])

robert_y = np.array([
    [0, 1],
    [-1, 0]
])

BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, 'image', 'Faizal Unformal.jpg')

if not os.path.exists(image_path):
    print(f"File tidak ditemukan: {image_path}")
    print(f"File yang ada di folder 'image':")
    image_dir = os.path.join(BASE_DIR, 'image')
    if os.path.exists(image_dir):
        for f in os.listdir(image_dir):
            print(f"  - {f}")
    else:
        print(f"  Folder 'image' tidak ada di {BASE_DIR}")
    sys.exit(1)

image_color = img.imread(image_path)

if image_color.ndim == 3:
    image_gray = np.dot(image_color[...,:3], [0.299, 0.587, 0.114])
else:
    image_gray = image_color

image_gray = image_gray.astype(np.float64)

imgPad = np.pad(image_gray, mode='constant', pad_width=1, constant_values=0)

Gx = np.zeros_like(imgPad, dtype=np.float64)
Gy = np.zeros_like(imgPad, dtype=np.float64)

for y in range(imgPad.shape[0] - 1):
    for x in range(imgPad.shape[1] - 1):
        area = imgPad[y:y+2, x:x+2]
        Gx[y, x] = np.sum(area * robert_x)
        Gy[y, x] = np.sum(area * robert_y)

Gx_c = Gx[:-1, :-1]
Gy_c = Gy[:-1, :-1]

G = np.sqrt(Gx_c**2 + Gy_c**2)
if G.max() > 0:
    G = (G / G.max()) * 255
G = np.clip(G, 0, 255).astype(np.uint8)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)

if image_color.ndim == 3:
    try:
        plt.imshow(image_color.astype(np.uint8))
    except Exception:
        plt.imshow(image_color)
else:
    plt.imshow(image_gray, cmap='gray')

plt.subplot(2,2,2)
plt.imshow(Gx_c, cmap='gray')

plt.subplot(2,2,3)
plt.imshow(Gy_c, cmap='gray')

plt.subplot(2,2,4)
plt.imshow(G, cmap='gray')
plt.show()

plt.show()