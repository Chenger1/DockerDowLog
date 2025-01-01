from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class DockerLog:
    name: str
    log_text: str


@dataclass(frozen=True)
class DockerContainer:
    name: str
    last_updated: Optional[datetime] = None
