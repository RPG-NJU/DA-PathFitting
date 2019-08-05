#
#!/usr/bin/python3
import numpy as np
import numpy.linalg
from scipy.io import loadmat
import matplotlib.pyplot as plt

def loaddata() :
    global base, path_chan
    m = loadmat("data/homework.mat")
    base = { int(ind) : np.array([x, y]) for ind, x, y, z in m['config'] }
    path_chan = m['path_chan']

def linear_regression(X, Y) :
    w = Y @ (X - X.mean()) / (X @ X - X.sum() * X.mean())
    b = (Y - w * X).mean()
    err = np.linalg.norm(w * X + b - Y)
    print("linear_regression的输出为", err / np.sqrt(X.shape[0]))
    return w, b


def PCA(X):
    center = X.mean(axis=0)
    demean = X - center
    cov = np.cov(X.T)
    egval, egvec = np.linalg.eig(cov)
    egvec = egvec.T
    vec = egvec[0] if egval[0] >= egval[1] else egvec[1]
    vec2 = egvec[1] if egval[0] >= egval[1] else egvec[0]
    print(np.linalg.norm(demean @ vec2) / np.sqrt(X.shape[0]))
    return vec[1] / vec[0], -vec[1] / vec[0] * center[0] + center[1]

loaddata()
plt.title('raw data')
plt.scatter(*path_chan.T, linewidths=0.1)
plt.axis('scaled')
plt.show()

def task1_show(w, b, title='') :
    def get_intersection(w1, b1, w2, b2) :
        return (b2 - b1) / (w1 - w2)
    x = np.array([
        get_intersection(w[0], b[0], w[1], b[1]),
        get_intersection(w[1], b[1], w[2], b[2]),
        get_intersection(w[2], b[2], w[3], b[3]),
        get_intersection(w[3], b[3], w[0], b[0]),
    ])
    y = x * w + b
    x = np.hstack([x[:], x[:1]])
    y = np.hstack([y[:], y[:1]])
    plt.clf()
    plt.title(title)
    plt.plot(x, y, c='r')
    plt.scatter(*path_chan.T, linewidths=0.1)
    plt.axis('scaled')
    plt.show()

def task1_sol1() :
    split = [0, 70, 210, 274, 382]
    X, Y = path_chan.T
    # print(type(X))
    w, b = [], []
    f, t = split[0], split[1]
    cw, cb = linear_regression(Y[f:t], X[f:t])
    cw, cb = 1.0 / cw, -cb / cw
    w.append(cw)
    b.append(cb)
    f, t = split[1], split[2]
    cw, cb = linear_regression(X[f:t], Y[f:t])
    w.append(cw)
    b.append(cb)
    f, t = split[2], split[3]
    cw, cb = linear_regression(Y[f:t], X[f:t])
    cw, cb = 1.0 / cw, -cb / cw
    w.append(cw)
    b.append(cb)
    f, t = split[3], split[4]
    cw, cb = linear_regression(X[f:t], Y[f:t])
    w.append(cw)
    b.append(cb)
    task1_show(w, b, 'least square method')

def task1_sol2() :
    split = [0, 70, 210, 274, 382]
    X = path_chan
    w, b = [], []
    for i in range(4) :
        l, r = split[i], split[i+1]
        cw, cb = PCA(X[l:r])
        w.append(cw)
        b.append(cb)
    task1_show(w, b, 'PCA')

task1_sol1()
task1_sol2()

