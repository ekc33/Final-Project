import pandas as pd
parks = pd.read_csv("park_data.csv")

parks = parks[(parks["type"] == "Park") | (parks["type"] == "Open Space")]
pd.set_option('display.max_columns', None)
parks.head(210)

parks = pd.read_csv("park_data.csv")
parks = parks[(parks["type"] == "Park") | (parks["type"] == "Open Space")]
count = parks["neighborhood"].value_counts()
count

import matplotlib.pyplot as plotter

import numpy as np

objectTypes     = ('Mount Washington', 'Hazelwood', 'Troy Hill', 'South Side Slopes', 'Beechview')
yAxisCategories = np.arange(len(objectTypes))
objectCount     = (5, 5, 5, 6, 6)
stdDeviation    = (0, 0, 0, 0, 0) 

figureObject, axesObject    = plotter.subplots()

hBarChart                   = plotter.barh(yAxisCategories,

                                           objectCount,

                                           xerr=stdDeviation,

                                           align='center',

                                           color='red',

                                           ecolor='blue')

axesObject.set_title('Amount of parks/open space in Pittsburgh per city')

axesObject.set_yticks(yAxisCategories)

axesObject.set_yticklabels(objectTypes)

axesObject.set_xlabel('Park Count')

 

plotter.show()


