"""
db_manager.py
--------------
Module for managing database operations with MongoDB.

Author: Satej
"""

from pymongo import MongoClient


def connect_to_mongo():
    """
    Establishes a connection to the MongoDB database.
    
    Returns:
        pymongo.database.Database: MongoDB database object.
    """
    print("Connecting to MongoDB...")
    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI if required
    db = client["market_trends_db"]  # Database name
    print("Connected to MongoDB.")
    return db


def store_data(cleaned_data):
    """
    Stores cleaned data into the MongoDB collection.
    
    Args:
        cleaned_data (pd.DataFrame): Cleaned and preprocessed data.
    """
    print("Storing data into MongoDB...")
    db = connect_to_mongo()
    collection = db["scraped_data"]  # Collection name

    # Convert DataFrame to a list of dictionaries for MongoDB insertion
    data_to_insert = cleaned_data.to_dict(orient="records")

    # Insert data into the collection
    collection.insert_many(data_to_insert)
    print("Data successfully stored in MongoDB.")


def retrieve_data():
    """
    Retrieves all records from the MongoDB collection.
    
    Returns:
        List[dict]: List of records retrieved from the database.
    """
    print("Retrieving data from MongoDB...")
    db = connect_to_mongo()
    collection = db["scraped_data"]
    data = list(collection.find())
    print(f"Retrieved {len(data)} records.")
    return data


# Example usage
if __name__ == "__main__":
    # Sample data for testing
    import pandas as pd

    sample_cleaned_data = pd.DataFrame([
        {"name": "Product A", "price": 1000.0, "availability": "In Stock"},
        {"name": "Product B", "price": 500.0, "availability": "Out of Stock"}
    ])
    
    store_data(sample_cleaned_data)
    retrieved_data = retrieve_data()
    print(retrieved_data)
