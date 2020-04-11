import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as op


def sigmoid(z):
    return 1 / (1 + math.exp(-float(z)))


def cost_func(theta, x, y):
    m, n = x.shape
    theta = theta.reshape((n, 1))
    y = y.reshape((m, 1))
    cost = 0;
    for i in range(len(y)):
        cost += math.log10(1 + math.exp(float(-y[i, 0] * theta.transpose() @ x[i, :])))
    return cost / len(y)


def gradient_func(theta, x, y):
    m, n = x.shape
    theta = theta.reshape((n, 1))
    y = y.reshape((m, 1))
    grad = np.zeros((3, 1))
    for i in range(len(y)):
        grad += - y[i, 0] * x[i, :].reshape(len(theta), 1) * sigmoid(-y[i, 0] * theta.transpose() @ x[i, :])
    return grad.flatten()/len(y)


file_in = 'ex2data1.txt'
delimiter = ','
header = ['x1', 'x2', 'y']

data = {}
for entry in header:
    data[entry] = []

with open(file_in, 'r') as file:
    for line in file:
        split = line.split(delimiter)
        count = 0
        for entry in header:
            data[entry].append(float(split[count]))
            count += 1

Y = np.array([y if y == 1 else -1 for y in data['y']])[:, np.newaxis]
X = np.transpose(np.array([[1 for i in range(len(Y))], data['x1'], data['x2']]))
m = len(Y)

plt.figure(figsize=(10, 6), dpi=80)

x1 = []
x2 = []
last_index = 0

for i in range(data['y'].count(0)):
    last_index = data['y'].index(0, last_index)
    x1.append(data['x1'][last_index])
    x2.append(data['x2'][last_index])
    last_index += 1
plt.scatter(x1, x2, marker="x", c='red', label='not admitted')

x1 = []
x2 = []
last_index = 0

for i in range(data['y'].count(1)):
    last_index = data['y'].index(1, last_index)
    x1.append(data['x1'][last_index])
    x2.append(data['x2'][last_index])
    last_index += 1
plt.scatter(x1, x2, marker="x", c='green', label='admitted')

plt.gca().set(xlabel='Exam 1 score', ylabel='Exam 2 score')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

initial_theta = np.zeros(3)


Result = op.minimize(fun=cost_func,
                     x0=initial_theta,
                     args=(X, Y),
                     method='TNC',
                     jac=gradient_func)

theta = Result.x

print(gradient_func(theta, X, Y))
print(theta)
print(cost_func(theta, X, Y))

x1 = np.linspace(int(X[:, 1].min()), int(X[:, 1].max()), 20)

y2 = (- theta[0] - theta[1] * x1) / theta[2]

plt.plot(x1, y2)

plt.show()

