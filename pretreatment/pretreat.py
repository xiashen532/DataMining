from transform import word_to_num
from direction import pre_direction
from model import pre_model
from address import pre_address
from fitment import pre_fitment
from overview import clean
import pandas as pd


def pretreatment(path):
    file = pd.read_csv(path, encoding='utf-8')

    file = clean(file)
    file = word_to_num(file, 'price_list')
    file = word_to_num(file, 'area')
    file = pre_direction(file)
    file = pre_model(file)
    file = pre_address(file)
    file = pre_fitment(file)

    file.to_csv("../data/res.csv", encoding='utf-8', index=False)

pretreatment("../data/ershoufang.csv")
