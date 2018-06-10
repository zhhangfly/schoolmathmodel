import pandas as pd
import numpy as np
import random
from pandas import Series,DataFrame
from sklearn.linear_model import LinearRegression


def analysis1():
    #时间列表
    newxlist=[]

    #开盘、收盘、利润、风险
    startlist=[]
    endlist=[]
    profitratelist=[]
    risklist=[]
    #预测列表
    predictlist=list(range(6708))
    #预测列表对应的预测K值
    kpredictlist=list(range(6708))


    rawdata = pd.read_excel('C:/Users/张博/Desktop/B.xlsx', sheet_name='上证指数',index_col='时间')#读取文件
    ele_y= '收盘'
    ele_date='日期整数'
    ele_start='开盘'

    #------------------开始求所有点的k值以及进行预测点之前的所有点的趋势或震荡判断---------------
    data =rawdata[ele_y].T        #收盘列数据
    array_y=np.array(list(data))

    #-------------------开盘数据、收盘数据-----------------
    start=rawdata[ele_start]
    for i in start:
        startlist.append(i)
    end = rawdata[ele_y]
    for i in end:
        endlist.append(i)


    #和原始时间等差的x
    date=rawdata[ele_date]
    for i in date:
        newxlist.append(i-33225)

    array_x=np.array(newxlist).reshape(-1,1)
    #-----------至此长度为6690的x与y已经构造完成-------------------

    #----------------------核心代码--------------------------
    t=0
    c=getcritical(array_x,array_y,6708)
    print('-----------------'+str(c))
    critical_k=c#k的临界值
    for i in range(2,len(array_y)+1):

        if i>=(t+2):         #限制向量的长度至少为3
            x=array_x[t:i]
            y=array_y[t:i]
            [k_value, interpreter, r] = regressF(x, y)#线性拟合
            if(abs(k_value[0])<=critical_k):  #前三个点的回归分析结果
                predictlist[t]=0
                kpredictlist[t]=k_value[0]
                t+=1
            else:
                x=array_x[t:i+1]                #优化模型中增加判定点的个数
                y=array_y[t:i+1]
                [k_value, interpreter, r] = regressF(x, y)
                if(abs(k_value[0])<=critical_k):
                    predictlist[t]=0
                    kpredictlist[t] = k_value[0]
                    t+=1
                else:
                    predictlist[t]=1
                    if abs(k_value[0])>180:#对K的值进行限制，减少其对可视化结果的影响
                        kpredictlist[t]=random.randint(100,180)
                    else:
                        kpredictlist[t] = k_value[0]
                        t=t+1
        else:
            continue
    print(predictlist)
    print(kpredictlist)
    sum1=0#统计前3000个点的趋势点的数目
    sum2=0#其与后部分数据
    for i in range(0,4001):
        if predictlist[i]==1:
            sum1+=1
    for i in range(4001,len(predictlist)):
        if predictlist[i]==1:
            sum2+=1


    #去除异常值
    for i in range(2,len(predictlist)-2):
        if predictlist[i-1]==predictlist[i+1]==predictlist[i-2]==predictlist[i+2]:
            predictlist[i]=predictlist[i-2]
    print(predictlist)

    #---------------------------对模型的评价--------------------
    result,profitratelist,risklist=getProfitAndRisk(startlist,endlist,kpredictlist,predictlist,660,c)#开盘，收盘，趋势预测结果，对应k值，持股周期，阈值K
    print(result)
    print(profitratelist)
    print(risklist)




    #----------------------------------四列值插入到rawdata中-----------------------
    magnitude=data/100                                  #统一和K的数量级方便看趋势
    predict_vector= np.array(predictlist).reshape(-1,1)
    k_vector=np.array(kpredictlist).reshape(-1,1)
    rawdata['预测']=predict_vector
    rawdata['k']=k_vector
    rawdata['数量级']=magnitude
    rawdata['日期']=array_x


    #求相关系数
    corrc=np.corrcoef(abs(k_vector[0:6680].T),magnitude[0:6680].T)
    print('相关系数为:'+str(corrc))
    #写入output1.xls
    rawdata.to_excel('C:/Users/张博/Desktop/output1.xlsx', sheet_name='sheet1')


