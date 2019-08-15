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


def GetAllUsableXYandTime(coord: list) -> list:
    X = list()
    Y = list()
    T = list()
    for line in coord:
        if line[3] == 1:
            X.append(line[1])
            Y.append(line[2])
            T.append(line[0])

    return [X, Y, T]


def GetSpeed(coord: list) -> dict:
    """
    :param coord: 所有的coord数据
    :return: 计算出来的速度，人每秒前进的距离等数据，参照dict说明
    通过这个函数，估算人前进的速度，用于之后估计插值结果是否符合要求
    进行后续的Fix修正
    """
    Time = list()
    XY = GetAllUsableXY(coord)

    for line in coord:
        if line[3] == 1:
            Time.append(line[0])

    all_s = 0.0
    all_t = 0.0

    speed_list = list()
    for i in range(0, len(XY[0]) - 1):
        # print(XY[0][i + 1] - XY[0][i])
        s = ((XY[0][i + 1] - XY[0][i]) ** 2 + (XY[1][i + 1] - XY[1][i]) ** 2) ** (1/2)
        # print(s)
        all_s += s
        t = Time[i + 1] - Time[i]
        all_t += t
        # print(s, t)
        v = s / t
        speed_list.append(v)
    # print(speed_list)

    # average_speed = numpy.mean(speed_list)
    average_speed = all_s/all_t
    res = {
        "average": average_speed,
        "max": max(speed_list)
    }
    # print(res)
    return res


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


def GetDelta(data: list) -> list:
    """
    :param data: 需要计算的数据列表
    :return: 返回delta计算结果
    """
    res = list()
    for i in range(0, len(data) - 1):
        res.append(data[i + 1] - data[i])

    return res


def CubicSplineInter(coord: list) -> list:
    """
    :param coord:
    :param begin: 插值的起点
    :param end: 插值的终点 迭代器方式
    :return:
    """
    XY = GetAllUsableXY(coord)
    delta_x = GetDelta(XY[0])
    delta_y = GetDelta(XY[1])
    # print(XY)
    L = list()
    for i in range(0, len(XY[0])):
        l = [0] * len(XY[0])
        # print(l)
        if i == 0:
            l[0] = 1
        elif i == len(XY[0]) - 1:
            l[len(XY[0]) - 1] = 1
        else:   # 此时是最一般的情况
            l[i - 1] = delta_x[i - 1]
            l[i] = 2 * (delta_x[i - 1] + delta_x[i])
            l[i + 1] = delta_x[i]
        L.append(l)
    LM = numpy.mat(L)
    # print(LM)

    R = list()
    for i in range(0, len(XY[0])):
        if i == 0 or i == len(XY[0]) - 1:
            R.append(0)
        else:
            R.append(3 * (delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1]))
    RM = numpy.mat(R).T
    # print(LM)

    CM = LM.I * RM
    # print(CM)
    C = CM.T.tolist()[0]
    # print(C)
    # print(C)
    D = list()
    B = list()
    A = [1] * len(C)
    for i in range(0, len(C) - 1):
        D.append((C[i + 1] - C[i]) / (3 * delta_x[i]))
        B.append(delta_y[i] / delta_x[i] - (delta_x[i] / 3) * (2 * C[i] + C[i + 1]))

    B.append(0)
    D.append(0)
    # print(A, "\n", B, "\n", C, "\n", D)
    # print(len(A), len(B), len(C), len(D))

    interX = list()
    interY = list()

    XYT = GetAllUsableXYandTime(coord)
    # print(XYT)
    for point in coord:
        if point[3] == 0:
            i = 0
            while i < len(XYT[0]) - 1:
                # print(point[0], XYT[2][i])
                if XYT[2][i + 1] > point[0] > XYT[2][i]:
                    t1 = XYT[2][i]
                    t2 = XYT[2][i + 1]
                    x1 = XYT[0][i]
                    x2 = XYT[0][i + 1]
                    t = point[0]
                    # x = t * (x1 + x2) / (t1 + t2)
                    # print(x1, x2)
                    # print(t1, t2, t)
                    x = x1 + (x2 - x1) * (t - t1) / (t2 - t1)
                    y1 = XYT[1][i]
                    y = A[i] * y1 + B[i] * (x - x1) + C[i] * (x - x1) ** 2 + D[i] * (x - x1) ** 3
                    interX.append(x)
                    interY.append(y)
                    break
                else:
                    i += 1
        else:
            continue

    interXY = [interX, interY]
    # print(interXY)
    return interXY


