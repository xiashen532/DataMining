# -*- coding: utf-8 -*-

import pandas as pd


# 查看每个属性的所有可能取值
def overview(path):
    esf = pd.read_csv(path, encoding='utf-8')

    # print(esf['model'].unique())
    # print(esf['direction'].unique())
    # print(esf['fitment'].unique())
    # print(esf['floor'].unique())
    # print(esf['address'].unique())
    # print(esf[esf.duplicated()])
    print(esf.info())
    # esf = clean(esf)
    # esf.to_csv(path, encoding='utf-8', index=False)


# 清除空值
def clean(file):
    file.dropna(axis=0, how='any', inplace=True)
    return file


path1 = "../data/res.csv"
overview(path1)
