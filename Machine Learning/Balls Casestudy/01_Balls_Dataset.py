"""
    Consider Below Characteristics of Machine Learning Application

    Classifier : Decision Tree
    Dataset : Balls Dataset
    Features : Weight & Surface Type
    Labels : Tennis & Cricket
    Training Dataset : 15 Entries
    Testing Dataset : 1 Entry
"""


from sklearn import tree


def MarvellousML(weight,surface):

    BallsFeatures = [[35,1], [47,1], [90,0], [48,1], [90,0], [35,1], [92,0], [35,1], [35,1], [35,1], [96,0], [43,1], [110,0], [35,1], [95,0] ]

    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(BallsFeatures,Names)

    result = clf.predict([[weight,surface]])

    if result == 1:
        print("Your Object Looks Like Tennis Ball")
    elif result == 2:
        print("Your Object Looks Like Cricket Ball")


def main():
    print("---------- Marvellous Infosystems ----------")

    print("Enter Weight of Object :")
    weight = input()

    print("What is the Surface type of your object Rough or Smooth :")
    surface = input()

    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Error : Wrong Input")
        exit()

    MarvellousML(weight,surface)


if __name__ == "__main__":
    main()