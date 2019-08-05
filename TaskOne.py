import numpy


DividePoint = [0, 70, 210, 274, 382]


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


LinearFit([1, 3, 5], [7, 9, 11])
