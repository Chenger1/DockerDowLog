def create_app():
    from litestar import Litestar

    from docker_dowlog.web.routers import routers


    return Litestar(
        route_handlers=routers
    )


app = create_app()
