from pretreatment.transform import word_to_num
from pretreatment.direction import pre_direction
from pretreatment.model import pre_model
from pretreatment.address import pre_address
from pretreatment.fitment import pre_fitment
from pretreatment.overview import clean
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

    file.to_csv("data/res.csv", encoding='utf-8', index=False)
    print("Pretreat Success!\n")

