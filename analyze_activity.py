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