def CubicSpline(coord: list, range=1):
    """
    :param coord:
    :return:
    三次样条插值的主函数
    """
    # 这里考虑进行全局的三次样条拟合
    XY = GetAllUsableXY(coord)
    # print(XY)
    interXY = CubicSplineInter(coord)
    print("三次样条 总计插值点", len(interXY[0]))

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(XY[0], XY[1], alpha=0.6, s=0.5, c="b")
    plt.scatter(interXY[0], interXY[1], alpha=0.6, s=0.5, c="r")
    plt.title("CubicSpline Inter Data")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""

    plt.show()


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


def CubicSplineInterWithFix1(coord: list, speed: dict) -> (list, list):
    """
    :param coord:
    :param begin: 插值的起点
    :param end: 插值的终点 迭代器方式
    :return:
    """
    XY = GetAllUsableXY(coord)
    delta_x = GetDelta(XY[0])
    delta_y = GetDelta(XY[1])
    # print(XY)
    L = list()
    for i in range(0, len(XY[0])):
        l = [0] * len(XY[0])
        # print(l)
        if i == 0:
            l[0] = 1
        elif i == len(XY[0]) - 1:
            l[len(XY[0]) - 1] = 1
        else:   # 此时是最一般的情况
            l[i - 1] = delta_x[i - 1]
            l[i] = 2 * (delta_x[i - 1] + delta_x[i])
            l[i + 1] = delta_x[i]
        L.append(l)
    LM = numpy.mat(L)
    # print(LM)

    R = list()
    for i in range(0, len(XY[0])):
        if i == 0 or i == len(XY[0]) - 1:
            R.append(0)
        else:
            R.append(3 * (delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1]))
    RM = numpy.mat(R).T
    # print(LM)

    CM = LM.I * RM
    # print(CM)
    C = CM.T.tolist()[0]
    # print(C)
    # print(C)
    D = list()
    B = list()
    A = [1] * len(C)
    for i in range(0, len(C) - 1):
        D.append((C[i + 1] - C[i]) / (3 * delta_x[i]))
        B.append(delta_y[i] / delta_x[i] - (delta_x[i] / 3) * (2 * C[i] + C[i + 1]))

    B.append(0)
    D.append(0)
    # print(A, "\n", B, "\n", C, "\n", D)
    # print(len(A), len(B), len(C), len(D))

    interX = list()
    interY = list()
    errorX = list()
    errorY = list()

    XYT = GetAllUsableXYandTime(coord)
    # print(XYT)
    for point in coord:
        if point[3] == 0:
            i = 0
            while i < len(XYT[0]) - 1:
                # print(point[0], XYT[2][i])
                if XYT[2][i + 1] > point[0] > XYT[2][i]:
                    t1 = XYT[2][i]
                    t2 = XYT[2][i + 1]
                    x1 = XYT[0][i]
                    x2 = XYT[0][i + 1]
                    t = point[0]
                    # x = t * (x1 + x2) / (t1 + t2)
                    # print(x1, x2)
                    # print(t1, t2, t)
                    x = x1 + (x2 - x1) * (t - t1) / (t2 - t1)
                    y1 = XYT[1][i]
                    y2 = XYT[1][i + 1]
                    y = A[i] * y1 + B[i] * (x - x1) + C[i] * (x - x1) ** 2 + D[i] * (x - x1) ** 3
                    if abs((((x - x1) ** 2 + (y - y1) ** 2) ** 1 / 2) / (t - t1)) < speed["max"]\
                            and abs((((x - x2) ** 2 + (y - y2) ** 2) ** 1 / 2) / (t - t2)) < speed["max"]:
                        interX.append(x)
                        interY.append(y)
                    else:
                        errorX.append(x)
                        errorY.append(y)
                    break
                else:
                    i += 1
        else:
            continue

    interXY = [interX, interY]
    errorXY = [errorX, errorY]
    # print(interXY)
    return interXY, errorXY


def CubicSplineWithFix1(coord: list, range=1):
    """
    :param coord:
    :return:
    三次样条插值的主函数
    """
    # 这里考虑进行全局的三次样条拟合
    XY = GetAllUsableXY(coord)
    speed = GetSpeed(coord)
    print("speed dict =", speed)
    # print(XY)
    interXY, errorXY = CubicSplineInterWithFix1(coord, speed)
    print("三次样条 修正1 总计插值点", len(interXY[0]))
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(XY[0], XY[1], alpha=0.6, s=0.5, c="b")
    plt.scatter(interXY[0], interXY[1], alpha=0.6, s=0.5, c="g")
    plt.scatter(errorXY[0], errorXY[1], alpha=0.6, s=4.0, marker="x", c="r")
    plt.title("CubicSpline Inter Data with Fix1")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""

    plt.show()


