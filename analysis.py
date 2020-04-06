import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from returns import exp_returns
from returns import var_eqt



#Carteira de variância mínima usando matrizes

A = 2 * var_eqt
vec1 = [[1,1,1,1,1,1,1,1,1,1,0]]
vec2 = np.transpose([[1,1,1,1,1,1,1,1,1,0]])
A = np.concatenate((A, vec2), axis=1)
A = np.concatenate((A,vec1))
A_inv = np.linalg.pinv(A)
b = np.transpose([[0,0,0,0,0,0,0,0,0,0,1]])
mvp_weights = A_inv.dot(b)
mvp_weights = np.delete(mvp_weights,10)

mvp_returns = np.matmul(exp_returns, mvp_weights.transpose())
mvp_variance = mvp_weights.dot(var_eqt.dot(mvp_weights.transpose()))

print(mvp_weights)
print('')
print(mvp_returns)
print('')
print(mvp_variance)