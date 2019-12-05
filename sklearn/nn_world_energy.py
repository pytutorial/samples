from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

years = list(range(1990, 2008))

energies = [8761, 8818, 8830, 8923, 8993, 9215, 9447, 9540, 9593, 9789,
10016, 10114, 10330, 10688, 11171, 11489, 11835, 12152 ]

X = [[x] for x in years]
Y = [y/1000 for y in energies]
Xtrain = X[:-2]
Ytrain = Y[:-2]
Xtest = X[-2:]
Ytest = Y[-2:]

scaler = MinMaxScaler()
scaler.fit(Xtrain)

Xtrain = scaler.transform(Xtrain)
Xtest = scaler.transform(Xtest)

model = MLPRegressor(50, max_iter=10000, tol=-1, verbose=True)
model.fit(Xtrain, Ytrain)

Ypredict = model.predict(Xtest)

for i in range(2):
    predict = round(1000 * Ypredict[i])
    err = round(100 * (predict - energies[-2+i])/energies[-2+i], 1)
    print(f'Year {years[-2+i]}, real : {energies[-2+i]},\
                    predict : {predict}, err(%) : {err}')

plt.plot(years, energies, '.', label='real')
plt.plot(years[:-2], 1000 * model.predict(Xtrain), label='validate')
plt.plot(years[-2:], 1000 * model.predict(Xtest), '.', label='predict')
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('World energy consumption (MTOE)')
plt.show()