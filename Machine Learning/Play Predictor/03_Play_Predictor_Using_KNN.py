import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


def MarvellousPlayPredictor(data_path):

    #step 1 : load data
    data = pd.read_csv(data_path, index_col = 0)

    print("Size of Actual dataset",len(data))

    #step 2 : Clean, Preapre, Manipulate data
    feature_names = ['Whether','Temperature']

    print("Names of features",feature_names)

    whether = data.Whether
    temperature = data.Temperature
    play = data.Play

    #Creating labelEncoder
    le = preprocessing.LabelEncoder()

    #Converting string labels into numbers
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    #Converting string labels into numbers
    temp_encoded = le.fit_transform(temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    #Combining whether and temperature into single list of tuples
    feaures = list(zip(whether_encoded,temp_encoded))

    #step 3 : Train data
    model = KNeighborsClassifier(n_neighbors=3)

    #train model using training sets
    model.fit(feaures,label)

    #step 4 : test data
    predicted = model.predict([[0,2]]) #0:Overcast, 2:Mild
    print(predicted)


    if predicted:
        print("You can play")
    else:
        print("You can't play")


def main():
    print("---------- Marvellous Infosystems ----------")

    print("Machine Learning Application")

    print("Play Predictor Application using K Neighbors Algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()