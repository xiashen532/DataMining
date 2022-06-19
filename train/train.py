import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn import datasets


def train(path):
    file = pd.read_csv(path, encoding='utf-8')
    file.drop(file.tail(1).index, inplace=True)
    del file['name']
    # del file['floor']

    # 平滑处理y
    y = np.log1p(file['total_list'])
    del file['total_list']
    # file = preprocessing.scale(file)
    x = file

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    # print(x_train.shape)
    # print(x_test.shape)

    lr = LinearRegression()
    lr.fit(x_train, y_train)  # 把训练集的自变量，因变量添加到函数fit()中，进行训练
    # print(lr.coef_)  # lr.coef_得到的是每个自变量的权重系数
    # print(lr.intercept_)  # lr.intercept_得到的是截距

    y_pred = lr.predict(x_test)

    MSE = metrics.mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    Rsquare = metrics.r2_score(y_test, y_pred)

    print("Train success! \nSome results :")
    print('MSE:', MSE)
    print('RMSE:', RMSE)
    print('Rsquare:', Rsquare)


    return file


def train_plot(y_test, y_pred):
    mpl.rcParams['font.family'] = ['sans-serif']
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(15, 5))
    plt.plot(range(len(y_test)), y_test, 'r', label='测试数据')
    plt.plot(range(len(y_test)), y_pred, 'b', label='预测数据')
    plt.show()

    plt.scatter(y_test, y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
    plt.xlabel('真实值')
    plt.ylabel('预测值')
    plt.show()
