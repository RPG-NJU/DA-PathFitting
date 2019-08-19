import numpy
import matplotlib.pyplot as plt





def LinearFit(X: list, Y: list) -> (float, float):
    """
    传入两个列表，分别代表了X轴数据和Y轴数据
    使用最小二乘法进行数据的拟合
    拟合出一个直线
    返回值分别为a，b作为直线的参数
    @:return y = bx + a，返回a和b
    """
    x = numpy.array(X)
    y = numpy.array(Y)
    b = (x - x.mean()) @ (y - y.mean()).T / ((x - x.mean()) @ (x - x.mean()).T)
    a = y.mean() - x.mean() * b
    print("直线最小二乘法拟合结果为 y=%fx+%f" % (b, a))
    return a, b


def Linear(X: list, Y: list):
    LinearDividePoint = [0, 70, 211, 275, 382]
    """这个数据是根据展示出来的散点图进行肉眼观察得到的"""
    A = list()
    B = list()
    """用于存储四条直线的a和b"""
    i = 0
    while i < 4:
        if i % 2 == 1:
            a, b = LinearFit(X[LinearDividePoint[i]: LinearDividePoint[i+1]], Y[LinearDividePoint[i]: LinearDividePoint[i+1]])
        else:
            a, b = LinearFit(Y[LinearDividePoint[i]: LinearDividePoint[i + 1]],
                             X[LinearDividePoint[i]: LinearDividePoint[i + 1]])
            b = 1.0 / b

            a = -a * b
        A.append(a)
        B.append(b)
        i += 1
    # 使用这种通用的方法发现会出现较大的误差，绘图之后是一个梯形
    # 后来fix了这个误差 2019.8.6

    # 得到了斜率和截距的数据之后，需要计算出交点
    Xpoint = list()
    Ypoint = list()
    A += A[0: 1]
    B += B[0: 1]
    # print(A, B)
    for i in range(0, 4):
        x, y = GetIntersection(A[i], B[i], A[i + 1], B[i + 1])
        print("测试输出", x, y)
        Xpoint.append(x)
        Ypoint.append(y)

    Xpoint += Xpoint[0: 1]
    Ypoint += Ypoint[0: 1]
    print(Xpoint, Ypoint)

    plt.clf()
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.title("Linear Fit")
    plt.scatter(X, Y, alpha=0.4, s=4)
    plt.plot(Xpoint, Ypoint, c="r")
    plt.show()


def LinearWithoutFix(X: list, Y: list):
    LinearDividePoint = [0, 70, 211, 275, 382]
    """这个数据是根据展示出来的散点图进行肉眼观察得到的"""
    A = list()
    B = list()
    """用于存储四条直线的a和b"""
    i = 0
    while i < 4:
        a, b = LinearFit(X[LinearDividePoint[i]: LinearDividePoint[i+1]], Y[LinearDividePoint[i]: LinearDividePoint[i+1]])
        A.append(a)
        B.append(b)
        i += 1
    # 使用这种通用的方法发现会出现较大的误差，绘图之后是一个梯形
    # 后来fix了这个误差 2019.8.6

    # 得到了斜率和截距的数据之后，需要计算出交点
    Xpoint = list()
    Ypoint = list()
    A += A[0: 1]
    B += B[0: 1]
    # print(A, B)
    for i in range(0, 4):
        x, y = GetIntersection(A[i], B[i], A[i + 1], B[i + 1])
        print("测试输出", x, y)
        Xpoint.append(x)
        Ypoint.append(y)

    Xpoint += Xpoint[0: 1]
    Ypoint += Ypoint[0: 1]
    print(Xpoint, Ypoint)

    plt.clf()
    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.title("Linear Fit without Fix")
    plt.scatter(X, Y, alpha=0.4, s=4)
    plt.plot(Xpoint, Ypoint, c="r")
    plt.show()


def GetIntersection(a1: float, b1: float, a2: float, b2: float) -> (float, float):
    x = (a2 - a1) / (b1 - b2)
    return x, b1 * x + a1


# 前面是线性拟合的构造
# 下面是线性拟合和二次拟合的复合拟合方式


