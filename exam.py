import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from scipy.misc import imread
import requests
import re
from bs4 import BeautifulSoup
import math





def test():
    i=0
    max=0
    while i<1.6:
        ma = (0.7853-i)*2*math.cos(i)
        if ma>max:
            max=ma
        i=i+0.001
    print(max)




if __name__ == "__main__":
    test()