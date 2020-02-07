import pandas as pd
import json

#print(type(art_df.iloc[0]['url']))
with open('./artworks_2.0_url.json') as json_file:
    js = json.load(json_file)

js[0]['genre'] = 'test'
print(js[0])
