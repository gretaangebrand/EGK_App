#%%
import pandas as pd

df = pd.read_csv("data/activities/activity.csv")
print(df.head())
# %%

#Mittelwert
df["PowerOriginal"].mean()
# %%

#Maximalwert der Leistung
df["PowerOriginal"].max()

# %%
#Leistung über die Zeit in Plot, welcher Leistung und Herzfrequenz über die Zeit anzeigt
import plotly.express as px

df["Time_in_Seconds"] = df.index
fig = px.line(df, x= "Time_in_Seconds", y= "PowerOriginal")
fig.show()


# %%
