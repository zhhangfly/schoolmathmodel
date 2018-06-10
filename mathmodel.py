import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from scipy.misc import imread

def dataAnalysis():

    #以下为选课结果的数目统计
    numcourse = np.zeros(19)
    dividedonecourse=np.zeros(6)#顺序为物理,化学,生物,政治,历史,地理
    dividedtwocourse=np.zeros(15)#顺序为物化0、物生1、物政2、物史3、物地4、化生5、化政6、化史7、化地8、生政9、生史10、生地11、政史12、政地13、史地14

    rawdata = pd.read_excel('C:/Users/张博/Desktop/A.xls',sheet_name='选课具体信息')
    ele = '选课情况'

    data  = rawdata[ele]#此处得到的为series数据类型，内容为长度为252的向量
    for course in data:#course为string类型的课程名
        if course == '物理化学生物':
            numcourse[0]+=1
            dividedonecourse[0]+=1
            dividedonecourse[1]+=1
            dividedonecourse[2]+=1

            dividedtwocourse[0]+=1
            dividedtwocourse[1]+=1
            dividedtwocourse[5]+=1
        if course == '物理化学历史':
            numcourse[1]+=1
            dividedonecourse[0] += 1
            dividedonecourse[1] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[0] += 1
            dividedtwocourse[3] += 1
            dividedtwocourse[7] += 1
        if course == '物理化学地理':
            numcourse[2] += 1
            dividedonecourse[0] += 1
            dividedonecourse[1] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[0] += 1
            dividedtwocourse[4] += 1
            dividedtwocourse[8] += 1
        if course == '物理生物政治':
            numcourse[3] += 1
            dividedonecourse[0] += 1
            dividedonecourse[2] += 1
            dividedonecourse[3] += 1

            dividedtwocourse[1] += 1
            dividedtwocourse[2] += 1
            dividedtwocourse[9] += 1
        if course == '物理生物历史':
            numcourse[4] += 1
            dividedonecourse[0] += 1
            dividedonecourse[2] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[1] += 1
            dividedtwocourse[3] += 1
            dividedtwocourse[10] += 1
        if course == '物理生物地理': 
            numcourse[5] += 1
            dividedonecourse[0] += 1
            dividedonecourse[2] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[1] += 1
            dividedtwocourse[4] += 1
            dividedtwocourse[11] += 1
        if course == '物理政治历史':
            numcourse[6] += 1
            dividedonecourse[0] += 1
            dividedonecourse[3] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[2] += 1
            dividedtwocourse[3] += 1
            dividedtwocourse[12] += 1
        if course == '物理政治地理':
            numcourse[7] += 1
            dividedonecourse[0] += 1
            dividedonecourse[3] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[2] += 1
            dividedtwocourse[4] += 1
            dividedtwocourse[13] += 1
        if course == '物理历史地理':
            numcourse[8] += 1
            dividedonecourse[0] += 1
            dividedonecourse[4] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[3] += 1
            dividedtwocourse[4] += 1
            dividedtwocourse[14] += 1
        if course == '化学生物政治':
            numcourse[9]+=1
            dividedonecourse[1] += 1
            dividedonecourse[2] += 1
            dividedonecourse[3] += 1

            dividedtwocourse[5] += 1
            dividedtwocourse[6] += 1
            dividedtwocourse[9] += 1
        if course == '化学生物历史':
            numcourse[10] += 1
            dividedonecourse[1] += 1
            dividedonecourse[2] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[5] += 1
            dividedtwocourse[7] += 1
            dividedtwocourse[10] += 1
        if course == '化学生物地理':
            numcourse[11] += 1
            dividedonecourse[1] += 1
            dividedonecourse[2] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[5] += 1
            dividedtwocourse[8] += 1
            dividedtwocourse[11] += 1
        if course == '化学政治历史':
            numcourse[12] += 1
            dividedonecourse[1] += 1
            dividedonecourse[3] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[6] += 1
            dividedtwocourse[7] += 1
            dividedtwocourse[12] += 1
        if course == '化学政治地理':
            numcourse[13] += 1
            dividedonecourse[1] += 1
            dividedonecourse[3] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[6] += 1
            dividedtwocourse[8] += 1
            dividedtwocourse[13] += 1
        if course == '化学历史地理':
            numcourse[14] += 1
            dividedonecourse[1] += 1
            dividedonecourse[4] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[7] += 1
            dividedtwocourse[8] += 1
            dividedtwocourse[13] += 1
        if course == '生物政治历史':
            numcourse[15] += 1
            dividedonecourse[2] += 1
            dividedonecourse[3] += 1
            dividedonecourse[4] += 1

            dividedtwocourse[9] += 1
            dividedtwocourse[10] += 1
            dividedtwocourse[12] += 1
        if course == '生物政治地理':
            numcourse[16] += 1
            dividedonecourse[2] += 1
            dividedonecourse[3] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[9] += 1
            dividedtwocourse[11] += 1
            dividedtwocourse[13] += 1
        if course == '生物历史地理':
            numcourse[17] += 1
            dividedonecourse[2] += 1
            dividedonecourse[4] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[10] += 1
            dividedtwocourse[11] += 1
            dividedtwocourse[14] += 1
        if course == '政治历史地理':
            numcourse[18] += 1
            dividedonecourse[3] += 1
            dividedonecourse[4] += 1
            dividedonecourse[5] += 1

            dividedtwocourse[12] += 1
            dividedtwocourse[13] += 1
            dividedtwocourse[14] += 1
    print(numcourse)
    print(dividedonecourse)
    print(dividedtwocourse)





if __name__ == "__main__":
    dataAnalysis()