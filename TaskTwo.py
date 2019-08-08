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


def test(coord: list):
    """
    :param coord: coord原始格式数据
    :return:
    """
    XY = GetAllUsableXY(coord)
    # print(GetAllUsableXY(coord))
    GetScatterPlot(XY[0], XY[1])
    speed = GetSpeed(coord)
    print(speed)