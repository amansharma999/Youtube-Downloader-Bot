from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hello 😊 <b>{message.from_user.first_name}</b>\nI can download yt videos for you\nJust send me any YouTube link."
    await message.reply_text(welcomed)#, reply_markup=joinButton)
    raise StopPropagation
