from litestar.controller import Controller
from litestar.handlers import get
from litestar.response import Template

from docker_dowlog.web.controllers import urls
from docker_dowlog.web.services.containers import DockerService


class ContainersController(Controller):
    @get(
        path=['/', urls.LIST_CONTAINERS],
        summary="List all containers",
        name="list_containers",
    )
    async def list_containers(self) -> Template:
        containers_list = await DockerService().get_list_of_containers()
        return Template(template_name='containers/list.html.jinja2',
                        context={
                            'containers': containers_list,
                        })
