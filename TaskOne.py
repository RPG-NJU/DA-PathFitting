import numpy
import matplotlib.pyplot as plt


LinearDividePoint = [0, 70, 211, 275, 382]
"""这个数据是根据展示出来的散点图进行肉眼观察得到的"""


def LinearFit(X: list, Y: list) -> (float, float):
    """
    传入两个列表，分别代表了X轴数据和Y轴数据
    使用最小二乘法进行数据的拟合
    拟合出一个直线
    返回值分别为a，b作为直线的参数
    """
    x = numpy.array(X)
    y = numpy.array(Y)
    # print(x, x.T)
    # print(x @ y.T)
    b = (x - x.mean()) @ (y - y.mean()).T / ((x - x.mean()) @ (x - x.mean()).T)
    a = y.mean() - x.mean() * b
    print("直线最小二乘法拟合结果为 a=%f b=%f" % (a, b))
    return a, b


# LinearFit([1, 3, 5], [7, 9, 11])


def Linear(X: list, Y: list):
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
    plt.title("Linear Fit")
    plt.scatter(X, Y, alpha=0.6, s=0.4)
    plt.plot(Xpoint, Ypoint, c="r")
    plt.show()


def GetIntersection(a1: float, b1: float, a2: float, b2: float) -> (float, float):
    x = (a2 - a1) / (b1 - b2)
    return x, b1 * x + a1


