# Rencana Pengujian — ParaBank QA Automation

## 1. Tujuan
Memeriksa alur utama yang terlihat oleh pengguna dan perilaku layanan terpilih pada aplikasi demo ParaBank. Proyek ini juga menjadi latihan penerapan QA lintas tools UI, API, dan uji smoke performa berintensitas rendah.

## 2. Sistem yang diuji
- Aplikasi: ParaBank demo perbankan
- URL dasar: `https://parabank.parasoft.com/parabank`
- Service index: `https://parabank.parasoft.com/parabank/services`
- Dokumen OpenAPI yang diamati: `https://parabank.parasoft.com/parabank/services/bank/openapi.json`
- Jenis lingkungan: demo publik bersama, bukan sistem bank produksi

## 3. Cakupan pengujian
- Ketersediaan aplikasi dan halaman utama.
- Perilaku login berhasil/gagal menggunakan data uji.
- Halaman ringkasan akun dan navigasi akun bila akun demo tersedia.
- Validasi form transfer jika data demo memungkinkan; tidak melakukan transaksi dengan dana nyata.
- Eksplorasi API read-only sebelum pengujian alur bisnis API.
- Uji smoke waktu respons halaman utama dengan satu pengguna dan satu iterasi.
- Dokumentasi hasil dan pelaporan temuan.

## 4. Di luar cakupan
- Transaksi finansial nyata.
- Penetration testing, serangan kredensial, fuzzing, atau pengujian destruktif.
- Penghapusan database atau penggunaan endpoint administratif yang berisiko.
- Uji beban/stress berkonkurensi tinggi pada demo publik.
- Klaim kepatuhan regulasi atau keamanan bank produksi.

## 5. Strategi tools
- **Selenium + Python/pytest:** otomasi UI utama.
- **Cypress:** regresi UI independen untuk login.
- **Postman:** eksplorasi endpoint dan assertion respons.
- **Katalon Studio:** suite UI low-code terpisah.
- **Apache JMeter:** uji smoke read-only dengan beban sangat rendah.

## 6. Data uji
- Jangan mengasumsikan kredensial bawaan tertentu valid.
- Jika registrasi tersedia, buat akun demo khusus yang dapat dibuang.
- Simpan kredensial hanya pada environment lokal, bukan dalam repository.
- Hindari asumsi saldo atau ID akun tetap pada lingkungan demo bersama.

## 7. Kriteria masuk
- Situs target dapat diakses dari komputer pengujian.
- Browser dan dependensi framework terpasang.
- Endpoint dan struktur respons API telah diperiksa sesuai kondisi terkini.
- Data uji tidak memuat informasi pribadi atau finansial nyata.

## 8. Kriteria keluar
- Setiap skenario memiliki status: Passed, Failed, Skipped/Blocked, atau Not Run.
- Kegagalan memiliki log/bukti dan klasifikasi yang sesuai.
- Tidak ada tes yang dinyatakan Passed tanpa hasil eksekusi nyata.
- Laporan menjelaskan batasan lingkungan demo publik.

## 9. Risiko dan mitigasi
| Risiko | Mitigasi |
|---|---|
| Demo publik tidak tersedia atau tidak stabil | Catat sebagai Blocked dan coba kembali nanti; jangan langsung menyimpulkan bug produk. |
| Data demo berubah | Hindari saldo/ID tetap dan temukan data saat runtime jika memungkinkan. |
| Selector UI berubah | Perbarui locator berdasarkan DOM aktual. |
| Kontrak API berubah | Periksa ulang service index, dokumen OpenAPI, dan body respons. |
| Beban berlebih pada layanan publik | Batasi JMeter pada satu pengguna dan satu iterasi. |
| Duplikasi cakupan antar-tools | Beri peran berbeda untuk tiap tools dan dokumentasikan cakupannya. |

## 10. Pelaporan
Catat tanggal/waktu, versi tools, URL target, ID skenario, status, hasil aktual, kategori kegagalan, lokasi screenshot/log, serta tindak lanjut.
