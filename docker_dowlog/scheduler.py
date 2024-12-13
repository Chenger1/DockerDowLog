import time
from abc import (
    ABC,
    abstractmethod
)
from typing import Callable

import schedule

from config import Config
from constants import SCHEDULE_TIME_FORMAT


class ScheduledJob:
    def __init__(self, function: Callable):
        self._function = function

    def start(self):
        return self._function()


class BaseScheduler(ABC):
    def __init__(self, config: Config):
        self._config = config

    @abstractmethod
    def get_job(self, task: Callable) -> ScheduledJob:
        raise NotImplementedError


class Scheduler(BaseScheduler):
    @staticmethod
    def _wrapper():
        while True:
            schedule.run_pending()
            time.sleep(1)

    def _build(self, task: Callable) -> schedule.Job:
        return schedule.every().day.at(self._config.SCHEDULE.strftime(SCHEDULE_TIME_FORMAT)).do(task)

    def get_job(self, task: Callable) -> ScheduledJob:
        self._build(task)
        return ScheduledJob(self._wrapper)
