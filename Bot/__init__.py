#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys, os
import logging
from logging.handlers import RotatingFileHandler


API_HASH = '90dd95178a8d13a69bfdbc7da68d23a4'
APP_ID = 2919867
TG_BOT_TOKEN = '5049507559:AAETCRZ2YM2VR9fj8DuNIfqUEnxp1HSavoc'
TG_BOT_WORKERS = 4
FORCE_SUB_CHANNEL = -1001611440971
CHANNEL_ID = -1001705686821
ADMINS = set(int(x) for x in  [5073412581,1392459364,1242979521,1337239251,2043468602,1791795037])
DISABLE_CHANNEL_BUTTON = True
DB_URI = "postgres://qfokcisu:w7kIyJJ4VmBuyCHAMaG-R32ifb-_2HE4@castor.db.elephantsql.com/qfokcisu"
FORCE_MSG = """
JOIN OUR CHANNEL TO GET ANIMES 😌 """
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

Pbot = Client("bot", api_hash=API_HASH,api_id=APP_ID,workers=TG_BOT_WORKERS,bot_token=TG_BOT_TOKEN)

async def start(Pbot):
    await Pbot.start()
    usr_bot_me = await Pbot.get_me()

    if FORCE_SUB_CHANNEL:
        try:
            link = await Pbot.export_chat_invite_link(FORCE_SUB_CHANNEL)
            Pbot.invitelink = link
        except Exception as a:
            LOGGER(__name__).warning(a)
            LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
            LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
            LOGGER(__name__).info("\nBot Stopped")
            sys.exit()
    try:
        db_channel = await Pbot.get_chat(CHANNEL_ID)
        Pbot.db_channel = db_channel
        test = await Pbot.send_message(chat_id = db_channel.id, text = "Test Message")
        await test.delete()
    except Exception as e:
        LOGGER(__name__).warning(e)
        LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
        LOGGER(__name__).info("\nBot Stopped.")
        sys.exit()

        Pbot.set_parse_mode("html")
        LOGGER(__name__).info(f"Bot Running..!\n\nCreated by Villians\nhttps://t.me/Villians_association")
        Pbot.username = usr_bot_me.username

    async def stop(Pbot, *args):
        await Pbot.stop()
        LOGGER(__name__).info("Bot stopped.")
