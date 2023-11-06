import cv2
import numpy as np
import os
import imageio


def sobel_filter(image):
    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 定义x和y方向的Sobel算子
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # 在x和y方向上应用Sobel滤波器
    gradient_x = cv2.filter2D(gray, cv2.CV_64F, sobel_x)
    gradient_y = cv2.filter2D(gray, cv2.CV_64F, sobel_y)

    # 结合梯度幅值和方向
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    gradient_direction = np.arctan2(gradient_y, gradient_x)

    return gradient_magnitude, gradient_direction


if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'img2.jpg')
    image = cv2.imread(image_path)

    # 执行Sobel滤波
    gradient_magnitude, gradient_direction = sobel_filter(image)

    # 对梯度幅值进行归一化，以便可视化显示
    gradient_magnitude_normalized = cv2.normalize(
        gradient_magnitude, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    imageio.imwrite(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'Sobel.png'), gradient_magnitude_normalized)

    # 显示梯度幅值图像
    cv2.imshow('Gradient Magnitude', gradient_magnitude_normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
