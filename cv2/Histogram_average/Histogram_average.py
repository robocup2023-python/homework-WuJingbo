import cv2
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os


def Histogram_average(img):
    # 转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 手写实现灰度直方图均衡化
    height, width = gray.shape
    # 用字典表示离散转换函数
    trans = {}
    arr = np.zeros(256)
    for i in range(height):
        for j in range(width):
            arr[gray[i, j]] += 1
    arr /= height * width
    trans[0] = round(255 * arr[0], 0)
    # 统计分布函数并进行转换
    for i in range(1, 256):
        arr[i] += arr[i - 1]
        trans[i] = round(255 * arr[i], 0)

    new_img = np.zeros(gray.shape, dtype='uint8')
    for i in range(height):
        for j in range(width):
            new_img[i, j] = trans[gray[i, j]]
    return new_img


if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'img2.jpg')
    image = imageio.imread(image_path)

    # 进行直方图均衡化
    equalized_image = Histogram_average(image)
    imageio.imwrite(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'Histogram_average.png'), equalized_image)
    # 可视化原始图像和均衡化后的图像
    plt.subplot(121)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.subplot(122)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')
    plt.show()
