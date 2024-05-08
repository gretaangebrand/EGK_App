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
#5 Zonen mittels Herzfrequenz einteilen
print(df["HeartRate"])

# %%
max_hr = int(input("Bitte geben Sie die maximale Herzfrequenz ein: "))

#Definition der 5 HR-Zonen
zones = {
    "Zone 1": (0.5 * max_hr, 0.6 * max_hr),
    "Zone 2": (0.6 * max_hr, 0.7 * max_hr),
    "Zone 3": (0.7 * max_hr, 0.8 * max_hr),
    "Zone 4": (0.8 * max_hr, 0.9 * max_hr),
    "Zone 5": (0.9 * max_hr, 1.0 * max_hr)
        }

# Aktivität in Zonen eingeteilt
for zone, (lower, upper) in zones.items():
    #df[zone] = (df["HeartRate"] > lower) & (df["HeartRate"] <= upper)
    df[zone] = (df["HeartRate"].apply(lambda x: 1 if lower <= x <= upper else 0))



# %%
#Zeit in jeder Zone berechnen (in Minuten)
time_in_zones = {}
for zone in zones:
    time_in_zone = df[zone].sum() * df["Duration"].mean() / 60  # in Minuten
    time_in_zones[zone] = round(time_in_zone, 2)

#Ergbnisse anzeigen
for zone, time in time_in_zones.items():
    print(f"{zone}: {time} Minuten")

# %%
# Durchschnittliche Leistung in jeder Zone berechnen
avg_power_in_zones = {}
for zone in zones:
    avg_power_in_zone = df[df[zone] == 1]["PowerOriginal"].mean()
    avg_power_in_zones[zone] = round(avg_power_in_zone, 2)

# Ergebnisse anzeigen
print("Durchschnittliche Leistung in jeder Zone:")
for zone, avg_power in avg_power_in_zones.items():
    print(f"{zone}: {avg_power} Watt")
