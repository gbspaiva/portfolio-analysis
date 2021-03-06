import pandas as pd
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
ibov = pd.read_csv('ibov.csv', sep=';', thousands='.', decimal=',')

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
ibov = ibov[['Date', 'Adj Close']]



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
var_eqt = pd.DataFrame(x.cov(), columns=['Adj Close_bbas3', 'Adj Close_bbrk3', 'Adj Close_brml3', 'Adj Close_cmig3','Adj Close_ggbr4', 'Adj Close_itsa4', 'Adj Close_itub4', 'Adj Close_petr4', 'Adj Close_usim5', 'Adj Close_vale3', 'Adj Close'])

cov_bbas3 = var_eqt.loc['Adj Close', 'Adj Close_bbas3']
cov_bbrk3 = var_eqt.loc['Adj Close', 'Adj Close_bbrk3']
cov_brml3 = var_eqt.loc['Adj Close', 'Adj Close_brml3']
cov_cmig3 = var_eqt.loc['Adj Close', 'Adj Close_cmig3']
cov_ggbr4 = var_eqt.loc['Adj Close', 'Adj Close_ggbr4']
cov_itsa4 = var_eqt.loc['Adj Close', 'Adj Close_itsa4']
cov_itub4 = var_eqt.loc['Adj Close', 'Adj Close_itub4']
cov_petr4 = var_eqt.loc['Adj Close', 'Adj Close_petr4']
cov_usim5 = var_eqt.loc['Adj Close', 'Adj Close_usim5']
cov_vale3 = var_eqt.loc['Adj Close', 'Adj Close_vale3']

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

exp_returns = [[bbas3_ret, bbrk3_ret, brml3_ret, cmig3_ret, ggbr4_ret, itsa4_ret, itub4_ret, petr4_ret, usim5_ret, vale3_ret]]
exp_returns = np.asmatrix(exp_returns)
var_eqt = var_eqt[['Adj Close_bbas3', 'Adj Close_bbrk3', 'Adj Close_brml3', 'Adj Close_cmig3','Adj Close_ggbr4', 'Adj Close_itsa4', 'Adj Close_itub4', 'Adj Close_petr4', 'Adj Close_usim5', 'Adj Close_vale3']]
var_eqt = var_eqt.drop('Adj Close', axis=0)
var_eqt = np.asmatrix(var_eqt)