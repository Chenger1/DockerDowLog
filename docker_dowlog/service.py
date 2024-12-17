from typing import List

import docker
from docker.models.containers import Container

from config import Config
from dto import DockerLog


class Docker:
    def __init__(self, config: Config):
        self._config = config
        self._docker_client = docker.from_env()

    def _get_containers(self) -> List[Container]:
        return [
            container for container in self._docker_client.containers.list()
            if container.name in self._config.DOCKER_CONTAINERS
        ]

    def get_logs(self) -> List[DockerLog]:
        return [
            DockerLog(
                name=container.name,
                log_text=container.logs().decode('utf-8'),
            ) for container in self._get_containers()
        ]
