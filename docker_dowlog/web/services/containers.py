from typing import List

from asgiref.sync import sync_to_async
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from docker_dowlog.domain.service import Docker
from docker_dowlog.domain.dto import DockerContainer
from docker_dowlog.web.db.repositories.containers import DockerContainersRepository


class DockerContainersService(SQLAlchemyAsyncRepositoryService):
    repository_type = DockerContainersRepository

    async def get_containers(self) -> List[DockerContainer]:
        docker_containers = await sync_to_async(Docker().get_containers)()
        saved_containers = await self.list()
        data = []
        for container in docker_containers:
            last_updated = None
            saved = next((i for i in saved_containers if i.name == container.name), None)
            if saved:
                last_updated = saved.last_updated
            data.append(
                DockerContainer(
                    name=container.name,
                    last_updated=last_updated,
                )
            )
        return data
