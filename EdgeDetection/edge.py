import imageio.v2 as img
import numpy as np
import matplotlib.pyplot as plt

sobel_x = np.array([
    [ -1, 0, 1],
    [ -2, 0, 2],
    [ -1, 0, 1]
])

sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

# Use a raw string for Windows path to avoid escape-sequence warnings
image_path = r'C:\Pemrograman\kuliah\smt5\Picidi\image\Faizal Unformal.jpg'
image_color = img.imread(image_path)

# Convert to grayscale if the image has color channels
if image_color.ndim == 3:
    # keep only first three channels if alpha is present
    image_gray = np.dot(image_color[...,:3], [0.299, 0.587, 0.114])
else:
    image_gray = image_color

# Work in float for convolution
image_gray = image_gray.astype(np.float64)

# Pad the grayscale image (2D) by 1 pixel
imgPad = np.pad(image_gray, mode='constant', pad_width=1, constant_values=0)

# Prepare gradient arrays (same shape as padded image)
Gx = np.zeros_like(imgPad, dtype=np.float64)
Gy = np.zeros_like(imgPad, dtype=np.float64)

# Convolve with Sobel kernels
for y in range(1, imgPad.shape[0] - 1):
    for x in range(1, imgPad.shape[1] - 1):
        area = imgPad[y-1:y+2, x-1:x+2]
        Gx[y, x] = np.sum(area * sobel_x)
        Gy[y, x] = np.sum(area * sobel_y)

# Crop out the padding to return to the original image size
Gx_c = Gx[1:-1, 1:-1]
Gy_c = Gy[1:-1, 1:-1]

# Gradient magnitude
G = np.sqrt(Gx_c**2 + Gy_c**2)
if G.max() > 0:
    G = (G / G.max()) * 255
G = np.clip(G, 0, 255).astype(np.uint8)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
# Show color image if available, otherwise show grayscale
if image_color.ndim == 3:
    # ensure integer type for display
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