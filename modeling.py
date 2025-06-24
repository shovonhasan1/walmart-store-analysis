

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def run_store_level_regressions(df):

    results = []

    for store_id in df['Store_Number'].unique():
        store_data = df[df['Store_Number'] == store_id]


        X = store_data[['CPI', 'Unemployment', 'Fuel_Price']]
        y = store_data['Weekly_Sales']

        model = LinearRegression()
        model.fit(X, y)

        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)

        results.append({
            'Store_Number': store_id,
            'CPI_Coeff': model.coef_[0],
            'Unemployment_Coeff': model.coef_[1],
            'FuelPrice_Coeff': model.coef_[2],
            'R_squared': r2
        })

    return pd.DataFrame(results)
