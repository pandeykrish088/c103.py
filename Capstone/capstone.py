import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
df2 = pd.read_csv("data.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "Country", title = "Cases in the World")
#fig = px.scatter(df2, x = "Country", y = "InternetUsers", size = "Percentage", color = "Country")

fig.show()