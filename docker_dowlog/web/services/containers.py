from typing import List

from asgiref.sync import sync_to_async

from docker_dowlog.domain.service import Docker
from docker_dowlog.domain.dto import DockerContainer


class DockerService:
    async def get_list_of_containers(self) -> List[DockerContainer]:
        containers = await sync_to_async(Docker().get_containers)()
        return [
            DockerContainer(
                name=container.name
            ) for container in containers
        ]
