import os
from Avatar import pbot as Client

@Client.on_message(filters.command("a"))
async def start_msg(client, message):
	await message.reply_text(
		f"😂",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🙂", callback_data=f"🙂"),
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "🙂" in cb_data:
		await update.message.edit_text("🙃",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌺", callback_data=f"🌺"),
				]]
			))
	elif "🌺" in cb_data:
		await update.message.edit_text("Language: Python\nFramework: Pyrogram\nEngine: YTDL\nCorded By: @Anjana_Ma\n\nPowered by @Harp_Tech",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌖", callback_data=f"🌖"),
				]]
			))
	elif "🌖" in cb_data:
		await update.message.edit_text(f"🥲",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🙂", callback_data=f"🙂"),
					InlineKeyboardButton("close", callback_data=f"about")
				]]
			))
