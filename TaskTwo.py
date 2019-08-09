"""这是用于插值任务的主要函数"""
import numpy
import matplotlib.pyplot as plt
from DrawPicture import *


def GetAllUsableXY(coord: list) -> list:
    X = list()
    Y = list()
    for line in coord:
        if line[3] == 1:
            X.append(line[1])
            Y.append(line[2])

    return [X, Y]


def GetSpeed(coord: list) -> float:
    """
    :param coord: 所有的coord数据
    :return: 计算出来的速度，人每秒前进的距离
    通过这个函数，估算人前进的速度，用于之后估计插值结果是否符合要求
    """
    Time = list()
    XY = GetAllUsableXY(coord)

    for line in coord:
        if line[3] == 1:
            Time.append(line[0])

    speed_list = list()
    for i in range(0, len(XY) - 1):
        # print(XY[0][i + 1] - XY[0][i])
        s = ((XY[0][i + 1] - XY[0][i]) ** 2 + (XY[1][i + 1] - XY[1][i]) ** 2) ** (1/2)
        t = Time[i + 1] - Time[i]
        v = s / t
        speed_list.append(v)

    return numpy.mean(speed_list)


def LinearInter(coord: list, mode=0) -> list:
    """
    :param coord:
    :param mode: 插值的模式
    :return: 返回插值的数据
    """
    X = list()
    Y = list()
    if mode == 0:
        """此时是最简单的内插完成"""
        x1 = coord[0][1]
        y1 = coord[0][2]
        t1 = coord[0][0]
        x2 = coord[-1][1]
        y2 = coord[-1][2]
        t2 = coord[-1][0]
    else:
        x1 = coord[0][1]
        y1 = coord[0][2]
        t1 = coord[0][0]
        x2 = coord[-1][1]
        y2 = coord[-1][2]
        t2 = coord[-1][0]

    for i in range(1, len(coord) - 1):
        t = coord[i][0]
        x = x1 + ((t - t1) / (t2 - t1)) * (x2 - x1)
        y = y1 + ((t - t1) / (t2 - t1)) * (y2 - y1)
        X.append(x)
        Y.append(y)

    return [X, Y]


def Linear(coord: list):
    """
    :param coord:
    :return:
    """
    X = list()
    Y = list()

    for i in range(0, len(coord) - 1):
        if coord[i + 1][3] == 1 or coord[i][3] == 0:
            continue

        for j in range(i + 1, len(coord)):
            if coord[j][3] == 1:
                XY = LinearInter(coord[i: j + 1])
                X += XY[0]
                Y += (XY[1])
                # i = j
                break

    # 此时应该开始绘图
    XY = GetAllUsableXY(coord)
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(XY[0], XY[1], alpha=0.6, s=0.4)
    plt.scatter(X, Y, alpha=0.6, s=0.4, c="r")
    plt.title("Linear Inter Data")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""
    plt.show()


# def test(coord: list):
#     """
#     :param coord: coord原始格式数据
#     :return:
#     """
#     XY = GetAllUsableXY(coord)
#     # print(GetAllUsableXY(coord))
#     GetScatterPlot(XY[0], XY[1])
#     speed = GetSpeed(coord)
#     print(speed)
#     Linear(coord)


def ShowRawData(coord: list):
    """
    :param coord:
    :return:
    绘制原始数据的图表
    """
    XY = GetAllUsableXY(coord)
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(XY[0], XY[1], alpha=0.6, s=0.8, c="b")
    plt.title("Coord Raw Data")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""

    plt.show()