def analysis2():
    #开盘
    startlist=[]
    endlist=[]
    profitratelist=[]
    risklist=[]
    # 时间列表
    xlist = []
    newxlist = []
    # 预测列表
    predictlist = list(range(3263))
    # 预测列表对应的预测K值
    kpredictlist = list(range(3263))

    rawdata = pd.read_excel('C:/Users/张博/Desktop/B.xlsx', sheet_name='沪深300指数', index_col='时间')
    ele_y = '收盘'
    ele_date = '日期整数'
    ele_start = '开盘'
    yten = rawdata[ele_y][0:10].T
    arrayyten = np.array(list(yten))  # 将series转化为向量从而进行回归分析
    xten = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
    # 通过给出的实际数据试探出k的分界值

    # for i in range(3,6):
    #    x=xten[:i]
    #    y=arrayyten[:i]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # for i in range(6,11):
    #    x=xten[i:]
    #    y=arrayyten[i:]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # 经判断k的分界值设为1比较合适

    # ------------------开始求所有点的k值以及进行预测点之前的所有点的趋势或震荡判断---------------
    data = rawdata[ele_y].T  # 开盘列数据
    array_y = np.array(list(data))
    # 作出仿时间序列的x
    # for i in range(1,len(array_y)+1):
    #   xlist.append(i)
    # array_x=np.array(xlist).reshape(-1,1)
    #-------------------开盘、收盘数据-----------------
    start=rawdata[ele_start]
    for i in start:
        startlist.append(i)
    end = rawdata[ele_y]
    for i in end:
        endlist.append(i)
    # 和原始时间等差的x
    date = rawdata[ele_date]
    for i in date:
        newxlist.append(i - 38355)

    array_x = np.array(newxlist).reshape(-1, 1)
    # -----------至此长度为6690的x与y已经构造完成-------------------
    # [k_value, interpreter, r] = regressF(array_x,array_y)
    # print(k_value)
    # print(interpreter)
    # print(r)
    # ----------------------核心代码--------------------------
    t = 0

    c=getcritical(array_x,array_y,3263)
    print('-----------------'+str(c))
    critical_k = c  # k的临界值，四组数据每组都应该微调
    for i in range(2, len(array_y)-5):

        if i >= (t + 2):  # 限制向量的长度至少为3
            x = array_x[t:i]
            y = array_y[t:i]
            [k_value, interpreter, r] = regressF(x, y)
            # print(k_value[0])
            if (abs(k_value[0]) <= critical_k):  # 前三个点的回归分析结果

                predictlist[t] = 0
                kpredictlist[t] = k_value[0]
                t += 1
            else:
                x = array_x[t:i+5]
                y = array_y[t:i+5]
                [k_value, interpreter, r] = regressF(x, y)
                if (abs(k_value[0]) <= critical_k):
                    predictlist[t] = 0
                    kpredictlist[t] = k_value[0]
                    t += 1
                else:
                    predictlist[t] = 1
                    if k_value[0] > 180:  # 对K的值进行限制，减少其对可视化结果的影响
                        kpredictlist[t] = random.randint(100, 180)
                    else:
                        kpredictlist[t] = k_value[0]
                        t = t + 1
        else:
            continue
    print(predictlist)
    print(kpredictlist)

    #去除异常值
    for i in range(2,len(predictlist)-2):
        if predictlist[i-1]==predictlist[i+1]==predictlist[i-2]==predictlist[i+2]:
            predictlist[i]=predictlist[i-2]
    print(predictlist)

    #---------------------------对模型的评价--------------------
    result,profitratelist,risklist=getProfitAndRisk(startlist,endlist,kpredictlist,predictlist,300,c)
    print(result)
    print(profitratelist)
    print(risklist)

    # ----------------------------------四列值插入到rawdata中-----------------------
    magnitude = data / 100  # 统一和K的数量级方便看趋势
    predict_vector = np.array(predictlist).reshape(-1, 1)
    k_vector = np.array(kpredictlist).reshape(-1, 1)
    rawdata['预测'] = predict_vector
    rawdata['k'] = k_vector
    rawdata['数量级'] = magnitude
    rawdata['日期'] = array_x

    # 求相关系数
    corrc = np.corrcoef(abs(k_vector[0:3220].T), magnitude[0:3220].T)
    print('相关系数为:' + str(corrc))
    # 写入C.xls
    rawdata.to_excel('C:/Users/张博/Desktop/output2.xlsx', sheet_name='sheet1')



