"""
config.py
---------
Centralized configuration for managing project parameters like database credentials,
API keys, file paths, and scheduling settings.

Author: Satej
"""

# Database Configuration
MONGO_URI = "mongodb://localhost:27017/"  # Update with your MongoDB URI
DB_NAME = "market_trends_db"
COLLECTION_NAME = "scraped_data"

# Scheduling Configuration
SCHEDULE_TIME = "12:00"  # Example: Daily schedule at 12:00 PM

# Scraping Configuration
STATIC_URL = "https://example-static-website.com/products"
DYNAMIC_URL = "https://example-dynamic-website.com/products"
SELENIUM_DRIVER_PATH = "/path/to/chromedriver"  # Replace with your Selenium driver path (e.g., "/Users/satej/chromedriver")

# Logging Configuration
LOG_FILE_PATH = "logs/scraper.log"  # Log file location for debugging

# File Export Paths
CLEANED_DATA_EXPORT_PATH = "satej_cleaned_data.csv"
SUMMARY_EXPORT_PATH = "satej_avg_price_by_category.csv"

# Tableau Integration
TABLEAU_PROJECT_NAME = "Market Trends Dashboard"
TABLEAU_DATA_SOURCE_PATH = CLEANED_DATA_EXPORT_PATH
