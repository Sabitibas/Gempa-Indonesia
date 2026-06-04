import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def kirim_notif_telegram(gempa):
    pesan = (
        "Warning Gempa Besar!\n\n"
        "Wilayah  : " + gempa["Wilayah"] + "\n"
        "Magnitudo: " + gempa["Magnitude"] + " SR\n"
        "Kedalaman: " + gempa["Kedalaman"] + "\n"
        "Waktu    : " + gempa["Tanggal"] + " - " + gempa["Jam"] + "\n"
        "Potensi  : " + gempa["Potensi"]
    )
    url = "https://api.telegram.org/bot" + TELEGRAM_TOKEN + "/sendMessage"
    try:
        r = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": pesan}, timeout=10)
        if r.status_code == 200:
            print("Notifikasi berhasil dikirim!")
        else:
            print("Gagal:", r.text)
    except Exception as e:
        print("Error:", e)