def analysis3():
    #开盘
    startlist=[]
    endlist=[]
    profitratelist=[]
    risklist=[]
    # 时间列表
    xlist = []
    newxlist = []
    # 预测列表
    predictlist = list(range(2767))
    # 预测列表对应的预测K值
    kpredictlist = list(range(2767))

    rawdata = pd.read_excel('C:/Users/张博/Desktop/B.xlsx', sheet_name='中证500指数', index_col='时间')
    ele_y = '收盘'
    ele_date = '日期整数'
    ele_start = '开盘'
    yten = rawdata[ele_y][0:10].T
    arrayyten = np.array(list(yten))  # 将series转化为向量从而进行回归分析
    xten = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
    # 通过给出的实际数据试探出k的分界值

    # for i in range(3,6):
    #    x=xten[:i]
    #    y=arrayyten[:i]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # for i in range(6,11):
    #    x=xten[i:]
    #    y=arrayyten[i:]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # 经判断k的分界值设为1比较合适

    # ------------------开始求所有点的k值以及进行预测点之前的所有点的趋势或震荡判断---------------
    data = rawdata[ele_y].T  # 开盘列数据
    array_y = np.array(list(data))
    # 作出仿时间序列的x
    # for i in range(1,len(array_y)+1):
    #   xlist.append(i)
    # array_x=np.array(xlist).reshape(-1,1)
    #-------------------开盘、收盘数据-----------------
    start=rawdata[ele_start]
    for i in start:
        startlist.append(i)
    end = rawdata[ele_y]
    for i in end:
        endlist.append(i)
    # 和原始时间等差的x
    date = rawdata[ele_date]
    for i in date:
        newxlist.append(i - 39096)

    array_x = np.array(newxlist).reshape(-1, 1)
    # -----------至此长度为6690的x与y已经构造完成-------------------
    # [k_value, interpreter, r] = regressF(array_x,array_y)
    # print(k_value)
    # print(interpreter)
    # print(r)
    # ----------------------核心代码--------------------------
    t = 0
    c=getcritical(array_x,array_y,2767)
    print('-----------------'+str(c))
    critical_k = c  # k的临界值
    for i in range(2, len(array_y) + 1):

        if i >= (t + 2):  # 限制向量的长度至少为3
            x = array_x[t:i]
            y = array_y[t:i]
            [k_value, interpreter, r] = regressF(x, y)
            # print(k_value[0])
            if (abs(k_value[0]) <= critical_k):  # 前三个点的回归分析结果

                predictlist[t] = 0
                kpredictlist[t] = k_value[0]
                t += 1
            else:
                x = array_x[t:i + 8]
                y = array_y[t:i + 8]
                [k_value, interpreter, r] = regressF(x, y)
                if (abs(k_value[0]) <= critical_k):
                    predictlist[t] = 0
                    kpredictlist[t] = k_value[0]
                    t += 1
                else:
                    predictlist[t] = 1
                    if k_value[0] > 180:  # 对K的值进行限制，减少其对可视化结果的影响
                        kpredictlist[t] = random.randint(100, 180)
                    else:
                        kpredictlist[t] = k_value[0]
                        t = t + 1
        else:
            continue
    print(predictlist)
    print(kpredictlist)
    sum1 = 0  # 统计前3000个点的趋势点的数目
    sum2 = 0  # 其与后部分数据
    for i in range(0, 1000):
        if predictlist[i] == 1:
            sum1 += 1
    for i in range(1001, len(predictlist)):
        if predictlist[i] == 1:
            sum2 += 1


    #去除异常值
    for i in range(2,len(predictlist)-2):
        if predictlist[i-1]==predictlist[i+1]==predictlist[i-2]==predictlist[i+2]:
            predictlist[i]=predictlist[i-2]
    print(predictlist)
    #---------------------------对模型的评价--------------------
    result,profitratelist,risklist=getProfitAndRisk(startlist,endlist,kpredictlist,predictlist,270,c)
    print(result)
    print(profitratelist)
    print(risklist)
    # ----------------------------------四列值插入到rawdata中-----------------------
    magnitude = data / 100  # 统一和K的数量级方便看趋势
    predict_vector = np.array(predictlist).reshape(-1, 1)
    k_vector = np.array(kpredictlist).reshape(-1, 1)
    rawdata['预测'] = predict_vector
    rawdata['k'] = k_vector
    rawdata['数量级'] = magnitude
    rawdata['日期'] = array_x

    # 求相关系数
    corrc = np.corrcoef(abs(k_vector[0:2730].T), magnitude[0:2730].T)
    print('相关系数为:' + str(corrc))
    # 写入C.xls
    rawdata.to_excel('C:/Users/张博/Desktop/output3.xlsx', sheet_name='sheet1')

