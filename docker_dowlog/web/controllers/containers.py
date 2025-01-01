from litestar.controller import Controller
from litestar.handlers import get
from litestar.response import Template
from litestar.di import Provide

from docker_dowlog.web.controllers import urls
from docker_dowlog.web.dependencies.containers import provide_containers_service
from docker_dowlog.web.services.containers import DockerContainersService


class ContainersController(Controller):
    @get(
        path=['/', urls.LIST_CONTAINERS],
        summary='List all containers',
        name='list_containers',
        dependencies={'containers_service': Provide(provide_containers_service)},
    )
    async def list_containers(self, containers_service: DockerContainersService) -> Template:
        containers_list = await containers_service.get_containers()
        return Template(template_name='containers/list.html.jinja2',
                        context={
                            'containers': containers_list,
                        })
