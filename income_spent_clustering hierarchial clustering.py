# -*- coding: utf-8 -*-
"""Income_Spent_clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mMReZZhjAZI_MVDly3Ws4s5kvNU2gxZI

Importing the basic libraries
"""

import matplotlib.pyplot as plt
import pandas as pd

""" Load and Summarize Dataset from Local Directory"""

from google.colab import files
uploaded = files.upload()

dataset = pd.read_csv('dataset.csv')

print(dataset.shape)
print(dataset.describe())
print(dataset.head(5))

"""Label Encoding"""

from sklearn import preprocessing
 dataset['Gender'] = preprocessing.LabelEncoder().fit_transform(dataset['Gender'])
dataset.head()

"""Dendrogram Data Visualization """

import scipy.cluster.hierarchy as clus

plt.figure(1,figsize = (15,7))
dendrogram = clus.dendrogram(clus.linkage(dataset, method = 'ward'))
 
plt.title("Dentrogram Tree Graph")
plt.xlabel("Customers")
plt.ylabel("Distances")
plt.show()

""" Fit hierarchial clustering to the dataset with  n=5

"""

from sklearn.cluster import AgglomerativeClustering
 model = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage='average')
 y_means = model.fit_predict(dataset)
 y_means

"""  Visualising Clusters for n = 5

cluster 1 : Customer with medium income and medium spend

cluster 2 : Customer with high income and high spend

cluster 3 : Customer with low income and low spend 

cluster 4 : Customer with high income and low spend

cluster 5 : Customer with low income and high spend 
"""

x = dataset.iloc[:, [3,4]].values
plt.scatter(x[y_means==0,0],x[y_means==0,1],s=50, c='brown',label='1')
plt.scatter(x[y_means==1,0],x[y_means==1,1],s=50, c='red',label='2')
plt.scatter(x[y_means==2,0],x[y_means==2,1],s=50, c='green',label='3')
plt.scatter(x[y_means==3,0],x[y_means==3,1],s=50, c='yellow',label='4')
plt.scatter(x[y_means==4,0],x[y_means==4,1],s=50, c='purple',label='4')
 
plt.title('Income Spent Analysis')
plt.xlabel('Income')
plt.ylabel('Spent')
plt.legend()
plt.show()