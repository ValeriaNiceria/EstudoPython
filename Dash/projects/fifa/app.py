import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly

df_fifa = pd.read_csv('data/fifa.csv')
print(df_fifa.head())

