import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Transformando os csvs em pandas datasets

bbas3 = pd.read_csv('bbas3.csv', sep=';', thousands='.', decimal=',')
print(bbas3)