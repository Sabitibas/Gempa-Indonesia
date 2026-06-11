## Sistem Monitoring Gempa

Website monitoring gempa bumi berbasis web yang menampilkan informasi gempa terbaru dari BMKG, dilengkapi batas minimal magnitudo, dan sistem notifikasi

## Website

https://gempa-indonesia.onrender.com/

## Fitur Website

* Menampilkan informasi gempa bumi terbaru secara real-time
* Filter notifikasi berdasarkan magnitudo minimum
* Auto refresh data gempa
* Menampilkan lokasi, magnitudo, kedalaman, dan waktu kejadian gempa
* Notifikasi gempa sesuai preferensi pengguna
* Menampilkan informasi potensi ancaman dari gempa yang terjadi

## Sumber Data Website

Data gempa bumi yang digunakan dalam sistem ini bersumber dari Badan Meteorologi, Klimatologi, dan Geofisika (BMKG)

BMKG Gempabumi Terkini

https://www.bmkg.go.id/gempabumi

BMKG Gempabumi Real-time

https://www.bmkg.go.id/gempabumi/gempabumi-realtime

## Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Backend | Python |
| Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| Pemetaan | Leaflet.js |
| Basemap | OpenStreetMap |
| Pengolahan Data | Built-in JSON (requests) |
| Penyimpanan Data | Real-time API (BMKG) |
| Notifikasi | Telegram Bot API |
| Deployment | Render |
