import time
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def long_running_task():
    """
    Simulates a long-running task with periodic logging.
    Runs for approximately 5 minutes.
    """
    start_time = time.time()
    max_runtime = 5 * 60  # 5 minutes in seconds
    
    try:
        iteration = 0
        while time.time() - start_time < max_runtime:
            iteration += 1
            logger.info(f"Running iteration {iteration}")
            
            # Simulate some work
            time.sleep(10)  # Sleep for 10 seconds between iterations
            
            # Optional: Add some meaningful work here
            # For example, you could:
            # - Check a condition
            # - Perform a calculation
            # - Make an API call
            # - Process some data
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
    
    logger.info("Task completed within 5-minute time limit")

def main():
    """
    Main function to run the script
    """
    logger.info("Starting script")
    long_running_task()
    logger.info("Script finished")

if __name__ == "__main__":
    main()
