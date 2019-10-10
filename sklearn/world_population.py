import matplotlib.pyplot as plt
from sklearn import linear_model

# World population : https://en.wikipedia.org/wiki/World_population_estimates

years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
populations = [6.067, 6.137, 6.215, 6.314, 6.396, 6.477,6.555, 6.625, 6.705, 6.81, 6.892 ]

X = [[x] for x in years]
y = populations
model = linear_model.LinearRegression()
model.fit(X, y)

y_predict = model.predict(X)

plt.plot(X, y, '.', label='real')
plt.plot(X, y_predict, '-', label='prediction')
plt.xlabel('years')
plt.ylabel('populations')
plt.legend(loc='upper left')
plt.show()