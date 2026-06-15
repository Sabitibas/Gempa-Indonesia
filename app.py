from flask import Flask, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from notifikasi import kirim_notif_telegram
import atexit

app = Flask(__name__)

gempa_terakhir_notif = None

# ✅ Format teks Potensi jadi lebih jelas dan spesifik
def format_potensi(teks):
    if not teks:
        return {"teks": "Data tidak tersedia", "tipe": "normal"}
    t = teks.lower()
    if "tidak berpotensi tsunami" in t:
        return {"teks": "Tidak berpotensi menimbulkan tsunami", "tipe": "aman"}
    elif "berpotensi tsunami" in t:
        return {"teks": "BERPOTENSI TSUNAMI — Waspada dan segera menjauh dari pantai", "tipe": "bahaya"}
    elif "dirasakan" in t:
        return {"teks": "Getaran dirasakan oleh masyarakat di sekitar wilayah episentrum", "tipe": "info"}
    elif "tidak dirasakan" in t:
        return {"teks": "Gempa tidak dirasakan oleh masyarakat umum", "tipe": "normal"}
    else:
        return {"teks": teks, "tipe": "normal"}

def ambil_data_gempa():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        gempa = data["Infogempa"]["gempa"]

        coords_raw = gempa.get("Coordinates", "")
        if "," in coords_raw:
            lat, lon = coords_raw.split(",")
            gempa["lat"] = float(lat.strip())
            gempa["lon"] = float(lon.strip())
        else:
            gempa["lat"] = 0
            gempa["lon"] = 0

        # ✅ Format potensi
        gempa["potensi_data"] = format_potensi(gempa.get("Potensi", ""))

        return gempa

    except Exception as e:
        print("ERROR ambil_data_gempa:", e)
        return None

# ✅ Diubah jadi 10 gempa + sertakan koordinat untuk peta
def ambil_gempa_terkini():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        daftar = data["Infogempa"]["gempa"]

        hasil = []
        for g in daftar[:10]:
            coords_raw = g.get("Coordinates", "0,0")
            try:
                coords = coords_raw.split(",")
                lat = float(coords[0].strip())
                lon = float(coords[1].strip())
            except:
                lat, lon = 0, 0

            hasil.append({
                "Jam"      : g.get("Jam", "-"),
                "Tanggal"  : g.get("Tanggal", "-"),
                "Wilayah"  : g.get("Wilayah", "-"),
                "Magnitude": g.get("Magnitude", "-"),
                "lat"      : lat,
                "lon"      : lon,
            })
        return hasil

    except Exception as e:
        print("ERROR ambil_gempa_terkini:", e)
        return []

def cek_dan_kirim_notif(gempa):
    global gempa_terakhir_notif

    # print("=== CEK NOTIF ===")
    # print("Magnitude:", gempa.get("Magnitude"))
    # print("DateTime :", gempa.get("DateTime"))

    if gempa:
        id_sekarang = gempa.get("DateTime", "")
        if float(gempa["Magnitude"]) >= 3.5:
            if id_sekarang != gempa_terakhir_notif:
                kirim_notif_telegram(gempa)
                gempa_terakhir_notif = id_sekarang
                print(f"✅ Notif dikirim untuk gempa {gempa['Magnitude']} SR di {gempa['Wilayah']}")
            else:
                print(f"⏭️  Gempa sudah dikirim sebelumnya (skipped)")
        else:
            print(f"ℹ️  Gempa {gempa['Magnitude']} SR (threshold 3.5, tidak dikirim)")

# 🔄 Background job - check gempa setiap 5 menit
def background_check_gempa():
    print("🔍 Checking gempa terbaru...")
    gempa = ambil_data_gempa()
    if gempa:
        print(f"📊 Gempa terdeteksi: {gempa['Magnitude']} SR - {gempa['Wilayah']}")
        cek_dan_kirim_notif(gempa)
    else:
        print("❌ Gagal ambil data gempa")

# Setup scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=background_check_gempa, trigger="interval", minutes=5)
scheduler.start()

# Shutdown scheduler saat aplikasi ditutup
atexit.register(lambda: scheduler.shutdown())

@app.route("/")
def index():
    gempa         = ambil_data_gempa()
    gempa_terkini = ambil_gempa_terkini()
    cek_dan_kirim_notif(gempa)
    return render_template("index.html", gempa=gempa, gempa_terkini=gempa_terkini)

@app.route("/api/gempa")
def api_gempa():
    gempa         = ambil_data_gempa()
    gempa_terkini = ambil_gempa_terkini()
    cek_dan_kirim_notif(gempa)
    return jsonify({
        "gempa"        : gempa,
        "gempa_terkini": gempa_terkini
    })

if __name__ == "__main__":
    app.run(debug=True)
