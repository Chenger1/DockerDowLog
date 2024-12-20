from config import Config
from scheduler import Scheduler
from service import Docker
from saver import get_saver

class Main:
    def __init__(self):
        self._config = Config.build_config()
        self._scheduler = Scheduler(self._config)

    def start(self):
        job = self._scheduler.get_job(self._save)
        job.start()

    def _save(self):
        containers = Docker(self._config).get_logs()
        get_saver(self._config)(self._config, containers).save()


if __name__ == "__main__":
    main = Main()
    main.start()
