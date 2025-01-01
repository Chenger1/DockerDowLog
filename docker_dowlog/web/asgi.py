def create_app():
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    from litestar import Litestar
    from litestar.static_files import create_static_files_router
    from litestar.contrib.jinja import JinjaTemplateEngine
    from litestar.template.config import TemplateConfig
    from litestar.plugins.htmx import HTMXPlugin
    from litestar.contrib.sqlalchemy.plugins import (
        SQLAlchemyPlugin,
        AsyncSessionConfig,
        SQLAlchemyAsyncConfig
    )
    from advanced_alchemy.config import AlembicAsyncConfig

    from docker_dowlog.web.routers import routers

    load_dotenv()

    assets_dir = Path(__file__).parent / 'assets'

    session_config = AsyncSessionConfig(expire_on_commit=False)
    sqlalchemy_config = SQLAlchemyAsyncConfig(
        connection_string=f'postgresql+asyncpg://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}',
        session_config=session_config,
        create_all=True,
        alembic_config=AlembicAsyncConfig(
            script_location='./web/db/migrations',
            script_config='./web/db/alembic.ini',
        )
    )

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
        plugins=[HTMXPlugin(), SQLAlchemyPlugin(config=sqlalchemy_config)],
        debug=True
    )


app = create_app()
