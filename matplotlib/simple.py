import matplotlib.pyplot as plt
X = list(range(-5, 6))
Y = [x*x for x in X]

plt.plot(X,Y)
plt.show()