def start_app():
    import os
    from loguru import logger

    logger.info('Starting Docker Downlog in WEB mode')

    os.environ.setdefault("LITESTAR_APP", "docker_dowlog.web.asgi:app")

    from litestar.__main__ import run_cli as litestar_cli
    litestar_cli()
