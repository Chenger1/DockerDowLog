import os
from typing import List
from datetime import datetime

from constants import SCHEDULE_TIME_FORMAT


class Config:
    def __init__(self):
        self.DOCKER_CONTAINERS: List[str] = self._get_containers_names()
        self.SCHEDULE: datetime = self._parse_schedule_time()

    @classmethod
    def build_config(cls) -> 'Config':
        return cls()

    def _get_containers_names(self) -> List[str]:
        try:
            return os.environ['DOCKER_CONTAINERS'].split(',')
        except KeyError:
            raise KeyError('DOCKER_CONTAINERS environment variable not set')

    def _get_common_param(self, param_name: str) -> str:
        try:
            return os.environ[param_name]
        except KeyError:
            raise KeyError(f'{param_name} environment variable not set')

    def _parse_schedule_time(self) -> datetime:
        param = self._get_common_param('DOWNLOAD_LOG_SCHEDULE')

        try:
            return datetime.strptime(param, SCHEDULE_TIME_FORMAT)
        except ValueError:
            raise ValueError(f'Schedule only support format: {SCHEDULE_TIME_FORMAT}. {param} - incorrect format')