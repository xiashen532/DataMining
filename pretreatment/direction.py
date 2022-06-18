# -*- coding: utf-8 -*-

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 可视化 direction 属性
def visualize_direction(file):
    sns.set(palette="muted", color_codes=True)  # seaborn样式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题
    sns.set(font='SimHei', font_scale=0.8)  # 解决Seaborn中文显示问题

    ax = sns.countplot(x='direction', data=file)
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=5, rotation=60)  # 旋转x轴标签

    plt.show()


# 预处理 direction 属性，凡是有“南“朝向存在均置1，反之置0
def direction(file):
    data = file.loc[:, 'direction']
    res_data = []

    for i in data:
        cnt = 0
        for tmp in i:
            if tmp == '\u5357':  # 识别是否有”南“（\u5357）
                cnt = cnt + 1
        if cnt >= 1:
            res_data.append(1)
        else:
            res_data.append(0)

    df_res = pd.DataFrame(res_data)
    file['direction'] = df_res


# df = pd.read_csv("../data/ershoufang.csv", encoding='utf-8')
# visualize_direction(df)

df = pd.read_csv("../data/test.csv", encoding='utf-8')
direction(df)
