import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
df = pd.read_csv("Data.csv")

np.random.seed(200)
k = 2

centroids = {
    0:[0.1,0.6],
    1:[0.3,0.2]
}

def assignment(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - x2)^2 - (y1 - y2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    return df

#print(df)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return k

df = assignment(df, centroids)
centroids = update(centroids)

while True:
    closest_centroids = df['closest'].copy(deep=True)
    df = assignment(df, centroids)
    centroids = update(centroids)
    if closest_centroids.equals(df['closest']):
        break

print(df['closest'][5])
print(centroids)

plt.scatter(df['x'] , df['y'] , c=df['closest'])
plt.show()

#using sklearn
from sklearn.cluster import KMeans
df = pd.read_csv("Data.csv")

init_cluster = np.ndarray( shape=(2,2), dtype=float , buffer=np.array( [[0.1,0.6], [0.3,0.2]] ) )

kmeans = KMeans(init=init_cluster, n_clusters=2)
kmeans.fit(df)
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

plt.scatter(df['x'] , df['y'] , c=kmeans.labels_)
plt.show()


print(labels)
print(kmeans.cluster_centers_)