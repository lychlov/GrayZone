import numpy as np
import matplotlib.pyplot as plt

history_data = [0.45, 5, 1, 6, 1.6, 6.31, 2.16, 6.63, 2.91, 6.97, 3.93, 7.33, 5.3, 7.7, 7.16, 8.4]
history_data = [5.00, 6.00, 6.31, 6.63, 6.97, 7.33, 7.70]
n = len(history_data)
X0 = np.array(history_data)

history_data_agg = [sum(history_data[0:i + 1]) for i in range(n)]
X1 = np.array(history_data_agg)
B = np.zeros([n - 1, 2])
Y = np.zeros([n - 1, 1])
for i in range(n - 1):
    B[i][0] = -0.5 * (X1[i] + X1[i + 1])
    B[i][1] = 1
    Y[i][0] = X0[i + 1]

A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
a = A[0][0]
u = A[1][0]

print(A)
print(a, u)
