import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json
import requests
import csv
import pandas as pd
import statistics as st

text = "painting, mona lisa, leonardo da vinci, woman, famous, art, mona lisa's smile, black beauty, human optical illusion, famous, interesting, beautiful, lovely, awesome, great, forest, lake, dark, smile, long hair, brown, calm, gray, classic, trees, hand, nose, head, dress, mountain, really complicated, smiling woman, forest, mountain scenery, dark background, sophisticated pose, portrait, lady, landscape background, enigmatic expression, gioconda, sixteenth century, natural light, expression, brightness, shape, structure, amazing"
words = text.split(',')
print(len(words))