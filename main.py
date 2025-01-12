"""
main.py
---------
Entry point for the web scraping project. Orchestrates the scraping, data cleaning, 
database storage, and analysis workflows.

Author: Satej
"""

import scraper
import data_cleaning
import db_manager
import eda_analysis
import visualization
import scheduler

def main():
    """
    Main function that coordinates the entire pipeline.
    Steps:
    1. Scrape data from static and dynamic websites.
    2. Clean and preprocess the scraped data.
    3. Store cleaned data in MongoDB.
    4. Perform EDA to identify trends.
    5. Visualize data using Tableau (integration preparation).
    6. Schedule periodic scraping and processing tasks.
    """
    # Step 1: Scrape data from websites
    print("Starting the scraping process...")
    raw_data = scraper.scrape_data()
    print(f"Scraping completed. {len(raw_data)} records retrieved.")

    # Step 2: Clean the scraped data
    print("Cleaning and preprocessing the scraped data...")
    cleaned_data = data_cleaning.clean_data(raw_data)
    print("Data cleaning completed.")

    # Step 3: Store the data in MongoDB
    print("Storing cleaned data in MongoDB...")
    db_manager.store_data(cleaned_data)
    print("Data storage completed.")

    # Step 4: Perform Exploratory Data Analysis
    print("Performing Exploratory Data Analysis...")
    eda_results = eda_analysis.perform_eda(cleaned_data)
    print("EDA completed.")

    # Step 5: Prepare data for Tableau visualization
    print("Preparing data for Tableau integration...")
    visualization.prepare_visualization(eda_results)
    print("Data preparation for visualization completed.")

    # Step 6: Schedule automation tasks
    print("Scheduling periodic scraping and processing tasks...")
    scheduler.schedule_tasks()
    print("Scheduling completed. Pipeline is fully operational.")

if __name__ == "__main__":
    main()
