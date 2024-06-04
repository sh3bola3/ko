import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f5902c94fdd47b5d012ee.jpg",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "َٰ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍ𝙀 َٰ𝘼ُ𝙑َٰ𝘼ٍ𝙏َٰ𝘼ٓ𝙍", url=f"https://t.me/source_av"),
                    InlineKeyboardButton(
                        "َٰ𝙎ُِ𝙊ِّ𝙐ٓ𝙍ٍّ𝘾ٍ𝙀 َٰ𝘼ُ𝙑َٰ𝘼ٍ𝙏َٰ𝘼ٓ𝙍", url=f"https://t.me/source_av"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕", url=f"https://t.me/K_IN_GO"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕 ", url=f"https://t.me/K_IN_GO"),
                ],[
                    InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),   
            ]
        ]
         ),
     )
  
