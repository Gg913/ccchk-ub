import os
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)
LOGS = logging.getLogger(__name__)

ENV = bool(os.getenv('ENV', True))
API_ID = int(os.getenv('API_ID', True))
API_HASH = os.getenv('API_HASH', True)
URL = os.getenv('URL', True)
DUMP_ID = int(os.getenv('DUMP_ID', True))
STRING_SESSION = os.getenv('STRING_SESSION', True)

Ubot = TelegramClient(StringSession(STRING_SESSION),
                      API_ID,
                      API_HASH,
                      auto_reconnect=False,
                      lang_code='en')
