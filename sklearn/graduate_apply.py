import pandas as pd

df = pd.read_csv('data/graduate_apply.csv')
print(df.head())

data = df.values
X = data[:, 1:4]
y = data[:, 0]
Ntrain = int(0.7 * len(data))
Xtrain, ytrain = X[:Ntrain], y[:Ntrain]
Xtest, ytest = X[Ntrain:], y[Ntrain:]

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(Xtrain, ytrain)

print('Accuracy: ', model.score(Xtest, ytest))