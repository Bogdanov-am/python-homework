import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as op


def mapfeature(x, order):
    amt = int((2 + order) / 2 * (order + 1))
    out_x = np.zeros((amt, 1))
    for i in range(n + 1):
        for j in range(i + 1):
            out_x[int((1 + i) / 2 * i) + j] = math.pow(x[0], i - j) * math.pow(x[1], j)
    return out_x


def dec_func(theta, x, y):
    m = len(theta)
    return float(theta.reshape(1, m) @ mapfeature(np.array([x, y]), 6))


def make_data(theta, x_min, x_max, y_min, y_max):
    step_x = (x_max - x_min) / 300
    step_y = (y_max - y_min) / 300
    x = np.arange(x_min, x_max, step_x)
    y = np.arange(y_min, y_max, step_y)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = np.zeros(xgrid.shape)

    for i in range(xgrid.shape[0]):
        for j in range(xgrid.shape[1]):
            zgrid[i,j] = dec_func(theta, xgrid[i, j], ygrid[i, j])

    return xgrid, ygrid, zgrid


def sigmoid(z):
    return 1 / (1 + math.exp(-float(z)))


def cost_func(theta, x, y, order):
    amt = int((2 + order) / 2 * (order + 1))
    m, n = x.shape
    theta = theta.reshape((amt, 1))
    y = y.reshape((m, 1))
    cost = 0;
    for i in range(m):
        cost += math.log10(1 + math.exp(float(-y[i, 0] * theta.transpose() @ mapfeature(x[i, :], order))))

    return cost / len(y)


def gradient_func(theta, x, y, order):
    p_lambda = 0.5

    amt = int((2 + order) / 2 * (order + 1))
    m, n = x.shape
    theta = theta.reshape((amt, 1))
    y = y.reshape((m, 1))
    grad = np.zeros((amt, 1))
    for i in range(len(y)):
        grad += - y[i, 0] * mapfeature(x[i, :], order) * sigmoid(
            -y[i, 0] * theta.transpose() @ mapfeature(x[i, :], order))

    grad[1:] += p_lambda * theta[1:]

    return grad.flatten() / len(y)


file_in = 'ex2data2.txt'
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
X = np.transpose([data['x1'], data['x2']])
m = len(Y)

plt.figure(figsize=(10, 8), dpi=80)

x1 = []
x2 = []
last_index = 0

for i in range(data['y'].count(0)):
    last_index = data['y'].index(0, last_index)
    x1.append(data['x1'][last_index])
    x2.append(data['x2'][last_index])
    last_index += 1
plt.scatter(x1, x2, c='red', label='y = 0')

x1 = []
x2 = []
last_index = 0

for i in range(data['y'].count(1)):
    last_index = data['y'].index(1, last_index)
    x1.append(data['x1'][last_index])
    x2.append(data['x2'][last_index])
    last_index += 1
plt.scatter(x1, x2, marker="x", c='green', label='y = 1')

plt.gca().set(xlabel='Microchip Test 1', ylabel='Microchip Test 2')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

n = 6
m = int((2 + n) / 2 * (n + 1))

initial_theta = np.zeros(m)

Result = op.minimize(fun=cost_func,
                     x0=initial_theta,
                     args=(X, Y, n),
                     method='TNC',
                     jac=gradient_func)

result_theta = Result.x

print(cost_func(result_theta, X, Y, n))

x, y, z = make_data(result_theta, -1.0, 1.2, -0.8, 1.2)
levels = [0]
plt.contour(x, y, z, levels, colors='blue')

plt.show()