def analysis4():
    #开盘
    startlist=[]
    endlist=[]
    proditratelist=[]
    risklist=[]
    # 时间列表
    xlist = []
    newxlist = []
    # 预测列表
    predictlist = list(range(1943))
    # 预测列表对应的预测K值
    kpredictlist = list(range(1943))

    rawdata = pd.read_excel('C:/Users/张博/Desktop/B.xlsx', sheet_name='创业板指数', index_col='时间')
    ele_y = '收盘'
    ele_date = '日期整数'
    ele_start = '开盘'
    yten = rawdata[ele_y][0:10].T
    arrayyten = np.array(list(yten))  # 将series转化为向量从而进行回归分析
    xten = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
    # 通过给出的实际数据试探出k的分界值

    # for i in range(3,6):
    #    x=xten[:i]
    #    y=arrayyten[:i]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # for i in range(6,11):
    #    x=xten[i:]
    #    y=arrayyten[i:]
    #    print(x)
    #    print(y)
    #    [k_value, interpreter, r] = regressF(x, y)
    #    print(k_value)
    #    print(interpreter)
    #    print(r)

    # 经判断k的分界值设为1比较合适

    # ------------------开始求所有点的k值以及进行预测点之前的所有点的趋势或震荡判断---------------
    data = rawdata[ele_y].T  # 开盘列数据
    array_y = np.array(list(data))
    # 作出仿时间序列的x
    # for i in range(1,len(array_y)+1):
    #   xlist.append(i)
    # array_x=np.array(xlist).reshape(-1,1)

    #-------------------开盘、收盘数据-----------------
    start=rawdata[ele_start]
    for i in start:
        startlist.append(i)
    end = rawdata[ele_y]
    for i in end:
        endlist.append(i)

    # 和原始时间等差的x
    date = rawdata[ele_date]
    for i in date:
        newxlist.append(i - 40329)

    array_x = np.array(newxlist).reshape(-1, 1)
    # -----------至此长度为6690的x与y已经构造完成-------------------
    # [k_value, interpreter, r] = regressF(array_x,array_y)
    # print(k_value)
    # print(interpreter)
    # print(r)
    # ----------------------核心代码--------------------------
    t = 0
    c=getcritical(array_x,array_y,1943)
    print('-----------------'+str(c))
    critical_k = c  # k的临界值
    for i in range(2, len(array_y) + 1):

        if i >= (t + 2):  # 限制向量的长度至少为3
            x = array_x[t:i]
            y = array_y[t:i]
            [k_value, interpreter, r] = regressF(x, y)
            # print(k_value[0])
            if (abs(k_value[0]) <= critical_k):  # 前三个点的回归分析结果

                predictlist[t] = 0
                kpredictlist[t] = k_value[0]
                t += 1
            else:
                x = array_x[t:i + 4]
                y = array_y[t:i + 4]
                [k_value, interpreter, r] = regressF(x, y)
                if (abs(k_value[0]) <= critical_k):
                    predictlist[t] = 0
                    kpredictlist[t] = k_value[0]
                    t += 1
                else:
                    predictlist[t] = 1
                    if k_value[0] > 180:  # 对K的值进行限制，减少其对可视化结果的影响
                        kpredictlist[t] = random.randint(100, 180)
                    else:
                        kpredictlist[t] =k_value[0]
                        t = t + 1
        else:
            continue
    print(predictlist)
    print(kpredictlist)
    sum1 = 0  # 统计前3000个点的趋势点的数目
    sum2 = 0  # 其与后部分数据
    for i in range(0, 1001):
        if predictlist[i] == 1:
            sum1 += 1
    for i in range(1001, len(predictlist)):
        if predictlist[i] == 1:
            sum2 += 1


    #去除异常值
    for i in range(2,len(predictlist)-2):
        if predictlist[i-1]==predictlist[i+1]==predictlist[i-2]==predictlist[i+2]:
            predictlist[i]=predictlist[i-2]
    print(predictlist)
    #---------------------------对模型的评价--------------------
    result,proditratelist,risklist=getProfitAndRisk(startlist,endlist,kpredictlist,predictlist,190,c)
    print(result)
    print(proditratelist)
    print(risklist)
    # ----------------------------------四列值插入到rawdata中-----------------------
    magnitude = data / 100  # 统一和K的数量级方便看趋势
    predict_vector = np.array(predictlist).reshape(-1, 1)
    k_vector = np.array(kpredictlist).reshape(-1, 1)
    rawdata['预测'] = predict_vector
    rawdata['k'] = k_vector
    rawdata['数量级'] = magnitude
    rawdata['日期'] = array_x

    # 求相关系数

    corrc = np.corrcoef(abs(k_vector[0:1900].T), magnitude[0:1900].T)
    print('相关系数为:' + str(corrc))
    # 写入C.xls
    rawdata.to_excel('C:/Users/张博/Desktop/output4.xlsx', sheet_name='sheet1')





