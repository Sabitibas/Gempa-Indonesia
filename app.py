from flask import Flask, render_template
import requests
from notifikasi import kirim_notif_telegram  # ✅ BARU

app = Flask(__name__)

# ✅ BARU: simpan ID gempa terakhir yang sudah dinotifikasi
# supaya tidak kirim notif berulang untuk gempa yang sama
gempa_terakhir_notif = None

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

        return gempa

    except Exception as e:
        print("ERROR ambil_data_gempa:", e)
        return None

def ambil_gempa_terkini():
    url = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        daftar = data["Infogempa"]["gempa"]

        hasil = []
        for g in daftar[:5]:
            hasil.append({
                "Jam"       : g.get("Jam", "-"),
                "Tanggal"   : g.get("Tanggal", "-"),
                "Wilayah"   : g.get("Wilayah", "-"),
                "Magnitude" : g.get("Magnitude", "-"),
            })
        return hasil

    except Exception as e:
        print("ERROR ambil_gempa_terkini:", e)
        return []

@app.route("/")
def index():
    global gempa_terakhir_notif  # ✅ BARU

    gempa         = ambil_data_gempa()
    gempa_terkini = ambil_gempa_terkini()

    # ✅ BARU: cek dan kirim notifikasi jika gempa >= 5
    if gempa:
        id_gempa_sekarang = gempa.get("DateTime", "")  # pakai DateTime sebagai ID unik

        if float(gempa["Magnitude"]) >= 5:
            if id_gempa_sekarang != gempa_terakhir_notif:
                kirim_notif_telegram(gempa)
                gempa_terakhir_notif = id_gempa_sekarang  # tandai sudah dinotifikasi

    return render_template("index.html", gempa=gempa, gempa_terkini=gempa_terkini)

if __name__ == "__main__":
    app.run(debug=True)