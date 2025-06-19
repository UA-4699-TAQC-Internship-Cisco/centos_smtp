import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from config.config import LOG_DIR, LOG_FILE_FORMAT, LOG_ENCODING, LOG_BACKUP_COUNT, LOG_LEVEL


def setup_logger():
    """
        Sets up a logger that writes log messages to a rotating log file. The log file is created daily
        with a timestamp in the filename. It also ensures that the log directory exists and is created if not.
        Returns:
            logging.Logger: A configured logger instance that logs messages to a rotating log file.
        """
    logger = logging.getLogger(__name__)
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    date_str = datetime.now().strftime(LOG_FILE_FORMAT)
    log_file = os.path.join(LOG_DIR, "{}.log".format(date_str))

    class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
        """
            A custom handler for rotating log files. This handler creates a new log file at midnight
            and uses a custom format for the rotated filenames.
            Methods:
            _get_rotated_filename(time): Creates the filename for the rotated log file based on the timestamp.
        """

        def __init__(self, *args, **kwargs):
            super(CustomTimedRotatingFileHandler, self).__init__(*args, **kwargs)

        def _get_rotated_filename(self, time):
            """
            Creates a filename for the rotated log file using a timestamp.
            Args:
                time (datetime): The timestamp used to generate the rotated log file name.
            Returns:
                str: The generated file name for the rotated log file.
            """
            return os.path.join(self.baseFilename, "{}.log".format(time.strftime(LOG_FILE_FORMAT)))

    handler = CustomTimedRotatingFileHandler(
        filename=log_file,
        when="midnight",
        interval=1,
        backupCount=LOG_BACKUP_COUNT,
        encoding=LOG_ENCODING,
    )
    handler.suffix = LOG_FILE_FORMAT

    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[handler],
    )

    return logger
