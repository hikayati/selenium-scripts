import pandas as pd
import os
import json
files = os.listdir("./csvs/")

dics = []
for f in files:
    j = None
    with open("./csvs/"+f, "r") as f:
        j = json.loads( f.read().replace("[", "").replace("]", "") )
    
    dics.append(j)
    
df = pd.DataFrame(dics)
df.to_csv("./preview_stats.csv", index=False)