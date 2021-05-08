import logging


class all_logs():

    def __init__(self, info_logs=None, warning_log=None, error_log=None):
        if info_logs is None: info_logs = []
        if warning_log is None: warning_log = []
        if error_log is None: error_log = []
        self.info_logs = info_logs
        self.warning_log = warning_log
        self.error_log = error_log

    def info_log(self, name, info_logs):
        logging.basicConfig(
            level=logging.INFO,
            filename="info.log",
            format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        )
        logger = logging.getLogger(name)
        logger = logging.LoggerAdapter(logger, {"app": info_logs})
        logger.info(info_logs)
        return True

    def warning_logs(self, name, warning_log):
        logging.basicConfig(
            level=logging.WARNING,
            filename="warning.log",
            format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        )
        logger = logging.getLogger(name)
        logger = logging.LoggerAdapter(logger, {"app": warning_log})
        logger.warning(warning_log)
        return True

    def error_logs(self, name, error_log):
        logging.basicConfig(
            level=logging.ERROR,
            filename="error.log",
            format="%(asctime)s - [%(levelname)s] - %(app)s - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        )
        logger = logging.getLogger(name)
        logger = logging.LoggerAdapter(logger, {"app": error_log})
        logger.error(error_log)
        return True