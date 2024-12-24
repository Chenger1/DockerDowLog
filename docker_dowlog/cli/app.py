from config import Config
from docker_dowlog.domain.scheduler import Scheduler
from docker_dowlog.domain.service import Docker
from docker_dowlog.domain.saver import get_saver

class App:
    def __init__(self):
        self._config = Config.build_config()
        self._scheduler = Scheduler(self._config)

    def start(self):
        job = self._scheduler.get_job(self._save)
        job.start()

    def _save(self):
        containers = Docker(self._config).get_logs()
        get_saver(self._config)(self._config, containers).save()
