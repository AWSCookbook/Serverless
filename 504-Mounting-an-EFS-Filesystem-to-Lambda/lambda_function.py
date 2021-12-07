import sys
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    try:
        os.system("touch /mnt/efs/awscookbook1.txt")
        os.system("touch /mnt/efs/awscookbook2.txt")
        os.system("touch /mnt/efs/awscookbook3.txt")
        for root, dirs, files in os.walk("/mnt/efs/"):
            for filename in files:
                print(filename)
        logger.info("SUCCESS: Connected to EFS via /mnt/efs/ and put 3 files!")
        return("SUCCESS: Connected to EFS via /mnt/efs/ and put 3 files!")
    except:
        logger.error("ERROR: Could not connect to EFS")
        return("ERROR: Could not connect to EFS")
