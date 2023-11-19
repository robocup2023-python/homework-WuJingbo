import cv2
import os
import imageio
import matplotlib.pyplot as plt
import numpy as np

def FFT(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft) 
    img_phase = np.angle(fft_shift)
    img_freq = np.abs(fft_shift)
    return fft_shift,img_freq,img_phase

if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'img.jpg')
    img = imageio.imread(image_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    fft_shift, img_freq, img_phase = FFT(gray)
    imageio.imwrite(os.path.join(os.path.dirname(
          os.path.abspath(__file__)), 'frequency.jpg'),np.log1p(img_freq))
    imageio.imwrite(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'phase.png'), img_phase)
    
    # 可视化
    plt.subplot(131), plt.imshow(np.log1p(img_freq), cmap='gray')
    plt.title('Frequency'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(img_phase, cmap='gray')
    plt.title('Phase'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(np.log1p(np.abs(fft_shift)), cmap='gray')
    plt.title('Shifted FFT'), plt.xticks([]), plt.yticks([])
    # plt.show()
