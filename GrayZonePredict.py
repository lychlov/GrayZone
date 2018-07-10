# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GrayZonePredict
   Description :
   Author :       Lychlov
   date：          2018/7/10
-------------------------------------------------
   Change Activity:
                   2018/7/10:
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
import math

# x = np.array([0.45, 5, 1, 6, 1.6, 6.31, 2.16, 6.63, 2.91, 6.97, 3.93, 7.33, 5.3, 7.7, 7.16, 8.4])
xu = np.array([5.00, 6.00, 6.31, 6.63, 6.97, 7.33, 7.70])
tu = [2, 4, 6, 8, 10, 12, 14]
xl = np.array([1.00, 1.60, 2.16, 2.91, 3.93, 5.30, 7.16])
tl = [3, 5, 7, 9, 11, 13, 15]


def array_add_x1(x, step):
    result = [x[0]]
    sum_temp = x[0]
    for i in range(1, len(x)):
        sum_temp += (step[i] - step[i - 1]) * x[i]
        result.append(sum_temp)
    return np.array(result)


def z_array(x1):
    result = []
    for i in range(1, len(x1)):
        result.append(0.5 * (x1[i] + x1[i - 1]))
    return np.array(result)


xu1 = array_add_x1(xu, tu)
xl1 = array_add_x1(xl, tl)
zu = z_array(xu1)
zl = z_array(xl1)
Bu = np.vstack((-zu, np.ones(len(zu)))).T
Yu = xu.T[1:]
Au = np.linalg.inv(Bu.T.dot(Bu)).dot(Bu.T).dot(Yu)
Bl = np.vstack((-zl, np.ones(len(zl)))).T
Yl = xl.T[1:]
Al = np.linalg.inv(Bl.T.dot(Bl)).dot(Bl.T).dot(Yl)

t = np.linspace(2, 25, 1000)
xu_f = [(xu1[0] - Au[1] / Au[0]) * math.exp(-Au[0] * (i - tu[0])) + Au[1] / Au[0] for i in t]
xl_f = [(xl1[0] - Al[1] / Al[0]) * math.exp(-Al[0] * (i - tl[0])) + Al[1] / Al[0] for i in t]

min_index = 0
min_diff = 100000
minus = np.fabs(np.array(xu_f) - np.array(xl_f))
t0 = t[np.where(minus == np.min(minus))[0][0]]

xu_f_in = [(xu1[0] - Au[1] / Au[0]) * math.exp(-Au[0] * (i - tu[0])) + Au[1] / Au[0] for i in range(1, 25)]

xl_f_in = [(xl1[0] - Al[1] / Al[0]) * math.exp(-Al[0] * (i - tl[0])) + Al[1] / Al[0] for i in range(1, 25)]

plt.plot(t, xu_f)
plt.plot(t, xl_f)
plt.show()
