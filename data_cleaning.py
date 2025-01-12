"""
data_cleaning.py
-----------------
Module for cleaning and preprocessing scraped data to ensure consistency and quality.

Author: Satej
"""

import pandas as pd


def clean_data(raw_data):
    """
    Cleans and preprocesses scraped data.
    
    Steps:
    1. Remove duplicates.
    2. Handle missing values.
    3. Standardize data formats.
    
    Args:
        raw_data (List[dict]): List of raw scraped data records.
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed data.
    """
    # Convert raw data to a DataFrame
    print("Converting raw data to a DataFrame...")
    df = pd.DataFrame(raw_data)

    # Step 1: Remove duplicates
    print("Removing duplicate records...")
    df = df.drop_duplicates()

    # Step 2: Handle missing values
    print("Handling missing values...")
    df = df.fillna({"price": "Unknown", "availability": "Unknown"})

    # Step 3: Standardize price field
    print("Standardizing price field...")
    def standardize_price(price):
        try:
            return float(price.replace("$", "").replace(",", "").strip())
        except ValueError:
            return None

    df['price'] = df['price'].apply(standardize_price)
    df = df.dropna(subset=['price'])  # Remove rows where price couldn't be standardized

    # Step 4: Strip whitespace from string columns
    print("Trimming whitespace from string fields...")
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.strip()

    print("Data cleaning completed.")
    return df


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"name": "Product A", "price": "$1,000", "availability": "In Stock"},
        {"name": "Product B", "price": "$500", "availability": "Out of Stock"},
        {"name": "Product A", "price": "$1,000", "availability": "In Stock"},  # Duplicate
        {"name": "Product C", "price": "Unknown", "availability": None},
    ]
    cleaned_data = clean_data(sample_data)
    print(cleaned_data)
