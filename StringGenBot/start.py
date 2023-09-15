from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""≭︰مرحبا بك صديقي {msg.from_user.mention},
≭︰انا بوت {me2},\n
≭︰بوت جديد يقوم باستخراج الجلسات
≭︰حدد نوع جلستك من الخيارات اسفل
≭︰البوت الاول من حيث الامان والاصدار \n
≭︰Sᴜᴘᴘᴏʀᴛ :- @NKINB
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="• بدء استخراج", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("• قناة التحديثات ⎙", url="https://t.me/NNINB"),
                    InlineKeyboardButton("• المطور 🛠", user_id=OWNER_ID)
                ],
                [
                    InlineKeyboardButton("• اضافة الى المجموعة", url="https://t.me/BtZkBot?startgroup=new")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
