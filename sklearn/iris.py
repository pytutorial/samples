import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Dataset : https://archive.ics.uci.edu/ml/datasets/iris
df = pd.read_csv('data/iris.csv')
df = df.sample(frac=1)

def get_label(species):
    m = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
    return m.get(species, 0)

X = df.drop('species', 1).values
y = df['species'].apply(get_label).values

Ntrain = int(0.7 * len(X))
Xtrain = X[:Ntrain]
ytrain = y[:Ntrain]

#model = KNeighborsClassifier(n_neighbors=3)
#model = SVC(kernel='linear')
model = DecisionTreeClassifier()
model.fit(Xtrain, ytrain)

Xtest = X[Ntrain:]
ytest = y[Ntrain:]

score = model.score(Xtest, ytest)
print('test accuracy = ', score)

ypredict = model.predict(Xtest)

for i in range(len(Xtest)):
    print(f'Real : {ytest[i]}, predict : {ypredict[i]}') 