import os

# LOGGER SETUP

LOG_DIR = os.getenv("LOG_DIR", "logs")
LOG_FILE_FORMAT = "%d-%m-%Y"
LOG_ENCODING = "utf-8"
LOG_BACKUP_COUNT = 0
LOG_LEVEL = "INFO"
