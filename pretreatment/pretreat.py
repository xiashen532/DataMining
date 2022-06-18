from transform import word_to_num
import pandas as pd


def pretreatment(path):
    file = pd.read_csv(path, encoding='utf-8')

    word_to_num(file, 'price_list')
    word_to_num(file, 'area')
    word_to_num(file, 'model')

    file.to_csv(path, encoding='utf-8', index=False)
