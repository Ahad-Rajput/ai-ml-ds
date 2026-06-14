import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('data.csv')

kmean_mdl = KMeans(n_clusters=2)  # create kmeans model and divide data into 2 groups

cluster_predict = kmean_mdl.fit_predict(df[['exp', 'salary']])  # Train the model

df['cluster'] = cluster_predict  # creating a new column named cluster at run time

cluster_0 = df[df['cluster'] == 0]  # selects only rows where cluster = 0
cluster_1 = df[df['cluster'] == 1]  # selects only rows where cluster = 1

plt.scatter(cluster_0['exp'], cluster_0['salary'])  # plot all points that belongs to cluster_0
plt.scatter(cluster_1['exp'], cluster_1['salary'])  # plot all points that belongs to cluster_1

plt.show()