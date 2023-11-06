import cv2
import numpy as np
import os
import imageio
import matplotlib.pyplot as plt


def canny_edge_detection(image, sigma=0.33):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 高斯模糊
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 计算梯度幅值和方向
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
    gradient_direction = np.arctan2(sobely, sobelx) * 180 / np.pi

    # 使用非极大值抑制
    nms_image = non_maximum_suppression(gradient_magnitude, gradient_direction)

    # 双阈值滞后阈值处理
    lower_threshold, upper_threshold = calculate_thresholds(blurred, sigma)
    final_edges = hysteresis_thresholding(
        nms_image, lower_threshold, upper_threshold)

    # 可视化展示结果
    plt.subplot(131)
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Gradient Magnitude')
    plt.subplot(132)
    plt.imshow(nms_image, cmap='gray')
    plt.title('Non-Maximum Suppression')
    plt.subplot(133)
    plt.imshow(final_edges, cmap='gray')
    plt.title('Final Edges')
    plt.show()

    return final_edges


def non_maximum_suppression(gradient_magnitude, gradient_direction):
    # 针对每个像素，根据梯度方向选择邻域内的两个像素
    nms_image = np.zeros_like(gradient_magnitude)
    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            current_pixel = gradient_magnitude[i, j]
            angle = gradient_direction[i, j]

            # 根据梯度方向选择邻域内的两个像素
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                neighbors = [gradient_magnitude[i, j-1],
                             gradient_magnitude[i, j+1]]
            elif 22.5 <= angle < 67.5:
                neighbors = [gradient_magnitude[i-1, j+1],
                             gradient_magnitude[i+1, j-1]]
            elif 67.5 <= angle < 112.5:
                neighbors = [gradient_magnitude[i-1, j],
                             gradient_magnitude[i+1, j]]
            else:
                neighbors = [gradient_magnitude[i-1, j-1],
                             gradient_magnitude[i+1, j+1]]

            # 如果当前像素是邻域内的最大值，则保留该像素值
            if all(current_pixel >= neighbor for neighbor in neighbors):
                nms_image[i, j] = current_pixel

    return nms_image


def calculate_thresholds(image, sigma):
    # 计算高斯模糊后图像的中值，并基于中值计算双阈值
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    median = np.median(blurred)
    lower_threshold = int(max(0, (1.0 - sigma) * median))
    upper_threshold = int(min(255, (1.0 + sigma) * median))

    return lower_threshold, upper_threshold


def hysteresis_thresholding(nms_image, lower_threshold, upper_threshold):
    final_edges = np.zeros_like(nms_image)
    weak = 50
    strong = 255

    # 根据梯度幅值的阈值进行分类：强边缘和弱边缘
    strong_i, strong_j = np.where(nms_image >= upper_threshold)
    weak_i, weak_j = np.where(
        (nms_image >= lower_threshold) & (nms_image < upper_threshold))
    final_edges[strong_i, strong_j] = strong
    final_edges[weak_i, weak_j] = weak

    # 使用强边缘像素连接弱边缘像素
    for i in range(1, nms_image.shape[0] - 1):
        for j in range(1, nms_image.shape[1] - 1):
            if final_edges[i, j] == weak:
                if any(final_edges[i + di, j + dj] == strong for di in [-1, 0, 1] for dj in [-1, 0, 1]):
                    final_edges[i, j] = strong
                else:
                    final_edges[i, j] = 0

    return final_edges


if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'img1.png')
    image = imageio.imread(image_path)

    edges = canny_edge_detection(image)
    imageio.imwrite(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'Canny.png'), edges)