def CubicSplineInterWithFix2(coord: list) -> (list, list):
    """
    :param coord:
    :param begin: 插值的起点
    :param end: 插值的终点 迭代器方式
    :return:
    """
    XY = GetAllUsableXY(coord)
    delta_x = GetDelta(XY[0])
    delta_y = GetDelta(XY[1])
    # print(XY)
    L = list()
    for i in range(0, len(XY[0])):
        l = [0] * len(XY[0])
        # print(l)
        if i == 0:
            l[0] = 1
        elif i == len(XY[0]) - 1:
            l[len(XY[0]) - 1] = 1
        else:   # 此时是最一般的情况
            l[i - 1] = delta_x[i - 1]
            l[i] = 2 * (delta_x[i - 1] + delta_x[i])
            l[i + 1] = delta_x[i]
        L.append(l)
    LM = numpy.mat(L)
    # print(LM)

    R = list()
    for i in range(0, len(XY[0])):
        if i == 0 or i == len(XY[0]) - 1:
            R.append(0)
        else:
            R.append(3 * (delta_y[i] / delta_x[i] - delta_y[i - 1] / delta_x[i - 1]))
    RM = numpy.mat(R).T
    # print(LM)

    CM = LM.I * RM
    # print(CM)
    C = CM.T.tolist()[0]
    # print(C)
    # print(C)
    D = list()
    B = list()
    A = [1] * len(C)
    for i in range(0, len(C) - 1):
        D.append((C[i + 1] - C[i]) / (3 * delta_x[i]))
        B.append(delta_y[i] / delta_x[i] - (delta_x[i] / 3) * (2 * C[i] + C[i + 1]))

    B.append(0)
    D.append(0)
    # print(A, "\n", B, "\n", C, "\n", D)
    # print(len(A), len(B), len(C), len(D))

    interX = list()
    interY = list()
    errorX = list()
    errorY = list()

    XYT = GetAllUsableXYandTime(coord)
    # print(XYT)
    for point in coord:
        if point[3] == 0:
            i = 0
            while i < len(XYT[0]) - 1:
                # print(point[0], XYT[2][i])
                if XYT[2][i + 1] > point[0] > XYT[2][i]:
                    t1 = XYT[2][i]
                    t2 = XYT[2][i + 1]
                    x1 = XYT[0][i]
                    x2 = XYT[0][i + 1]
                    t = point[0]
                    x = x1 + (x2 - x1) * (t - t1) / (t2 - t1)
                    y1 = XYT[1][i]
                    y2 = XYT[1][i + 1]
                    y = A[i] * y1 + B[i] * (x - x1) + C[i] * (x - x1) ** 2 + D[i] * (x - x1) ** 3
                    v = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)) / (t2 - t1)
                    v_max = 2.0 * v
                    v_min = 0.5 * v

                    if v_min < abs((((x - x1) ** 2 + (y - y1) ** 2) ** (1 / 2)) / (t - t1)) < v_max\
                            and v_min < abs((((x - x2) ** 2 + (y - y2) ** 2) ** (1 / 2)) / (t - t2)) < v_max:
                        interX.append(x)
                        interY.append(y)
                    else:
                        errorX.append(x)
                        errorY.append(y)
                    break
                else:
                    i += 1
        else:
            continue

    interXY = [interX, interY]
    errorXY = [errorX, errorY]
    # print(interXY)
    return interXY, errorXY


def CubicSplineWithFix2(coord: list, range=1):
    """
    :param coord:
    :return:
    三次样条插值的主函数
    """
    # 这里考虑进行全局的三次样条拟合
    XY = GetAllUsableXY(coord)
    speed = GetSpeed(coord)
    print("speed dict =", speed)
    # print(XY)
    interXY, errorXY = CubicSplineInterWithFix2(coord)
    print("三次样条 修正2 总计插值点", len(interXY[0]))
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(XY[0], XY[1], alpha=0.6, s=0.5, c="b")
    plt.scatter(interXY[0], interXY[1], alpha=0.6, s=0.5, c="g")
    plt.scatter(errorXY[0], errorXY[1], alpha=0.6, s=4.0, marker="x", c="r")
    plt.title("CubicSpline Inter Data with Fix2")
    """x y为点的坐标序列 alpha为颜色的深浅 s为点的大小"""

    plt.show()