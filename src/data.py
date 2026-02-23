import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    # fill missing numeric values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    return df
