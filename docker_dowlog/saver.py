import os
from abc import (
    ABC,
    abstractmethod
)
from typing import List
from datetime import datetime

from dto import DockerLog
from config import Config


class Saver(ABC):
    def __init__(self, config: Config, docker_logs: List[DockerLog]):
        self._config = config
        self._docker_logs = docker_logs

    @abstractmethod
    def save(self):
        raise NotImplementedError()


class FileSaver(Saver):
    _folder_path: str

    def _create_folder(self):
        path = self._config.PATH if self._config.PATH else os.getcwd()
        self._folder_path = os.path.join(path, 'logs')
        os.mkdir(self._folder_path)

    def _write_files(self):
        now = datetime.now()
        for log in self._docker_logs:
            filename = f'{log.name}_{now.strftime("%Y-%m-%d_%H-%M-%S")}.log'
            with open(os.path.join(self._folder_path, filename), 'w') as f:
                f.write(log.log_text)

    def save(self):
        self._create_folder()
        self._write_files()
