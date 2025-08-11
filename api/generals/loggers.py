import logging


class AuraTestLogger:

    @staticmethod
    def create_logger(logger_name: str = "Aura test") -> logging.Logger:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("\n%(message)s\n")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        return logger
