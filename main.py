from ReadFile import *
from FixData import *
from DrawPicture import *
import StandardFix
import TaskOne
import TaskTwo


def main():
    data = LoadData()
    station_location = GetStationLocation(data)
    """通过Get函数得到了所有站点的位置信息，存储在了station_location中"""
    """存储的形式是list的list，每个list子元素中的分布为：编号 X Y"""
    path_chan = GetPathChan(data)
    XY_list = GetXYList(path_chan)
    # GetScatterPlot(XY_list[0], XY_list[1], 1)
    # TaskOne.LinearWithoutFix(XY_list[0], XY_list[1])
    # TaskOne.Linear(XY_list[0], XY_list[1])  # 这是进行线性拟合的函数
    # TaskOne.LinearAndQuadratic(XY_list[0], XY_list[1])

    coord = GetCoord(data)
    # TaskTwo.ShowRawData(coord)
    # TaskTwo.test(coord)
    # TaskTwo.Linear(coord)
    # TaskTwo.CubicSpline(coord)
    # TaskTwo.CubicSplineWithFix1(coord)
    TaskTwo.CubicSplineWithFix2(coord)


main()
