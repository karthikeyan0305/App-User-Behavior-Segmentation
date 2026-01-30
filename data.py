import pandas as pd

def clean():
    # Load the dataset
    df = pd.read_csv('raw_data.csv')
    
    # Drop rows with missing values
    df.dropna(inplace=True)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Convert date columns to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    # Standardize text columns to lowercase
    df['text_column'] = df['text_column'].str.lower()
    
    # Save the cleaned dataset
    df.to_csv('cleaned_data.csv', index=False)