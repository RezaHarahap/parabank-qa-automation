# Log Eksekusi — ParaBank QA Automation

Log ini hanya mencatat hasil yang telah ditunjukkan selama pengerjaan portofolio. Hasil bisa berubah karena aplikasi demo publik dan lingkungan lokal dapat berubah.

## Eksekusi yang diamati pada 25 Oktober 2026

| Tools | Skenario/bukti | Hasil yang diamati | Interpretasi dan batasan |
|---|---|---|---|
| Selenium + pytest | `python -m pytest -v` pada Windows 11, Python 3.12.2 | **2 passed, 2 skipped** dalam 34,52 detik | Tes form login dan umpan balik login tidak valid lulus. Tes overview akun dan form transfer dilewati karena kredensial akun demo belum diatur. Laporan HTML dibuat lokal; perlu disalin ke repository jika ingin dipublikasikan. |
| Cypress 14.5.4 | `npx cypress run`, Electron headless, Node.js 24.15.0 | **2 passing, 1 pending, 0 failing** sekitar 8 detik | Tes form login dan pesan kredensial tidak valid lulus. Navigasi login valid masih pending karena kredensial demo belum diatur. Video dibuat secara lokal. |
| Postman | `GET {{baseUrl}}/services` | **HTTP 200 OK**, 2/2 pemeriksaan yang ditampilkan lulus | Service index mengembalikan HTML yang mengiklankan layanan SOAP. Ini hanya memverifikasi respons endpoint yang diamati. |
| Postman | `GET {{baseUrl}}/services/bank/openapi.json` | **HTTP 200 OK**, 3/3 pemeriksaan yang ditampilkan lulus | Dokumen JSON OpenAPI diterima dan pemeriksaan yang terlihat lulus. Periksa ulang bila kontrak demo berubah. |
| Apache JMeter 5.6.3 | `ParaBank_ReadOnly_Smoke.jmx`, satu pengguna virtual/satu iterasi, GET halaman utama | **HTTP 200 OK**, Error Count 0 pada sampel yang ditampilkan | Hanya uji smoke konektivitas/waktu respons berintensitas rendah. Sampel ini tidak cukup untuk klaim load, stress, kapasitas, atau SLA. Waktu sekitar 742 ms terlihat pada salah satu sampel, bukan hasil benchmark. |
| Katalon Studio 11.6.0 | `TC_Login_Invalid_Credentials` | **6 langkah Passed** dalam 16,369 detik | Browser dibuka, halaman dituju, kredensial dummy diisi, tombol login diklik, dan elemen pesan error diverifikasi terlihat. Assertion teks persis belum ditambahkan. Bukti: [`katalon-invalid-login-passed.png`](../results/evidence/katalon-invalid-login-passed.png). |

## Prinsip pelaporan

- Status `Skipped` atau `Pending` bukan lulus atau gagal; skenario belum menyelesaikan assertion sebagai tes aktif.
- Respons HTTP sukses tidak membuktikan semua fungsi bisnis/API benar.
- Tes Katalon saat ini memeriksa visibilitas elemen error, bukan kecocokan teks persis.
- Jangan publikasikan screenshot/log yang berisi kata sandi, token, ID sesi, data pribadi, atau informasi rahasia.
- Sebelum publikasi, pastikan file bukti benar-benar ada dan sudah diperiksa dari sisi informasi sensitif.