def LinearAndQuadratic(X: list, Y: list):
    """
    线性拟合与二次拟合的复合拟合方式
    手动选择需要二次拟合的部分，进行拟合之后拼接
    可以使用最小二乘法进行拟合
    """
    LinearDivide = [
        [0, 67],
        [84, 211],
        [211, 269],
        [269, 382],
    ]
    QuadraticDivide = [
        [67, 84],
        [269, 296]
    ]
    LinearDrawDivide = [
        [-423, -403],
        [-380, 450],
        [350, 450],
        [-400, 400]
    ]

    a_list = list() # 存储了系数的列表
    for pair in QuadraticDivide:
        # print(pair)
        a = MultipleFit(X[pair[0]: pair[1]], Y[pair[0]: pair[1]], 2)
        a_list.append(a)

    plt.clf()
    plt.title("Linear And Quadratic")

    i = 0
    for a in a_list:
        # x = numpy.array(X[QuadraticDivide[i][0]: QuadraticDivide[i][1]])
        if X[QuadraticDivide[i][0]] < X[QuadraticDivide[i][1]]:
            x = numpy.arange(X[QuadraticDivide[i][0]], X[QuadraticDivide[i][1]], 0.1)
        else:
            x = numpy.arange(X[QuadraticDivide[i][1]], X[QuadraticDivide[i][0]], 0.1)
        y = a[0] * x ** 2 + a[1] * x + a[2]
        y = y.T
        plt.plot(x, y, c="r")
        i += 1
    # 上面完成了二次拟合的部分，下面需要补充线性拟合部分
    A = list()
    B = list()
    """用于存储四条直线的a和b"""
    i = 0
    while i < 4:
        if i % 2 == 1:  # 为了减少在垂直方向的误差所设计的
            a, b = LinearFit(X[LinearDivide[i][0]: LinearDivide[i][1]],
                             Y[LinearDivide[i][0]: LinearDivide[i][1]])
        else:
            a, b = LinearFit(Y[LinearDivide[i][0]: LinearDivide[i][1]],
                             X[LinearDivide[i][0]: LinearDivide[i][1]])
            b = 1.0 / b
            a = -a * b
            
        A.append(a)
        B.append(b)
        i += 1

    LinearDivide[3][1] = 381
    for i in range(0, 4):
        x = numpy.arange(LinearDrawDivide[i][0], LinearDrawDivide[i][1], 0.1)
        y = B[i] * x + A[i]
        y = y.T
        plt.plot(x, y, c="r")

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.show()


def MultipleFit(X: list, Y: list, n: int) -> list:
    """
    :param X: 需要拟合的所有点的X坐标list
    :param Y: Y坐标list
    :param n: 拟合的最高次数
    :return: 返回值为从最高次数项开始的系数list
    本函数采用最小二乘法进行拟合
    """
    XA = list()
    i = n
    while i >= 0:
        x = [x_ ** i for x_ in X]
        # print(x)
        XA.append(x)
        i -= 1
    A = numpy.mat(XA)
    A = A.T
    # 通过上面的代码准备完成了一个矩阵
    b = numpy.mat(Y)
    b = b.T
    # 再次准备了一个矩阵，b

    a = A.I * A.T.I * A.T * b
    print("%d次拟合系数为:" % n, a.T)
    # print(a.T)
    return a


def CubicWithoutFix(X: list, Y: list):
    """
    :param X: X坐标
    :param Y: Y坐标
    :return: void
    通过最小二乘法进行三次函数的拟合实验
    """
    DividePoint = [0, 70, 211, 275, 382]    # 从前序实验中直接移植来的分割点

    plt.clf()
    plt.title("Cubic Fit without Fix")
    for i in range(0, 4):
        a = MultipleFit(X[DividePoint[i]: DividePoint[i + 1]], Y[DividePoint[i]: DividePoint[i + 1]], 3)
        if DividePoint[i + 1] >= 382:
            DividePoint[i + 1] -= 1
        if X[DividePoint[i]] < X[DividePoint[i + 1]]:
            x = numpy.arange(X[DividePoint[i]], X[DividePoint[i + 1]], 0.1)
        else:
            x = numpy.arange(X[DividePoint[i + 1]], X[DividePoint[i]], 0.1)
        y = a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x + a[3]
        y = y.T
        print(y)
        plt.plot(x, y, c="r")

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.show()


