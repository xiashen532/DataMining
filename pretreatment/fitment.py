# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 可视化 fitment 属性
def visualize_fitment(file):
    sns.set(palette="muted", color_codes=True)  # seaborn样式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决无法显示符号的问题
    sns.set(font='SimHei', font_scale=0.8)  # 解决Seaborn中文显示问题

    f, ax1 = plt.subplots(figsize=(10, 10))
    sns.countplot(x='fitment', data=file, ax=ax1)
    ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=10, rotation=60)  # 旋转x轴标签

    plt.show()


def pre_fitment(file):
    dummies = pd.get_dummies(file['fitment'])
    df1 = pd.concat([file, dummies], axis=1)
    del df1['fitment']
    df1.rename(columns={'精装': 'jingzhuang', '简装': 'jianzhuang', '毛坯': 'maopi', '其他': 'qita'}, inplace=True)
    file = df1

    return file


# df = pd.read_csv("../data/ershoufang.csv", encoding='utf-8')
# visualize_fitment(df)

# df = pd.read_csv("../data/test.csv", encoding='utf-8')
# pre_fitment(df)
