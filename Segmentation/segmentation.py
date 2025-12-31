import numpy as np
import imageio
import matplotlib.pyplot as plt
import os


def create_sample_image():
    """Membuat citra sample"""
    os.makedirs('image', exist_ok=True)
    
    # Buat gradient image dengan shapes
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    for i in range(300):
        img[i, :] = int(i / 300 * 255)
    
    img[50:100, 50:100] = [255, 0, 0]
    img[150:200, 50:100] = [0, 255, 0]
    img[100:150, 150:250] = [0, 0, 255]
    
    imageio.imwrite('image/Faizal Unformal.png', img)
    return img


def to_grayscale(img):
    """Konversi ke grayscale"""
    if len(img.shape) == 3:
        return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return img.astype(np.uint8)


def binary_threshold(gray_img, threshold):
    """Binary thresholding"""
    return np.where(gray_img >= threshold, 255, 0).astype(np.uint8)


def otsu_threshold(gray_img):
    """Otsu automatic thresholding"""
    hist, _ = np.histogram(gray_img, 256, [0, 256])
    hist = hist.astype(np.float32) / hist.sum()
    
    weight_bg = np.cumsum(hist)
    weight_fg = 1.0 - weight_bg
    mean_total = np.cumsum(hist * np.arange(256))
    mean_bg = mean_total / weight_bg
    mean_fg = (mean_total[-1] - mean_total) / weight_fg
    
    variance = weight_bg * weight_fg * (mean_bg - mean_fg) ** 2
    otsu_value = np.argmax(variance)
    
    return binary_threshold(gray_img, otsu_value), otsu_value


def display_results(original, gray, seg_binary, seg_otsu, otsu_value, threshold=128):
    """Menampilkan hasil segmentasi"""
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))
    fig.suptitle('Segmentasi Citra - Basic Thresholding', fontsize=14, fontweight='bold')
    
    # Original
    axes[0, 0].imshow(original)
    axes[0, 0].set_title('Original')
    axes[0, 0].axis('off')
    
    # Grayscale
    axes[0, 1].imshow(gray, cmap='gray')
    axes[0, 1].set_title('Grayscale')
    axes[0, 1].axis('off')
    
    # Histogram
    hist, _ = np.histogram(gray, 256, [0, 256])
    axes[0, 2].plot(hist, color='blue')
    axes[0, 2].axvline(threshold, color='red', linestyle='--', label=f'T={threshold}')
    axes[0, 2].axvline(otsu_value, color='green', linestyle='--', label=f'Otsu={otsu_value}')
    axes[0, 2].set_title('Histogram')
    axes[0, 2].set_xlabel('Intensitas')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)
    
    # Binary Threshold
    axes[1, 0].imshow(seg_binary, cmap='gray')
    axes[1, 0].set_title(f'Binary Threshold = {threshold}')
    axes[1, 0].axis('off')
    
    # Otsu Threshold
    axes[1, 1].imshow(seg_otsu, cmap='gray')
    axes[1, 1].set_title(f'Otsu Threshold = {otsu_value}')
    axes[1, 1].axis('off')
    
    # Difference
    diff = np.abs(seg_binary.astype(float) - seg_otsu.astype(float))
    axes[1, 2].imshow(diff, cmap='hot')
    axes[1, 2].set_title('Perbedaan Metode')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    return fig


# Main
if __name__ == "__main__":
    print("="*50)
    print("SEGMENTASI CITRA - BASIC THRESHOLDING")
    print("="*50)
    
    # Load/create image
    print("\n[1] Membuat citra sample...")
    original = create_sample_image()
    
    # Convert to grayscale
    print("[2] Konversi ke grayscale...")
    gray = to_grayscale(original)
    
    # Binary thresholding
    print("[3] Binary thresholding (T=128)...")
    seg_binary = binary_threshold(gray, 128)
    imageio.imwrite('image/segmented_binary.png', seg_binary)
    
    # Otsu thresholding
    print("[4] Otsu thresholding...")
    seg_otsu, otsu_value = otsu_threshold(gray)
    imageio.imwrite('image/segmented_otsu.png', seg_otsu)
    print(f"    Otsu threshold value: {otsu_value}")
    
    # Display
    print("[5] Menampilkan hasil...")
    fig = display_results(original, gray, seg_binary, seg_otsu, otsu_value, 128)
    fig.savefig('image/comparison.png', dpi=100, bbox_inches='tight')
    
    print("\nSelesai! Hasil disimpan di folder 'image/'")
    plt.show()
