from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("25635928")
APP_HASH = os.environ.get("6e49a338bcf4c3406afdb0ce9a2892e1")
BOT_USERNAME = os.environ.get("@bbbbbbvndbot")
session = os.environ.get("1BJWap1sBu3SuUBASUs3kxyV7fXxt_MzuL3S6peX9jT5SBg7AWjaa5-976VlWLTjr0tqMbdOH-Nm-Qbk3a9to1KfAdI7KgVjODTEeZWx1XaGciVJdiiqbs1jdj6f5fSH9JgyLi_w9w63NNBCkrzvQZ7RlmHEncssxw5BYrfH72ILBdMuxaCbaSYFAjTDdvDks0MqVuJc9RxbUZFAIfc15MyrRZFOXvjqHsEK9zlH4mdifaeFNpIEG_UGpy0EwhnvjWrfT5q_nhtxwU9hA5XnHqy34atxelL5T5yPXNh8ZKqYC_6S7pydaLaTN-DlVMuvKsOaYN4O_hf_WLfSpIV-ildr15Gm6Fw0=")
SESSION = os.environ.get("1BJWap1sBu3SuUBASUs3kxyV7fXxt_MzuL3S6peX9jT5SBg7AWjaa5-976VlWLTjr0tqMbdOH-Nm-Qbk3a9to1KfAdI7KgVjODTEeZWx1XaGciVJdiiqbs1jdj6f5fSH9JgyLi_w9w63NNBCkrzvQZ7RlmHEncssxw5BYrfH72ILBdMuxaCbaSYFAjTDdvDks0MqVuJc9RxbUZFAIfc15MyrRZFOXvjqHsEK9zlH4mdifaeFNpIEG_UGpy0EwhnvjWrfT5q_nhtxwU9hA5XnHqy34atxelL5T5yPXNh8ZKqYC_6S7pydaLaTN-DlVMuvKsOaYN4O_hf_WLfSpIV-ildr15Gm6Fw0=")
token = os.environ.get(""7512172162:AAHo_Qq1OIsV5b1WkScWDWreyIonNblN9lM)
sfox = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
