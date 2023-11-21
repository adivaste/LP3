import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
df.head()

df.info()
df.describe()

# Remove the heatmap part for now
# fig = plt.figure(figsize=(12, 10))
# sns.heatmap(df.corr(), annot=True, fmt='.2f')
# plt.show()

df = df[['PRICEEACH', 'MSRP']]
df.head()
df.isna().any()

df.describe().T
df.shape
df.info()
df.isnull().sum()
df.dtypes
inertia = []

for i in range(1, 11):
    clusters = KMeans(n_clusters=i, init='k-means++', random_state=42, n_init=10)  # Set n_init explicitly
    clusters.fit(df)
    inertia.append(clusters.inertia_)

plt.figure(figsize=(6, 6))
sns.lineplot(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=inertia)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)  # Set n_init explicitly
y_kmeans = kmeans.fit_predict(df)
y_kmeans

plt.figure(figsize=(8, 8))
sns.scatterplot(x=df['PRICEEACH'], y=df['MSRP'], hue=y_kmeans)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', label='Centroids', marker='*')
plt.legend()
plt.show()

kmeans.cluster_centers_




#distortions = []
#K = range(l,10) 
#for k in K: 
#kmeanModel = KMeans(n_clusters=k) 
#kmeanModel.fit(df) 
#distortions.append(kmeanModel.inertia_)
#plt.figure(figsize=(16,8))
#plt.plot(K, distortions, 'bx-') 
#plt.xlabel('k') 
#plt.ylabel('Distortion') 
#plt.title('The Elbow Method showing the optimal k') plt.show() 
