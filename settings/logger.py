import logging
from os import getcwd, path
from settings.manager import manager


class Logger:

    def __init__(self, name: str, level=logging.INFO):
        self.log_name = f'{manager.test_start}_{manager.test_name}.log'
        self.log_path = path.join(getcwd(), 'results', self.log_name)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            handler = logging.FileHandler(self.log_path)
            stream_handler = logging.StreamHandler()
            formatter = logging.Formatter(
                f'{"=" * 50}\n%(asctime)s - %(name)s - %(levelname)s\n%(message)s'
            )
            handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.addHandler(stream_handler)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)
