# Market-Trends-Web-Scraper
Built an automated web scraper to collect and analyze market data from e-commerce platforms.

## Overview
The **Market Trends Web Scraper** is a Python-based solution designed to extract, clean, analyze, and visualize market data from e-commerce platforms. This system scrapes product information such as pricing, availability, and competitor trends to help businesses make data-driven decisions regarding pricing strategies and inventory management. The scraper uses a combination of **BeautifulSoup** for static content and **Selenium** for dynamic content, along with **Pandas** for data processing and **Tableau** for visualization.

This project includes a modular pipeline for scraping, data wrangling, exploratory analysis, visualization, automation, and scheduled task execution.

---

## Key Features
- **Data Collection**: Scrapes product data (names, prices, availability, etc.) from e-commerce websites using BeautifulSoup and Selenium.
- **Data Cleaning**: Cleans and preprocesses scraped data, handling missing values, duplicates, and formatting issues.
- **Exploratory Data Analysis (EDA)**: Performs analysis on pricing trends, product categories, and competitor pricing strategies.
- **Visualization**: Generates visualizations for price trends, category distributions, and competitor comparisons.
- **Automation**: Automates the scraping process to update data periodically.
- **MongoDB Integration**: Stores cleaned data in MongoDB for scalable storage and retrieval.
- **Tableau Integration**: Prepares data for integration with Tableau for dynamic market trend reporting.

---

## Directory Structure
```
project/
│
├── main.py                     # Orchestrates the entire pipeline
├── scraper.py                  # Handles web scraping with BeautifulSoup and Selenium
├── data_cleaning.py            # Preprocesses and cleans raw scraped data
├── db_manager.py               # Manages MongoDB operations for storing and retrieving data
├── eda_analysis.py             # Performs Exploratory Data Analysis (EDA)
├── visualization.py            # Prepares data for Tableau visualization
├── scheduler.py                # Automates periodic scraping and data processing tasks
├── config.py                   # Stores reusable configurations and constants
├── utils.py                    # Provides helper functions for logging, error handling, etc.
├── README.md                   # Project documentation
```


# Modules

## 1. main.py
- Orchestrates the entire scraping, cleaning, storing, and visualization pipeline.
- Calls functions from `scraper.py`, `data_cleaning.py`, `db_manager.py`, and `visualization.py`.

## 2. scraper.py
- Handles web scraping of both static and dynamic content.
- Uses BeautifulSoup for static scraping and Selenium for dynamic content.

## 3. data_cleaning.py
- Preprocesses scraped data, removing duplicates, handling missing values, and standardizing formats.

## 4. db_manager.py
- Manages MongoDB database operations for storing and retrieving data.

## 5. eda_analysis.py
- Performs Exploratory Data Analysis (EDA) on pricing trends, popular product categories, and competitor strategies.

## 6. visualization.py
- Prepares and exports data for Tableau integration.
- Saves visualizations as CSV files for use in Tableau dashboards.

## 7. scheduler.py
- Automates the periodic execution of the entire pipeline using the `schedule` library.
- Ensures that data is scraped and processed regularly.

## 8. config.py
- Centralized configuration file for database credentials, URLs, scheduling times, and file paths.

## 9. utils.py
- Helper functions for logging, error handling, generating timestamped filenames, and pausing execution.

# Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com

