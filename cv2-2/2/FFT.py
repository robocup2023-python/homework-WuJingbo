import imageio
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path):
    img = imageio.imread(image_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def FFT(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft) 
    img_phase = np.angle(fft_shift)
    img_freq = np.abs(fft_shift)
    return fft_shift,img_freq,img_phase

def apply_mask(f_transform_shifted, mask_radius):
    rows, cols = f_transform_shifted.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.uint8)
    cv2.circle(mask, (center_col, center_row), mask_radius, (0, 0, 0), -1)
    f_transform_shifted_masked = f_transform_shifted * mask
    return f_transform_shifted_masked

def restore_image(f_transform_shifted_masked):
    f_inverse_shifted = np.fft.ifftshift(f_transform_shifted_masked)
    image_restored = np.fft.ifft2(f_inverse_shifted).real
    return image_restored

def plot_images(original_image, masked_image, restored_image):
    plt.figure()
    
    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + masked_image), cmap='gray')
    plt.title('Masked')
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3)
    plt.imshow(restored_image, cmap='gray')
    plt.title('Restored')
    plt.xticks([]), plt.yticks([])

    plt.savefig(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'figure.png'))
    plt.show()

if __name__ == '__main__':
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img.jpg')
    image = read_image(image_path)
    f_transform_shifted, img_freq, img_phase = FFT(image)
    mask_radius = 500
    f_transform_shifted_masked = apply_mask(f_transform_shifted, mask_radius)
    image_restored = restore_image(f_transform_shifted_masked)
    plot_images(image, img_freq, image_restored)

