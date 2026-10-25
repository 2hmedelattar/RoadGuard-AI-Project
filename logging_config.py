import logging

def configure_logging() -> None:

    logger = logging.getLogger("roadguard")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # System Handler
    system_handler = logging.FileHandler("logs/system.log")
    system_handler.setLevel(logging.INFO)
    system_handler.setFormatter(formatter)

    # Error Handler
    error_handler = logging.FileHandler("logs/errors.log")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(system_handler)
    logger.addHandler(error_handler)