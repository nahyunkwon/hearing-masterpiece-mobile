import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict

import pandas as pd
import pprint
import json

raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
'age': [20, 19, 22, 21],
'favorite_color': ['blue', 'red', 'yellow', "green"],
'grade': [88, 92, 95, 70]}
df = pd.DataFrame(raw_data)


#print(df.iloc[0]['name'])

df.at[0, 'name'] = "new"
print(df)