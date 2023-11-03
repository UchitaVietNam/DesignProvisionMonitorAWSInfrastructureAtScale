import os
import logging

# Set up the logging configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log an info message
    response = "{} from Lambda!".format(os.environ['greeting'])
    logger.info(response)
    return response
