import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def elbow_plot(X_scaled):

    inertia = []
    # max_k = 10

    for k in range(1, 11):

        m = KMeans(n_clusters=k, random_state=42)
        m.fit(X_scaled)
        inertia.append(m.inertia_)

    plt.figure(figsize=(8, 5))  
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')    
    plt.ylabel('Inertia')
    plt.xticks(range(1, 11))
    plt.grid()
    plt.show()





def pca_plot(X_scaled, clusters):

        
    pca = PCA(n_components=2)
    comp = pca.fit_transform(X_scaled)

    df = pd.DataFrame(comp, columns=['PC1', 'PC2'])
    df['cluster'] = clusters

    sns.scatterplot(data=df, x='PC1', y='PC2', hue='cluster', palette='Set2')
    plt.title('PCA of Clusters')
        # plt.xlabel('Principal Component 1')
        # plt.ylabel('Principal Component 2')
        # plt.legend(title='Cluster')
    plt.grid()
    plt.show()


       