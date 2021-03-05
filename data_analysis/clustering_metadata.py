from glob import glob
import pandas as pd
import json
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # model
import math
import numpy as np

meta_data = glob(r'D:\meta_data\*.json')
len(meta_data)  # 43861
track_df = pd.DataFrame(columns=["tempo", "tempo_confidence"])

# <json files into pandas DataFrame>
for i in range(1001):
    # <load json file>
    with open(meta_data[i]) as f:
        meta_json = json.load(f)

    # <seperate song information>
    data_info = pd.DataFrame({
        "tempo": meta_json['track']['tempo'],
        "tempo_confidence": meta_json['track']['tempo_confidence']
    }, index=[i])

    track_df = track_df.append(data_info, sort=True)

# <K-means Clustering>
model = KMeans(n_clusters=10, random_state=0, algorithm='auto')
model.fit(track_df)
pred = model.predict(track_df)
pred
len(pred)
plt.scatter(x=track_df['tempo'], y=track_df['tempo_confidence'], c=pred)
