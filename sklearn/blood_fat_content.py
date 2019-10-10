import pandas as pd
from sklearn import linear_model

df = pd.read_csv('data/blood_fat_content.csv')
df = df.sample(frac=1)

X = df[['weight', 'age']].values
y = df['blood_fat_content'].values
    
Ntrain = int(0.7 * len(X))
Xtrain = X[:Ntrain]
ytrain = y[:Ntrain]

model = linear_model.LinearRegression()
model.fit(Xtrain, ytrain)

Xtest = X[Ntrain:]
ytest = y[Ntrain:]

ypredict = model.predict(Xtest)
for i in range(len(Xtest)):
    yreal, ypred = int(ytest[i]), int(ypredict[i])
    err = abs(ypred - yreal)/yreal * 100;
    print(f'Real={yreal}, predict={ypred}, error(%)={round(err,2)}')