def start_app():
    from loguru import logger

    from docker_dowlog.cli.app import App
    logger.info('Starting Docker Downlog in CLI mode')

    app = App()
    app.start()
