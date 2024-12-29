def create_app():
    from pathlib import Path

    from litestar import Litestar
    from litestar.static_files import create_static_files_router
    from litestar.contrib.jinja import JinjaTemplateEngine
    from litestar.template.config import TemplateConfig
    from litestar.plugins.htmx import HTMXPlugin

    from docker_dowlog.web.routers import routers

    assets_dir = Path(__file__).parent / 'assets'

    def on_startup():
        assets_dir.mkdir(exist_ok=True)

    return Litestar(
        route_handlers=routers + [
            create_static_files_router(path='/static', directories=[assets_dir], name='assets'),
        ],
        on_startup=[on_startup],
        template_config=TemplateConfig(
            directory=Path(__file__).parent / 'templates',
            engine=JinjaTemplateEngine
        ),
        plugins=[HTMXPlugin()],
        debug=True
    )


app = create_app()
