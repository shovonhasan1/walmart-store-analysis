import pandas as pd

def load_and_clean_data(filepath):

    df = pd.read_csv(filepath)

    df.columns = df.columns.str.strip()

    df['Weekly_Sales'] = df['Weekly_Sales'].replace('[,]', '', regex=True).astype(float)

    df['Date'] = pd.to_datetime(df['Date'])

    df = df.sort_values(by=['Store_Number', 'Date']).reset_index(drop=True)

    return df