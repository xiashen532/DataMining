# -*- coding: utf-8 -*-


from pretreatment.pretreat import pretreatment
from train.train import train

if __name__ == '__main__':
    # csv源文件所在路径
    path = "data/ershoufang.csv"
    # 预处理后文件所在路径
    path_res = "data/res.csv"
    pretreatment(path)
    train(path_res)
