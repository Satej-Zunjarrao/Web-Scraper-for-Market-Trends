"""
eda_analysis.py
---------------
Module for performing Exploratory Data Analysis (EDA) on the cleaned data.

Author: Satej
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda(data):
    """
    Performs Exploratory Data Analysis on the cleaned data.
    
    Steps:
    1. Generate summary statistics.
    2. Identify price trends over time.
    3. Analyze popular product categories.
    4. Visualize competitor pricing strategies.
    
    Args:
        data (pd.DataFrame): Cleaned data containing columns like 'name', 'price', 'availability'.
    
    Returns:
        dict: EDA results including insights and visualized plots.
    """
    print("Performing EDA...")

    # Step 1: Summary statistics
    print("Generating summary statistics...")
    summary_stats = data.describe(include="all")

    # Step 2: Price trends
    print("Analyzing price trends...")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['price'], bins=30, kde=True)
    plt.title("Distribution of Product Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.savefig("eda_price_distribution.png")  # Save the plot
    plt.close()

    # Step 3: Popular product categories
    print("Identifying popular product categories...")
    if 'category' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(y=data['category'], order=data['category'].value_counts().index[:10])
        plt.title("Top 10 Product Categories")
        plt.xlabel("Count")
        plt.ylabel("Category")
        plt.savefig("eda_top_categories.png")  # Save the plot
        plt.close()
    else:
        print("No 'category' column available in the data.")

    # Step 4: Competitor pricing strategies
    print("Analyzing competitor pricing strategies...")
    if 'competitor' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='competitor', y='price', data=data)
        plt.title("Competitor Pricing Strategies")
        plt.xlabel("Competitor")
        plt.ylabel("Price")
        plt.savefig("eda_competitor_pricing.png")  # Save the plot
        plt.close()
    else:
        print("No 'competitor' column available in the data.")

    print("EDA completed.")
    return {
        "summary_statistics": summary_stats,
        "plots": [
            "eda_price_distribution.png",
            "eda_top_categories.png",
            "eda_competitor_pricing.png"
        ]
    }


# Example usage
if __name__ == "__main__":
    sample_data = pd.DataFrame([
        {"name": "Product A", "price": 1000.0, "category": "Electronics", "competitor": "Site A"},
        {"name": "Product B", "price": 500.0, "category": "Clothing", "competitor": "Site B"},
        {"name": "Product C", "price": 1200.0, "category": "Electronics", "competitor": "Site A"}
    ])
    eda_results = perform_eda(sample_data)
    print("Summary Statistics:\n", eda_results["summary_statistics"])
    print("Plots saved:", eda_results["plots"])
