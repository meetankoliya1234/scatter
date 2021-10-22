import pandas as pd
import plotly_express as px

data = pd.read_csv("C:/Users/Meet Ankoliya/OneDrive/Desktop/Python/project-7/Copy+of+data+-+data.csv")
fig = px.scatter(data,x="date",y="cases",color="country",size_max=60)
fig.show()