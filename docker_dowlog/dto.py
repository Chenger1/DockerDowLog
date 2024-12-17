from dataclasses import dataclass


@dataclass
class DockerLog:
    name: str
    log_text: str
