import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from returns import exp_returns
from returns import var_eqt



#Carteira de variância mínima usando matrizes
A = 2 * var_eqt
vec1 = [[1,1,1,1,1,1,1,1,1,1,1,0]]
vec2 = np.transpose([[1,1,1,1,1,1,1,1,1,1,0]])
A = np.concatenate((A, vec2), axis=1)
A = np.concatenate((A,vec1))
A_inv = np.linalg.pinv(A)
b = np.transpose([[0,0,0,0,0,0,0,0,0,0,0,1]])
mvp_weights = A_inv.dot(b)
np.delete(mvp_weights,11)

mvp_returns = mvp_weights.transpose().dot(exp_returns)
mvp_variance = mvp_weights.dot(mvp_returns.transpose().dot(var_eqt))

print(mvp_weights)
print('')
print(mvp_returns)
print('')
print(mvp_variance)