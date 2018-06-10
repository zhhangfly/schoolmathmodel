import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from scipy.misc import imread
from sklearn.linear_model import LinearRegression
import random


def mainanalysis():
    for i in range(1,75):
        if 75%i==0 and 75/i<50:
            print(i)





















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
    mainanalysis()