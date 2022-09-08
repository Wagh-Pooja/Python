import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot


def MarvellousPlayPredictor(data_path):

    data = pd.read_csv(data_path, index_col = 0)

    print("Size of Actual Dataset",len(data))

    feature_names = ['Whether','Temperature']

    print("Names of Features",feature_names)

    x = data[feature_names]

    y = data.Play

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/2)

    print("Size of Training dataset",len(x_train))

    print("Size of Testing dataset",len(x_test))


def main():
    MarvellousPlayPredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()