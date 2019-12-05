import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier

def get_class(species):
    return {
    'setosa': [1, 0, 0],
    'versicolor': [0, 1, 0],
    'virginica': [0, 0, 1]
    }[species]
    
df = pd.read_csv('data/iris.csv')
values = df.values
X = np.array(values[:, :-1], dtype=np.float)
Y = np.array([get_class(species) for species in values[:, -1]])

Xtrain = np.concatenate((X[:35], X[50:85], X[100:135]))
Ytrain = np.concatenate((Y[:35], Y[50:85], Y[100:135]))
Xtest = np.concatenate((X[35:50], X[85:100], X[135:]))
Ytest = np.concatenate((Y[35:50], Y[85:100], Y[135:]))

model = MLPClassifier(hidden_layer_sizes=(5,), activation='tanh',
                            max_iter=10000, tol=1e-7, verbose=True)
model.fit(Xtrain, Ytrain)
score = model.score(Xtest, Ytest)
print('test score = ', score)