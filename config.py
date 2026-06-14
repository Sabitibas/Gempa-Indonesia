import os
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()

# Ambil token dan chat ID dari environment variables
TELEGRAM_TOKEN   = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Validasi
if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
    print("⚠️  WARNING: TELEGRAM_TOKEN atau TELEGRAM_CHAT_ID tidak ditemukan di environment variables!")
    print("Pastikan file .env sudah dibuat dengan isi:")
    print("TELEGRAM_TOKEN=your_token_here")
    print("TELEGRAM_CHAT_ID=your_chat_id_here")
