# -*- coding: utf-8 -*-

import pandas as pd


# 查看每个属性的所有可能取值
def overview(path):
    esf = pd.read_csv(path, encoding='utf-8')

    print(esf['model'].unique())
    print(esf['direction'].unique())
    print(esf['fitment'].unique())
    print(esf['floor'].unique())
    print(esf['address'].unique())

path1 = "../data/ershoufang.csv"
overview(path1)