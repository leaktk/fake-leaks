# Metadata: label=Telegram bot tokens, type=api_key, provider=telegram, context=Python code, generator=secret_generator.py

from telegram import Bot
from telegram.ext import Updater

class TelegramConfig:
    # Telegram Bot Token (format: bot_id:hash)
    BOT_TOKEN = "1234567890:AAH5iJ6kL7mN8oP9qR0sT1uV2wX3yZ4aB5cD6eF7gH8iJ"

    # Production bot
    PROD_BOT_TOKEN = "9876543210:AAH1jK2lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK"

    # Test bot
    TEST_BOT_TOKEN = "5432109876:AAH7mN8oP9qR0sT1uV2wX3yZ4aB5cD6eF7gH8iJ9kL0mN"

    # Bot API URL (for custom bot API server)
    BOT_API_URL = "https://api.telegram.org/bot1234567890:AAH5iJ6kL7mN8oP9qR0sT1uV2wX3yZ4aB5cD6eF7gH8iJ"

def create_bot():
    return Bot(token=TelegramConfig.BOT_TOKEN)

def create_updater():
    return Updater(token=TelegramConfig.BOT_TOKEN, use_context=True)

# Webhook secret token (for validating webhook requests)
WEBHOOK_SECRET = "My_T3l3gr@m_W3bh00k_S3cr3t_2024"

# Store bot tokens in environment
import os
os.environ['TELEGRAM_BOT_TOKEN'] = '6789012345:AAH3oP4qR5sT6uV7wX8yZ9aB0cD1eF2gH3iJ4kL5mN6oP'
os.environ['TELEGRAM_CHAT_ID'] = '-1001234567890'
