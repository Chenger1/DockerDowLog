from litestar.controller import Controller
from litestar.handlers import get

from docker_dowlog.web.controllers import urls


class ContainersController(Controller):
    @get(
        path=urls.LIST_CONTAINERS,
        summary="List all containers",
    )
    async def list_containers(self) -> str:
        return "Hello World"
