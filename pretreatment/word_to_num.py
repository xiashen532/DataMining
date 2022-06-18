# -*- coding: utf-8 -*-

import re
import pandas as pd

# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv("../data/test.csv", encoding='utf-8')
esf = pd.read_csv("../data/ershoufang.csv", encoding='utf-8')


# 处理数据值为
def word_to_num(file, attribute):
    simple_punctuation = '[\" /,]'
    data = file.loc[:, attribute]
    res_data = []

    for i in data:
        tmp = re.sub('[\u4e00-\u9fa5]', '', i)
        res = re.sub(simple_punctuation, '', tmp)
        res_data.append(res)

    df_res = pd.DataFrame(res_data)
    file[attribute] = df_res


word_to_num(df, 'price_list')
word_to_num(df, 'area')
df.to_csv("../data/test.csv", encoding='utf-8', index=False)
