from transform import word_to_num
from direction import pre_direction
import pandas as pd


def pretreatment(path):
    file = pd.read_csv(path, encoding='utf-8')

    word_to_num(file, 'price_list')
    word_to_num(file, 'area')
    pre_direction(file)

    file.to_csv(path, encoding='utf-8', index=False)

pretreatment("../data/test.csv")
