import scipy.io as scio


def LoadData():
    dataFile = "./data/homework.mat"
    data = scio.loadmat(dataFile)

    # print(type(data))   # 数据存储格式为dict字典格式
    # print(data)

    return data



