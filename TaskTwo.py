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


def test(coord: list):
    """
    :param coord: coord原始格式数据
    :return:
    """
    XY = GetAllUsableXY(coord)
    # print(GetAllUsableXY(coord))
    GetScatterPlot(XY[0], XY[1])