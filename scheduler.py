"""
scheduler.py
------------
Module for automating periodic scraping and data processing tasks.

Author: Satej
"""

import schedule
import time
import main


def job():
    """
    Job to execute the full pipeline.
    Calls the `main.py` script to handle scraping, cleaning, storing, and visualizing data.
    """
    print("Starting the scheduled job...")
    main.main()
    print("Scheduled job completed.")


def schedule_tasks():
    """
    Schedules tasks to automate the pipeline at regular intervals.
    Example:
    - Run the job every day at 12:00 PM.
    """
    print("Scheduling tasks...")
    schedule.every().day.at("12:00").do(job)  # Schedule the job to run daily at 12 PM

    # Keep the scheduler running
    print("Scheduler is running. Press Ctrl+C to stop.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # Sleep for 1 second between checks
    except KeyboardInterrupt:
        print("Scheduler stopped.")


# Example usage
if __name__ == "__main__":
    schedule_tasks()
