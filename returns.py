import pandas as pd
import numpy as np
from analysis import bbas3
from analysis import bbrk3
from analysis import brml3
from analysis import cmig3
from analysis import ggbr4
from analysis import itsa4
from analysis import itub4
from analysis import petr4
from analysis import usim5
from analysis import vale3
from analysis import ibov


#Para utilizar o modelo CAPM precisamos pegar os desvios-padrões dos papéis e do ibov

ibov_std = ibov['Adj Close'].diff().std()

#No modelo CAPM, o retorno esperado (R) é função da taxa livre de risco (r0), dos desvios padrões do papel e do mercado e do prêmio de risco de mercado (PRM): 
# R = r0 + (Cov(papel, ibov)/ibov_std)*PRM
# O PRM será utilizado a partir do calculado pelo prof. Damodaran. O valor aqui é o de jan/2020
# O r0 utilizado é a selic em taxa mensal. Pode-se utilizar também o spread dos títulos do tesouro com vencimentos no próximo ano em taxas mensais. 
# Selic definida pelo Copom em 19/03/2020

selic = 0.035
r0 = (1+selic)**(1/12)-1
PRM_year = 0.0816
PRM = (1+PRM_year)**(1/12)-1

x = pd.merge(bbas3, bbrk3, on='Date', suffixes=('_bbas3', '_bbrk3'))
x =  pd.merge(x, brml3, on = 'Date')
x = pd.merge(x, cmig3, on = 'Date', suffixes = ('_brml3', '_cmig3'))
x = pd.merge(x, ggbr4, on = 'Date')
x = pd.merge(x, itsa4, on = 'Date', suffixes = ('_ggbr4', '_itsa4'))
x = pd.merge(x, itub4, on = 'Date')
x = pd.merge(x, petr4, on = 'Date', suffixes = ('_itub4', '_petr4'))
x = pd.merge(x, usim5, on = 'Date')
x = pd.merge(x, vale3, on = 'Date', suffixes = ('_usim5', '_vale3'))
x = pd.merge(x, ibov, on = 'Date')
x = pd.DataFrame(x.cov(), columns=['Adj Close_bbas3', 'Adj Close_bbrk3', 'Adj Close_brml3', 'Adj Close_cmig3','Adj Close_ggbr4', 'Adj Close_itsa4', 'Adj Close_itub4', 'Adj Close_petr4', 'Adj Close_usim5', 'Adj Close_vale3', 'Adj Close'])

cov_bbas3 = x.loc['Adj Close', 'Adj Close_bbas3']
cov_bbrk3 = x.loc['Adj Close', 'Adj Close_bbrk3']
cov_brml3 = x.loc['Adj Close', 'Adj Close_brml3']
cov_cmig3 = x.loc['Adj Close', 'Adj Close_cmig3']
cov_ggbr4 = x.loc['Adj Close', 'Adj Close_ggbr4']
cov_itsa4 = x.loc['Adj Close', 'Adj Close_itsa4']
cov_itub4 = x.loc['Adj Close', 'Adj Close_itub4']
cov_petr4 = x.loc['Adj Close', 'Adj Close_petr4']
cov_usim5 = x.loc['Adj Close', 'Adj Close_usim5']
cov_vale3 = x.loc['Adj Close', 'Adj Close_vale3']

bbas3_ret = r0 + (cov_bbas3/ibov_std)*PRM
bbrk3_ret = r0 + (cov_bbrk3/ibov_std)*PRM
brml3_ret = r0 + (cov_brml3/ibov_std)*PRM
cmig3_ret = r0 + (cov_cmig3/ibov_std)*PRM
ggbr4_ret = r0 + (cov_ggbr4/ibov_std)*PRM
itsa4_ret = r0 + (cov_itsa4/ibov_std)*PRM
itub4_ret = r0 + (cov_itub4/ibov_std)*PRM
petr4_ret = r0 + (cov_petr4/ibov_std)*PRM
usim5_ret = r0 + (cov_usim5/ibov_std)*PRM
vale3_ret = r0 + (cov_vale3/ibov_std)*PRM

exp_returns = [bbas3_ret, bbrk3_ret, brml3_ret, cmig3_ret, ggbr4_ret, itsa4_ret, itub4_ret, petr4_ret, usim5_ret, vale3_ret]
print(exp_returns)