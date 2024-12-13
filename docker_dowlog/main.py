from config import Config
from scheduler import Scheduler

class Main:
    def __init__(self):
        self._config = Config.build_config()
        self._scheduler = Scheduler(self._config)


if __name__ == "__main__":
    def f():
        print("MY task")

    main = Main()
    job = main._scheduler.get_job(f)
    job.start()
