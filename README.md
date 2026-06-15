## Sistem Monitoring Gempa

Indonesia Earthquake Detector adalah sistem monitoring gempa bumi berbasis web yang menampilkan data gempa secara real-time dari API BMKG (Badan Meteorologi, Klimatologi, dan Geofisika). Sistem ini dirancang untuk memberikan informasi gempa terkini kepada pengguna dengan tampilan visual yang informatif, peta interaktif, dan notifikasi otomatis melalui Telegram.

## Website

https://gempa-indonesia.onrender.com/

## Fitur Website

* Informasi gempa terbaru: tanggal, jam, magnitudo, kedalaman, wilayah, koordinat, dirasakan
* Pesan otomatis dikirim ke Telegram saat terdeteksi gempa M ≥ 5.0 SR
* Menampilkan 10 titik episentrum gempa terkini.
* Marker terbesar = gempa paling baru, warna berdasarkan magnitudo
* Daftar 10 gempa terkini dengan badge warna berdasarkan magnitudo
* Banner merah berkedip muncul otomatis jika BMKG menyatakan potensi tsunami
* Teks potensi BMKG diterjemahkan menjadi lebih spesifik dengan kode warna

## Sumber Data Website

Data gempa bumi yang digunakan dalam sistem ini bersumber dari Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)

BMKG Gempabumi Terkini

https://www.bmkg.go.id/gempabumi

BMKG Gempabumi Real-time

https://www.bmkg.go.id/gempabumi/gempabumi-realtime

## Teknologi yang Digunakan

| Komponen | Teknologi | Fungsi |
|---|---|---|
| Backend | Python | Bahasa pemrograman utama untuk logika server |
| Framework | Flask | Web framework untuk routing dan serving HTTP |
| Frontend | HTML | Struktur halaman web |
| Styling | CSS | Struktur halaman web |
| Interaktivitas | JavaScript| Interaktivitas	JavaScript	Logika sisi browser, auto-refresh, peta |
| Pemetaan | Leaflet.js | Library peta interaktif berbasis JavaScript |
| Basemap | OpenStreetMap | Sumber tile/gambar peta gratis |
| Template Engine | Jinja2 | Sumber tile/gambar peta gratis |
| Pengolahan Data | Built-in JSON | Mengirim data gempa dari BMKG |
| HTTP Client | request | HTTP Client	requests	Mengambil data dari API BMKG |
| Penyimpanan Data | Real-time API (BMKG) | Data gempa real-time Indonesia |
| Notifikasi | Telegram Bot API | Pengiriman notifikasi otomatis ke HP |
| Deployment | Render | Platform hosting aplikasi web |