def CubicWithFix(X: list, Y: list):
    """
    :param X: X坐标
    :param Y: Y坐标
    :return: void
    通过最小二乘法进行三次函数的拟合实验
    """
    DividePoint = [0, 70, 211, 275, 382]    # 从前序实验中直接移植来的分割点

    plt.clf()
    plt.title("Cubic Fit with Fix")
    for i in range(0, 4):
        if i % 2 == 0:
            a = MultipleFit(Y[DividePoint[i]: DividePoint[i + 1]], X[DividePoint[i]: DividePoint[i + 1]], 3)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if Y[DividePoint[i]] < Y[DividePoint[i + 1]]:
                x = numpy.arange(Y[DividePoint[i]], Y[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(Y[DividePoint[i + 1]], Y[DividePoint[i]], 0.1)
            y = a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x + a[3]
            y = y.T
            # print(y)
            plt.plot(y, x, c="r")
        else:
            a = MultipleFit(X[DividePoint[i]: DividePoint[i + 1]], Y[DividePoint[i]: DividePoint[i + 1]], 3)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if X[DividePoint[i]] < X[DividePoint[i + 1]]:
                x = numpy.arange(X[DividePoint[i]], X[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(X[DividePoint[i + 1]], X[DividePoint[i]], 0.1)
            y = a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x + a[3]
            y = y.T
            # print(y)
            plt.plot(x, y, c="r")

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.show()


def Quadratic(X: list, Y: list):
    """
    :param X: X坐标
    :param Y: Y坐标
    :return: void
    通过最小二乘法进行三次函数的拟合实验
    """
    DividePoint = [0, 70, 211, 275, 382]    # 从前序实验中直接移植来的分割点

    plt.clf()
    plt.title("Quadratic Fit")
    for i in range(0, 4):
        if i % 2 == 0:
            a = MultipleFit(Y[DividePoint[i]: DividePoint[i + 1]], X[DividePoint[i]: DividePoint[i + 1]], 4)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if Y[DividePoint[i]] < Y[DividePoint[i + 1]]:
                x = numpy.arange(Y[DividePoint[i]], Y[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(Y[DividePoint[i + 1]], Y[DividePoint[i]], 0.1)
            y = a[0] * x ** 4 + a[1] * x ** 3 + a[2] * x ** 2 + a[3] * x + a[4]
            y = y.T
            # print(y)
            plt.plot(y, x, c="r")
        else:
            a = MultipleFit(X[DividePoint[i]: DividePoint[i + 1]], Y[DividePoint[i]: DividePoint[i + 1]], 4)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if X[DividePoint[i]] < X[DividePoint[i + 1]]:
                x = numpy.arange(X[DividePoint[i]], X[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(X[DividePoint[i + 1]], X[DividePoint[i]], 0.1)
            y = a[0] * x ** 4 + a[1] * x ** 3 + a[2] * x ** 2 + a[3] * x + a[4]
            y = y.T
            # print(y)
            plt.plot(x, y, c="r")

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.show()


# def nF()


def nFit(X: list, Y: list, n: int):
    """
    :param X: X坐标
    :param Y: Y坐标
    :return: void
    通过最小二乘法进行三次函数的拟合实验
    """
    DividePoint = [0, 70, 211, 275, 382]    # 从前序实验中直接移植来的分割点

    plt.clf()
    plt.title(str(n) + " Fit")
    for i in range(0, 4):
        if i % 2 == 0:
            a = MultipleFit(Y[DividePoint[i]: DividePoint[i + 1]], X[DividePoint[i]: DividePoint[i + 1]], n)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if Y[DividePoint[i]] < Y[DividePoint[i + 1]]:
                x = numpy.arange(Y[DividePoint[i]], Y[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(Y[DividePoint[i + 1]], Y[DividePoint[i]], 0.1)
            # y = a[0] * x ** 4 + a[1] * x ** 3 + a[2] * x ** 2 + a[3] * x + a[4]
            y = x * 0
            y = numpy.mat(y)
            y = y.T
            for k in range(0, n + 1):
                # print(y)
                # print(x ** (n - i))
                y += numpy.mat(a[k] * x ** (n - k)).T
            y = y.T
            y = numpy.matrix.tolist(y)
            y = list(y)[0]

            print(y)
            plt.plot(y, x, c="r")
        else:
            a = MultipleFit(X[DividePoint[i]: DividePoint[i + 1]], Y[DividePoint[i]: DividePoint[i + 1]], n)
            if DividePoint[i + 1] >= 382:
                DividePoint[i + 1] -= 1
            if X[DividePoint[i]] < X[DividePoint[i + 1]]:
                x = numpy.arange(X[DividePoint[i]], X[DividePoint[i + 1]], 0.1)
            else:
                x = numpy.arange(X[DividePoint[i + 1]], X[DividePoint[i]], 0.1)
            y = x * 0
            y = numpy.mat(y)
            y = y.T
            for k in range(0, n + 1):
                # print(y)
                # print(x ** (n - i))
                y += numpy.mat(a[k] * x ** (n - k)).T
            y = y.T
            y = numpy.matrix.tolist(y)
            y = list(y)[0]
            plt.plot(x, y, c="r")

    plt.axis('equal')  # 保证XY轴的单位长度是一致的
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.show()