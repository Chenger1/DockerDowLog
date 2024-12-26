from litestar.controller import Controller
from litestar.handlers import get
from litestar.response import Template

from docker_dowlog.web.controllers import urls


class ContainersController(Controller):
    @get(
        path=urls.LIST_CONTAINERS,
        summary="List all containers",
        name="list_containers",
    )
    async def list_containers(self,) -> Template:
        return Template(template_name='containers/list.html.jinja2')
