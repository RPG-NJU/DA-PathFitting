"""这个文件使用库函数进行拟合的结果"""

from scipy import optimize
from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np

# 调用numpy.ployfit()进行数据拟合


# 直线方程函数
def f_1(x, A, B):
    return A * x + B


# 二次曲线方程
def f_2(x, A, B, C):
    return A * x * x + B * x + C


# 三次曲线方程
def f_3(x, A, B, C, D):
    return A * x * x * x + B * x * x + C * x + D


def standardFix(x: list, y: list):
    # plt.figure()
    #
    # # 拟合点
    # # x0 = [1, 2, 3, 4, 5]
    # # y0 = [1, 3, 8, 18, 36]
    #
    # # 绘制散点
    # plt.scatter(x0[:], y0[:], 2, "red")
    #
    # # 直线拟合与绘制
    # A1, B1 = optimize.curve_fit(f_1, x0, y0)[0]
    # x1 = np.arange(-500, 600, 0.01)
    # y1 = A1 * x1 + B1
    # plt.plot(x1, y1, "blue")
    #
    # # 二次曲线拟合与绘制
    # A2, B2, C2 = optimize.curve_fit(f_2, x0, y0)[0]
    # x2 = np.arange(-500, 600, 0.01)
    # y2 = A2 * x2 * x2 + B2 * x2 + C2
    # plt.plot(x2, y2, "green")
    #
    # # 三次曲线拟合与绘制
    # A3, B3, C3, D3 = optimize.curve_fit(f_3, x0, y0)[0]
    # x3 = np.arange(-500, 600, 0.01)
    # y3 = A3 * x3 * x3 * x3 + B3 * x3 * x3 + C3 * x3 + D3
    # plt.plot(x3, y3, "purple")
    #
    # plt.title("test")
    # plt.xlabel('x')
    # plt.ylabel('y')
    #
    # plt.show()
    xx = np.array(x)
    yy = np.array(y)
    xx = np.r_[xx, xx[0]]
    yy = np.r_[yy, yy[0]]
    tck, u = interpolate.splprep([xx, yy], s=0, per=True)

    # evaluate the spline fits for 1000 evenly spaced distance values
    xi, yi = interpolate.splev(np.linspace(0, 1, 1000), tck)

    # plot the result
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, 'or')
    ax.plot(xi, yi, '-b')
