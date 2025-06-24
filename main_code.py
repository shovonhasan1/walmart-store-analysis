# main_code.py

from preprocessing import load_and_clean_data
from modeling import run_store_level_regressions
from Clustering import cluster_stores

def main():
    print("Loading data...")
    df = load_and_clean_data("Walmart_sales_analysis.csv")

    print("Running store-level economic sensitivity analysis...")
    results_df = run_store_level_regressions(df)

    print("Clustering stores based on economic behavior...")
    clustered_df = cluster_stores(results_df, n_clusters=3)

    print("\n  Preview of the clustered results:\n")
    print(clustered_df.head())

    clustered_df.to_excel("store_sensitivity_clustered.xlsx", index=False)

if __name__ == "__main__":
    main()
