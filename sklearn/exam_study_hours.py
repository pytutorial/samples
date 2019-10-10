import pandas as pd
from sklearn.linear_model import LogisticRegression

#Data source : https://en.wikipedia.org/wiki/Logistic_regression

df = pd.read_csv('data/exam_study_hours.csv')
X = df[['hours']].values
y = df['pass'].values

model = LogisticRegression()
model.fit(X, y)

score = model.score(X, y)
print('Accuracy = ', score)

ypredict = model.predict(X)

for i,x in enumerate(X):
    print(f'hour={x[0]}, real={y[i]}, predict={ypredict[i]}')
