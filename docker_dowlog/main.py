from config import Config
from scheduler import Scheduler
from service import Docker
from saver import FileSaver

class Main:
    def __init__(self):
        self._config = Config.build_config()
        self._scheduler = Scheduler(self._config)

    def save(self):
        containers = Docker(self._config).get_logs()
        FileSaver(self._config, containers).save()


if __name__ == "__main__":
    def f():
        print("MY task")

    main = Main()
    main.save()
