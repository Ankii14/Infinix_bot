from telethon import TelegramClient
import logging
import time


#openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6270188801:AAHLd7i64-erQKXRZ4BTVVHM2g61HFEAnTo"

bot=TelegramClient("a", api_id, api_hash).start(bot_token=bot_token)
