import plotly
plotly.tools.set_credentials_file(username='zzhang115', api_key='F3maZlp8z5KbNAYJZltX')
import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

table = ff.create_table(df)
py.iplot(table)