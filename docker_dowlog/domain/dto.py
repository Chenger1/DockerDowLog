from dataclasses import dataclass


@dataclass(frozen=True)
class DockerLog:
    name: str
    log_text: str


@dataclass(frozen=True)
class DockerContainer:
    name: str
