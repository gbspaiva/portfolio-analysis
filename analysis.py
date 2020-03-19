import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#Transformando os csvs em pandas datasets

bbas3 = pd.read_csv('bbas3.csv', sep=';', thousands='.', decimal=',')
bbrk3 = pd.read_csv('bbrk3.csv', sep=';', thousands='.', decimal=',')
brml3 = pd.read_csv('brml3.csv', sep=';', thousands='.', decimal=',')
cmig3 = pd.read_csv('cmig3.csv', sep=';', thousands='.', decimal=',')
ggbr4 = pd.read_csv('ggbr4.csv', sep=';', thousands='.', decimal=',')
itsa4 = pd.read_csv('itsa4.csv', sep=';', thousands='.', decimal=',')
itub4 = pd.read_csv('itub4.csv', sep=';', thousands='.', decimal=',')
petr4 = pd.read_csv('petr4.csv', sep=';', thousands='.', decimal=',')
usim5 = pd.read_csv('usim5.csv', sep=';', thousands='.', decimal=',')
vale3 = pd.read_csv('vale3.csv', sep=';', thousands='.', decimal=',')

#Vamos selecionar a coluna Adj Close, pois ela já leva em conta os dividendos distribuidos

bbas3 = bbas3[['Date', 'Adj Close']]
bbrk3 = bbrk3[['Date', 'Adj Close']]
brml3 = brml3[['Date', 'Adj Close']]
cmig3 = cmig3[['Date', 'Adj Close']]
ggbr4 = ggbr4[['Date', 'Adj Close']]
itsa4 = itsa4[['Date', 'Adj Close']]
itub4 = itub4[['Date', 'Adj Close']]
petr4 = petr4[['Date', 'Adj Close']]
usim5 = usim5[['Date', 'Adj Close']]
vale3 = vale3[['Date', 'Adj Close']]

#Carteira de variância mínima
#mvp_weights = 
#mvp_returns = mvp_returns.transpose().dot(exp_returns)
#mvp_variance = eqt.dot(mvp_returns.transpose().dot(var_eqt))