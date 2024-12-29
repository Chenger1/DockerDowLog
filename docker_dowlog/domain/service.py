from typing import Optional

import docker
from docker.models.containers import Container

from docker_dowlog.domain.dto import DockerLog


class Docker:
    def __init__(self):
        self._docker_client = docker.from_env()

    def get_containers(self, containers_names: Optional[list[str]] = None) -> list[Container]:
        containers = self._docker_client.containers.list(all=True)
        if containers_names:
            return [container for container in containers if container.name in containers_names]
        return containers

    def get_logs(self, containers_names: Optional[list[str]] = None) -> list[DockerLog]:
        return [
            DockerLog(
                name=container.name,
                log_text=container.logs().decode('utf-8'),
            ) for container in self.get_containers(containers_names)
        ]
