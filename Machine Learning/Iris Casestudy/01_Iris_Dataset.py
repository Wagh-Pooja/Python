"""
    Consider Below Characteristics of Machine Learning Application

    Classifier : Decision Tree
    Dataset : Iris Dataset
    Features : Sepal Width, Sepal Length, Petal Width, Petal Length
    Labels : Versicolor, Setosa, Virginica
    Training Dataset : 150 Entries
    Testing Dataset : -
"""


from sklearn.datasets import load_iris

iris = load_iris()

print("Feature Names of iris dataset :")
print(iris.feature_names)

print("Target names of iris dataset :")
print(iris.target_names)

print("First 10 elements from iris dataset")

for i in range(len(iris.target)):
    print("ID : %d , Features : %s, Label : %s" % (i, iris.data[i], iris.target[i]))
    