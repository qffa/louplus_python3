# -*- coding:utf-8-

import pandas as pd

def quarter_volume():

    data = pd.read_csv("apple.csv", header = 0)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace = True)

    volume = pd.Series(data['Volume']).resample('Q').sum().sort_values(ascending = False)

    second_volume = volume[1]
    
    return second_volume

print(quarter_volume())
