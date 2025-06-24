from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def cluster_stores(results_df, n_clusters=3):

    features = results_df[['CPI_Coeff', 'Unemployment_Coeff', 'FuelPrice_Coeff', 'R_squared']]

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(features)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    results_df['Cluster'] = kmeans.fit_predict(x_scaled)

    return results_df
