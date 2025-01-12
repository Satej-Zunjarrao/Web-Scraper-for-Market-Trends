"""
utils.py
--------
Utility functions for common operations across the project.
Provides helper functions like logging, error handling, and others.

Author: Satej
"""

import logging
import os
import time


def setup_logger(log_file_path="logs/scraper.log"):
    """
    Sets up the logger for the project. Ensures that logs are written to a specified file.
    
    Args:
        log_file_path (str): The path where log messages will be saved.
    
    Returns:
        logging.Logger: Configured logger object.
    """
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # You can set this to DEBUG for more detailed logs
    
    # Create file handler to store logs in a file
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    
    # Create a console handler to print logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


def handle_error(exception, logger=None):
    """
    Handles exceptions by logging the error message and printing it to the console.
    
    Args:
        exception (Exception): The exception to be logged and printed.
        logger (logging.Logger, optional): Logger to record the error. If None, no log is written.
    """
    error_message = f"Error occurred: {str(exception)}"
    print(error_message)
    
    if logger:
        logger.error(error_message)


def wait_for(seconds):
    """
    Pauses the execution for a specified duration (in seconds).
    
    Args:
        seconds (int): Duration to pause the execution in seconds.
    """
    print(f"Waiting for {seconds} seconds...")
    time.sleep(seconds)


def create_timestamp_filename(base_filename="output"):
    """
    Generates a timestamped filename to ensure unique file names.
    
    Args:
        base_filename (str): The base name for the file (default is "output").
    
    Returns:
        str: A unique file name with the current timestamp.
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"{base_filename}_{timestamp}.csv"


# Example usage
if __name__ == "__main__":
    logger = setup_logger("logs/scraper.log")
    
    try:
        # Simulating a task
        wait_for(3)
        
        # Generating a timestamped filename
        filename = create_timestamp_filename("scraped_data")
        print(f"Generated filename: {filename}")
        
    except Exception as e:
        handle_error(e, logger)
