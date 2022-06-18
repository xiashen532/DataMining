# -*- coding: utf-8 -*-

import pandas as pd

esf = pd.read_csv("../data/ershoufang.csv", encoding='utf-8')

# 查看每个属性的所有可能取值
print(esf['model'].unique())
print(esf['direction'].unique())
print(esf['fitment'].unique())
print(esf['floor'].unique())
