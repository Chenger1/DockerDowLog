from datetime import datetime

from litestar.contrib.sqlalchemy.base import BigIntBase
from sqlalchemy.orm import Mapped


class DockerContainers(BigIntBase):
    __tablename__ = 'docker_containers'

    name: Mapped[str]
    last_updated: Mapped[datetime]
