import matplotlib.pyplot as plt
X = list(range(-5, 6))
Y1 = [5*abs(x) for x in X]
Y2 = [x*x for x in X]

plt.plot(X, Y1, 'b')
plt.plot(X, Y2, '--r')
plt.show()