#--------------------------------------------------股票模拟交易-------------------------------
def getProfitAndRisk(startList,endlist,kList,trendlist,t,k):#开盘，收盘，k值，趋势，持有时间,趋势判别阈值
    risklist=[]
    resultlist=[]
    profitrateList=[]
    days=len(startList)
    print('days'+str(days))
    income=0#收入
    pay=0#支出
    hold=0
    risk=0#风险点个数
    for i in range(0,days-1):
        if abs(kList[i])<1.2*k and abs(kList[i])>0.8*k:
            risk+=1
        if hold==0:#判断当前是否持有股票,持有为1，否则为0
            if kList[i]>0 and trendlist[i] == 1:#当遇到上升趋势的点则第二天买入并将持有标记置为1
                pay=pay+startList[i+1]
                hold=1
            else:
                pass

        else:
            if (kList[i] > 0 and trendlist[i] == 1) or (trendlist == 0):  # 股票呈现上涨趋势或震荡则继续持有
                pass
            else:  # 抛出股票，并将持有标记置为0
                income=income+(endlist[i])*0.97         #收取手续费(只在卖出时收取)
                hold=0
        if (i+1)%t==0:#开始新一轮的买入买出
            if hold==1:#若手中尚有股票未卖出，在此时卖出
                income=income+ (endlist[i])*0.97
            profit=income-pay
            if pay!=0:
                profitrateList.append(income/pay)        #得出收益率
            else:
                profitrateList.append(0)
                print('本持股阶段未买入股票')
            print('本持股周期利润为'+str(profit))
            resultlist.append(profit)
            risklist.append(risk/t)
            income = 0  # 收入
            pay = 0  # 支出
            hold = 0
            risk =0
    sum1=0#优异值
    sum2=0#收益率
    sum3=0#风险值
    for i in range(0,len(resultlist)):#计算优异值
        sum1=sum1+(1-risklist[i])*resultlist[i]

    for i in range(0,len(resultlist)):#计算风险
        sum2=sum2+risklist[i]

    for i in range(0,len(resultlist)):#计算收益值
        sum3=sum3+profitrateList[i]


    print('持股周期数目为'+str(len(risklist)))
    print(sum1/(len(risklist)*t))
    print(sum3 / len(risklist))
    print(sum2 / len(risklist))

    return resultlist,profitrateList,risklist

def getcritical(array_x,array_y,length):
    t=0
    #预测列表对应的预测K值
    kpredictlist=list(range(length))
    for i in range(2, len(array_y) + 1):

        if i >= (t + 2):  # 限制向量的长度至少为3
            x = array_x[t:i]
            y = array_y[t:i]
            [k_value, interpreter, r] = regressF(x, y)
            # print(k_value[0])
            kpredictlist[t] = abs(k_value[0])
            t += 1
    kpredictlist.sort()
    return kpredictlist[int(length/40)]#上证为1/40,沪深为1/20，中证为1/3，创业板为1/3













def regressF(X_parameter,Y_parameter):
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parameter)

    #回归系数(截距)
    intercept = regr.intercept_
    # 回归系数（斜率值）
    k_value = regr.coef_
    #回归函数的得分
    r=regr.score(X_parameter,Y_parameter)
    return k_value,intercept,r








if __name__ == "__main__":
    analysis1()