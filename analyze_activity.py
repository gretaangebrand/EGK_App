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

# Angenommene maximale Herzfrequenz und Ruheherzfrequenz
max_hr = 220 - age

# Definition der Zonen
def teile_in_herzfrequenz_zonen(herzfrequenz, max_hr):
    zonen = {
        "Zone 1": (0.5 * max_hr, 0.6 * max_hr),
        "Zone 2": (0.6 * max_hr, 0.7 * max_hr),
        "Zone 3": (0.7 * max_hr, 0.8 * max_hr),
        "Zone 4": (0.8 * max_hr, 0.9 * max_hr),
        "Zone 5": (0.9 * max_hr, max_hr)
        }
    
    for zone, (min_hf, max_hf) in zonen.items():
        if min_hf <= herzfrequenz < max_hf:
            return zone
    return "Außerhalb der Zonen"

# Beispiel Herzfrequenzdaten
df[""] = HeartRate

# Einteilung der Herzfrequenz in Zonen
heart_rate_zones = []
for hr in heart_rates:
    for zone, (lower, upper) in zones.items():
        if lower <= hr <= upper:
            heart_rate_zones.append((hr, zone))
            break

# Ausgabe der Herzfrequenzdaten mit zugehöriger Zone
for hr, zone in heart_rate_zones:
    print(f"Herzfrequenz: {hr}, Zone: {zone}")

# %%
