import pandas as pd

def load_data():
    
    try:
        df = pd.read_csv("data/app_user_behavior_dataset.csv")

        df.fillna(df.mean(numeric_only=True), inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None