# -*- coding: utf-8 -*-

import pandas as pd
from pretreatment.transform import word_to_num

# 将floor属性预处理，分成 height 和 max_height 两个属性，对 height做独热码
def pre_floor(file):
    file = file[file['floor'].str.contains('楼层')]
    file = file.reset_index()
    del file['index']
    # file['tmp'] = range(len(file))

    # file1 = pd.read_csv('floor.csv', encoding='utf-8')
    # print(file1['floor'].unique())

    df1 = pd.concat([file, file['floor'].str.split('(', expand=True)], axis=1)
    del df1['floor']
    df1.rename(columns={0: 'height', 1: 'max_height'}, inplace=True)
    file = df1
    file = word_to_num(file, 'max_height')

    dummies = pd.get_dummies(file['height'])
    df2 = pd.concat([file, dummies], axis=1)
    del df2['height']
    df2.rename(columns={'低楼层': 'low', '中楼层': 'medium', '高楼层': 'high'}, inplace=True)
    file = df2
    # del file['tmp']

    return file

