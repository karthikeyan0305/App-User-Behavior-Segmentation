from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def scale_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def train_kmeans(X_scaled, k=4):
    model =  KMeans(n_clusters=k, random_state=42)
    clusters = model.fit_predict(X_scaled)
    return clusters, model