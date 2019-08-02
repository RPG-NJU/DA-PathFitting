from ReadFile import *
from FixData import *
from DrawPicture import *
import StandardFix


def main():
    data = LoadData()
    station_location = GetStationLocation(data)
    """通过Get函数得到了所有站点的位置信息，存储在了station_location中"""
    """存储的形式是list的list，每个list子元素中的分布为：编号 X Y"""
    path_chan = GetPathChan(data)
    XY_list = GetXYList(path_chan)
    GetScatterPlot(XY_list[0], XY_list[1])
    StandardFix.standardFix(XY_list[0], XY_list[1])
    # StandardFix.standardFix()


main()
