import logging
import os


def setup_logger():

    # CREATE LOGS FOLDER

    if not os.path.exists(
        "logs"
    ):

        os.makedirs(
            "logs"
        )

    # LOGGER CONFIGURATION

    logging.basicConfig(

        filename="logs/test.log",

        level=logging.INFO,

        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    return logging.getLogger()