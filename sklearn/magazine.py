import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Data source : http://logisticregressionanalysis.com/MiscPages/KidCreative.csv
df = pd.read_csv('data/magazine.csv')

values = df.values
X = values[:, 2:]
y = values[:, 1]

Ntrain = int(0.7 * len(X))
Xtrain = X[:Ntrain]
ytrain = y[:Ntrain]

#model = KNeighborsClassifier(n_neighbors=3)
#model = SVC(kernel='linear')
#model = DecisionTreeClassifier()
model = LogisticRegression()
model.fit(Xtrain, ytrain)

Xtest = X[Ntrain:]
ytest = y[Ntrain:]

score = model.score(Xtest, ytest)
print('test accuracy = ', score)