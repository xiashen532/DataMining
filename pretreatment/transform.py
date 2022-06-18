# -*- coding: utf-8 -*-

import re
import pandas as pd


# import matplotlib.pyplot as plt
# import seaborn as sns

# 将数字汉字符号混合的原始数据转换为数值
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
