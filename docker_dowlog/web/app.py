from litestar import Litestar, get


@get('/')
def index() -> str:
    return 'Hello'


app = Litestar([index])
