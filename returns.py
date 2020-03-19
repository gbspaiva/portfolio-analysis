#Para calcular os retornos esperados primeiro vamos ver quais os retornos médios de cada papel
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

bbas3_ret = bbas3[['Adj Close']].apply(lambda bbas3 : np.linalg.norm(bbas3), axis = 1)
print(bbas3_ret.head())
print(bbas3.head())