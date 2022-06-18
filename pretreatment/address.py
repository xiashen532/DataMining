# -*- coding: utf-8 -*-

import re
import pandas as pd


def pre_address(file):
    dummies = pd.get_dummies(file['address'])
    df1 = pd.concat([file, dummies], axis=1)
    del df1['address']
    df1.rename(columns={'浦东': 'pudong', '嘉定': 'jiading', '金山': 'jinshan', '虹口': 'hongkou', '静安': 'jingan',
                        '黄浦': 'huangpu', '闵行': 'minhang', '宝山': 'baoshan', '徐汇': 'xuhui', '普陀': 'putuo',
                        '杨浦': 'yangpu', '长宁': 'changning', '松江': 'songjiang', '青浦': 'qingpu', '奉贤': 'fengxian',
                        '崇明':'chongming'}, inplace=True)
    file = df1

    return file

# df = pd.read_csv("../data/test.csv", encoding='utf-8')
# pre_address(df)
