#Assigning features and labels variables

#First feature
weather = ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']

#Second feature
temp = ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

#Label or Target Variable
play = ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

#import LabelEncoder
from sklearn import preprocessing

#creating LabelEncoder
le = preprocessing.LabelEncoder()

#Converting string labels into numbers
weather_encoded = le.fit_transform(weather)

print(weather_encoded)


#Converting string labels into numbers
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)

print(temp_encoded)


#Combining weather and temp into single list of tuples
features = list(zip(weather_encoded,temp_encoded))

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)


#Train model using training sets
model.fit(features,label)


#Predict Output
predicted = model.predict([[0,2]]) #0 : Overcast, 2 : Mild
print(predicted)