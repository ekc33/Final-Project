import pandas as pd

# Import csv park data
data = pd.read_csv("park_data.csv")

# Filter out all non parks and open space
data = data[(data["type"] == "Park") | (data["type"] == "Open Space")]

# Total all parks and open spaces for each neighborhood
neighborhood = data["neighborhood"].value_counts()

print(beechview/southside slopes)

df = pd.park_data({'val':[10, 30, 20]})
ax = df.plot.bar(x='neighborhoods', y='val', rot=0)

https://cdn.discordapp.com/attachments/469896909755252756/914916478313193482/parkdatavisualization.png

