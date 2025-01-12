"""
scraper.py
----------
Module for scraping static and dynamic web content using BeautifulSoup and Selenium.

Author: Satej
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

def scrape_data():
    """
    Scrapes data from both static and dynamic web pages.
    Returns:
        List[dict]: A list of dictionaries containing scraped data.
    """
    scraped_data = []

    # Static scraping with BeautifulSoup
    print("Scraping static content...")
    static_url = "https://example-static-website.com/products"
    response = requests.get(static_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', class_='product-item')

        for product in products:
            data = {
                "name": product.find('h2', class_='product-name').text.strip(),
                "price": product.find('span', class_='price').text.strip(),
                "availability": product.find('span', class_='availability').text.strip(),
            }
            scraped_data.append(data)
    else:
        print(f"Failed to scrape static content. Status code: {response.status_code}")

    # Dynamic scraping with Selenium
    print("Scraping dynamic content...")
    dynamic_url = "https://example-dynamic-website.com/products"
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    driver.get(dynamic_url)
    time.sleep(5)  # Allow the page to load

    try:
        product_elements = driver.find_elements(By.CLASS_NAME, "product-item")
        for element in product_elements:
            data = {
                "name": element.find_element(By.CLASS_NAME, "product-name").text.strip(),
                "price": element.find_element(By.CLASS_NAME, "price").text.strip(),
                "availability": element.find_element(By.CLASS_NAME, "availability").text.strip(),
            }
            scraped_data.append(data)
    except Exception as e:
        print(f"Error during dynamic scraping: {e}")
    finally:
        driver.quit()

    return scraped_data

# Example usage
if __name__ == "__main__":
    data = scrape_data()
    print(f"Scraped {len(data)} items.")
    print(data)
