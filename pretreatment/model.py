# -*- coding: utf-8 -*-

import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transform import word_to_num


# 可视化 model 属性
def visualize_model(file):
    sns.set(palette="muted", color_codes=True)  # seaborn样式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题
    sns.set(font='SimHei', font_scale=0.8)  # 解决Seaborn中文显示问题

    f, ax1 = plt.subplots(figsize=(20, 20))
    sns.countplot(x='model', data=file, ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=10, rotation=60)  # 旋转x轴标签

    plt.show()


def pre_model(file):
    df_res = pd.DataFrame(
        columns=['name', 'model', 'area', 'direction', 'fitment', 'floor', 'address', 'total_list', 'price_list'])

    for index, row in file.iterrows():
        if ((row['model'] == '4室3厅' or row['model'] == '4室2厅' or row['model'] == '3室2厅' or
                row['model'] == '1室1厅' or row['model'] == '2室1厅' or row['model'] == '3室1厅' or
                row['model'] == '5室2厅' or row['model'] == '2室2厅' or row['model'] == '2室0厅' or
                row['model'] == '1室0厅' or row['model'] == '1室2厅' or row['model'] == '5室3厅')
                and (float(row['total_list']) < 1500)):
            df_res = df_res.append(row, ignore_index=True)

    file = df_res
    # 将 model 属性拆分为 室（room）和厅（hall）
    df1 = pd.concat([file, file['model'].str.split('室', expand=True)], axis=1)
    del df1['model']
    df1.rename(columns={0: 'room', 1: 'hall'}, inplace=True)
    file = df1
    word_to_num(file, 'hall')

    return file

# df = pd.read_csv("../data/ershoufang.csv", encoding='utf-8')
# visualize_model(df)

# df = pd.read_csv("../data/test.csv", encoding='utf-8')
# pre_model(df)
