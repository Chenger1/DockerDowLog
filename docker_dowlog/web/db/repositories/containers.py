from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from docker_dowlog.web.db.models.containers import DockerContainers


class DockerContainersRepository(SQLAlchemyAsyncRepository[DockerContainers]):
    model_type = DockerContainers
