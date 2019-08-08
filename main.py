from ReadFile import *
from FixData import *
from DrawPicture import *
import StandardFix
from TaskOne import *
from TaskTwo import *


def main():
    data = LoadData()
    station_location = GetStationLocation(data)
    """通过Get函数得到了所有站点的位置信息，存储在了station_location中"""
    """存储的形式是list的list，每个list子元素中的分布为：编号 X Y"""
    path_chan = GetPathChan(data)
    XY_list = GetXYList(path_chan)
    # GetScatterPlot(XY_list[0], XY_list[1])
    # StandardFix.standardFix(XY_list[0], XY_list[1])
    """这里通过库函数来进行拟合，但是拟合的结果并不是非常符合题意，之后也许会进行优化
       2019.8.2
    """
    # StandardFix.standardFix()
    # Linear(XY_list[0], XY_list[1])  # 这是进行线性拟合的函数
    # LinearAndQuadratic(XY_list[0], XY_list[1])

    coord = GetCoord(data)
    print(coord)
    test(coord)


main()
