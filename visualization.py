"""
visualization.py
-----------------
Module for preparing and exporting data for Tableau visualization.

Author: Satej
"""

import pandas as pd


def prepare_visualization(data):
    """
    Prepares data for Tableau visualization by exporting cleaned data and additional insights.
    
    Steps:
    1. Export cleaned data to a CSV file for Tableau integration.
    2. Generate summary tables (e.g., average price by category).
    
    Args:
        data (pd.DataFrame): Cleaned and preprocessed data.
    
    Returns:
        str: Path to the exported CSV file.
    """
    print("Preparing data for Tableau visualization...")

    # Export cleaned data to CSV
    cleaned_data_path = "satej_cleaned_data.csv"
    data.to_csv(cleaned_data_path, index=False)
    print(f"Cleaned data exported to {cleaned_data_path}.")

    # Generate a summary table: Average price by category
    if 'category' in data.columns:
        avg_price_by_category = data.groupby('category')['price'].mean().reset_index()
        avg_price_path = "satej_avg_price_by_category.csv"
        avg_price_by_category.to_csv(avg_price_path, index=False)
        print(f"Average price by category exported to {avg_price_path}.")
    else:
        print("No 'category' column available to generate summary tables.")

    return cleaned_data_path


# Example usage
if __name__ == "__main__":
    sample_data = pd.DataFrame([
        {"name": "Product A", "price": 1000.0, "category": "Electronics"},
        {"name": "Product B", "price": 500.0, "category": "Clothing"},
        {"name": "Product C", "price": 1200.0, "category": "Electronics"}
    ])
    visualization_file = prepare_visualization(sample_data)
    print(f"Data prepared for visualization: {visualization_file}")
