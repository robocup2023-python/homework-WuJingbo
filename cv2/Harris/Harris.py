import cv2
import numpy as np
import os
import imageio


def harris_corner_detection(image, window_size, k, threshold):
    # 将图像转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 高斯模糊
    gray_blur = cv2.GaussianBlur(gray, (window_size, window_size), 0)

    # 计算梯度
    Ix = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
    Iy = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)

    # 计算导数的乘积
    Ixx = Ix * Ix
    Iyy = Iy * Iy
    Ixy = Ix * Iy

    # 对导数的乘积应用高斯模糊
    Ixx_blur = cv2.GaussianBlur(Ixx, (window_size, window_size), 0)
    Iyy_blur = cv2.GaussianBlur(Iyy, (window_size, window_size), 0)
    Ixy_blur = cv2.GaussianBlur(Ixy, (window_size, window_size), 0)

    # 计算Harris角点响应函数
    det_M = Ixx_blur * Iyy_blur - Ixy_blur * Ixy_blur
    trace_M = Ixx_blur + Iyy_blur
    R = det_M - k * trace_M * trace_M

    # 阈值处理
    R[R < threshold] = 0

    # 非极大值抑制
    R = cv2.dilate(R, None)
    R[R != cv2.dilate(R, None)] = 0

    # 在图像上绘制检测到的角点
    image[R > 0.01 * R.max()] = [0, 0, 255]

    return image


if __name__ == "__main__":
    image_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'img1.png')
    image = imageio.imread(image_path)

    # 进行Harris角点检测
    window_size = 3
    k = 0.04
    threshold = 10000
    result = harris_corner_detection(image, window_size, k, threshold)
    imageio.imwrite(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'Harris.png'), result)

    # 显示结果
    cv2.imshow('Harris Corner Detection', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
