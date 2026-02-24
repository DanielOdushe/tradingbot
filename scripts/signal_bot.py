import os
import yaml
import asyncio
from telegram import Bot

# Load config
cfg_path = "config.yaml" if os.path.exists("config.yaml") else "config.template.yaml"
with open(cfg_path, "r") as f:
    cfg = yaml.safe_load(f)

### bot_token = os.getenv('TELEGRAM_BOT_TOKEN', cfg['telegram'].get('bot_token', ''))
### chat_id = os.getenv('TELEGRAM_CHAT_ID', cfg['telegram'].get('chat_id', ''))

bot_token = os.environ['TELEGRAM_BOT_TOKEN']   # will raise KeyError if missing (good for debugging)
chat_id = os.environ['TELEGRAM_CHAT_ID']

if not bot_token or not chat_id:
    raise ValueError("Telegram bot token or chat ID not found!")

bot = Bot(token=bot_token)

# Async wrapper
async def send_test_message():
    try:
        await bot.send_message(chat_id=chat_id, text="✅ Test message from Signal Bot is successful!")
        print("Telegram test message sent successfully.")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

# Run the async function
asyncio.run(send_test_message())
