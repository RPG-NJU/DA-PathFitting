def GetStationLocation(data):
    print("<PRINT station_location 基站位置信息>")
    # print(data['station_location'])   # 所有的基站的坐标信息
    '''
    格式
    基站标号 X Y Z
    我们只考虑二维平面
    '''
    # print(data["station_location"][0][0])
    station_location = list(list())
    for line in data['config']:
        line_list = list()
        line_list.append(int(line[0]))
        line_list.append(line[1])
        line_list.append(line[2])
        print(line_list)
        station_location.append(line_list)
        print(station_location)
        # line_list.clear()

    print("<PRINT station_location 基站位置信息>")
    print(station_location)
    # print(station_location[0][0])