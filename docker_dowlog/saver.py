import os
from abc import (
    ABC,
    abstractmethod
)
from typing import (
    List,
    Type
)
from datetime import datetime

from aiogram import Bot
from aiogram.types import BufferedInputFile
from asgiref.sync import async_to_sync
from loguru import logger

from dto import DockerLog
from config import Config


class Saver(ABC):
    def __init__(self, config: Config, docker_logs: List[DockerLog]):
        self._config = config
        self._docker_logs = docker_logs

    @abstractmethod
    def save(self):
        raise NotImplementedError()


class FileSaver(Saver):
    _folder_path: str

    def _create_folder(self):
        path = self._config.PATH if self._config.PATH else os.getcwd()
        self._folder_path = os.path.join(path, 'logs')
        try:
            os.mkdir(self._folder_path)
        except FileExistsError:
            return

    def _write_files(self):
        now = datetime.now()
        for log in self._docker_logs:
            filename = f'{log.name}_{now.strftime("%Y-%m-%d_%H-%M-%S")}.log'
            with open(os.path.join(self._folder_path, filename), 'w') as f:
                f.write(log.log_text)

    def save(self):
        logger.info('Save logs on disk')
        self._create_folder()
        self._write_files()


class TelegramSaver(Saver):
    def __init__(self, config: Config, docker_logs: List[DockerLog]):
        super().__init__(config, docker_logs)
        self._bot = Bot(token=config.TELEGRAM_BOT_API_KEY)
        assert config.TELEGRAM_CHAT_ID is not None, 'If you want to use Telegram, provide chat it'

    def _prepare_file(self) -> List[BufferedInputFile]:
        now = datetime.now()
        files = []
        for log in self._docker_logs:
            filename = f'{log.name}_{now.strftime("%Y-%m-%d_%H-%M-%S")}.log'
            files.append(BufferedInputFile(log.log_text.encode('utf-8'), filename=filename))
        return files

    async def _send_message(self, file: BufferedInputFile):
        await self._bot.send_document(chat_id=self._config.TELEGRAM_CHAT_ID, document=file)
        await self._bot.session.close()

    def save(self):
        logger.info('Send logs to telegram')
        for file in self._prepare_file():
            async_to_sync(self._send_message)(file)


def get_saver(config: Config) -> Type[Saver]:
    if config.TELEGRAM_BOT_API_KEY is not None:
        return TelegramSaver
    return FileSaver
