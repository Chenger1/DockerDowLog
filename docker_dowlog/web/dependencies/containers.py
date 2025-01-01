from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from docker_dowlog.web.services.containers import DockerContainersService


async def provide_containers_service(db_session: AsyncSession) -> AsyncGenerator[DockerContainersService, None]:
    async with DockerContainersService.new(db_session) as service:
        yield service
