# Portofolio QA Automation — ParaBank Demo

Proyek portofolio pengujian perangkat lunak pada aplikasi demo perbankan **ParaBank**. Proyek ini memperlihatkan proses pengujian UI, API, serta uji performa dasar menggunakan beberapa tools QA.

> **Catatan keamanan dan ruang lingkup:** ParaBank yang digunakan adalah aplikasi demo publik, bukan sistem bank produksi. Gunakan hanya data uji/dummy. Proyek ini bukan izin untuk menguji sistem produksi atau melakukan pengujian beban tinggi pada layanan publik.

## Tujuan proyek

- Mempraktikkan penyusunan test case dan dokumentasi QA.
- Mengotomasi skenario UI dasar dan login dengan kredensial tidak valid.
- Memeriksa respons endpoint API yang dapat diakses secara aman.
- Menjalankan uji smoke HTTP berintensitas rendah dengan JMeter.
- Mencatat hasil pengujian secara transparan, termasuk skenario yang dilewati atau belum dijalankan.

## Tools dan cakupan

| Tools | Penggunaan dalam proyek | Cakupan yang diuji |
|---|---|---|
| Selenium + Python + pytest | Otomasi UI | Form login, umpan balik login tidak valid, serta pemeriksaan overview/transfer yang memerlukan akun demo opsional |
| Cypress | Regresi UI | Tampilan form login, umpan balik kredensial tidak valid, navigasi login valid jika kredensial dummy tersedia |
| Postman | Eksplorasi API | Pemeriksaan service index dan dokumen OpenAPI yang ditemukan |
| Apache JMeter | Uji smoke HTTP | Satu pengguna virtual, satu iterasi, permintaan GET halaman utama yang hanya membaca data |
| Katalon Studio | Otomasi UI low-code | Alur login tidak valid dan pemeriksaan visibilitas elemen pesan error |

## Hasil eksekusi yang diamati

Hasil berikut berasal dari eksekusi di komputer Windows pada **25 Oktober 2026**. Hasil dapat berubah apabila aplikasi demo atau lingkungan lokal berubah.

| Tools | Hasil yang diamati | Catatan |
|---|---|---|
| Selenium + pytest | **2 passed, 2 skipped** | Form login dan umpan balik login tidak valid lulus. Dua skenario yang memerlukan kredensial akun demo dilewati. |
| Cypress 14.5.4 | **2 passing, 1 pending, 0 failing** | Form login dan umpan balik login tidak valid lulus. Skenario login valid masih pending karena kredensial demo belum dikonfigurasi. |
| Postman | **HTTP 200 OK** pada dua request | Pemeriksaan yang terlihat di Postman menunjukkan 2/2 dan 3/3 assertion lulus. Ini tidak membuktikan seluruh fungsi API benar. |
| Apache JMeter 5.6.3 | **HTTP 200 OK, Error Count 0** pada sampel yang ditampilkan | Hanya uji smoke satu pengguna/satu iterasi, bukan uji load, stress, kapasitas, atau SLA. |
| Katalon Studio 11.6.0 | **6 langkah passed** | Alur login tidak valid berhasil dieksekusi dan elemen pesan error terlihat. Assertion untuk mencocokkan teks error secara persis masih menjadi peningkatan berikutnya. |

Rincian ada di [`docs/EXECUTION_LOG.md`](docs/EXECUTION_LOG.md). Bukti eksekusi Katalon: [`katalon-invalid-login-passed.png`](results/evidence/katalon-invalid-login-passed.png).

## Struktur folder

```text
.
├── .github/workflows/       # Alur CI yang disiapkan
├── cypress/                 # Konfigurasi dan tes UI Cypress
├── docs/                    # Test plan, test case, log eksekusi, audit, template bug
├── jmeter/                  # Rencana uji smoke JMeter
├── katalon/                 # Panduan proyek Katalon Studio
├── postman/                 # Koleksi dan environment Postman
├── results/evidence/        # Bukti screenshot yang telah disiapkan
└── selenium-tests/          # Tes Selenium + pytest
```

## Cara menjalankan Selenium + pytest (Windows Git Bash)

```bash
cd selenium-tests
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
export PARABANK_BASE_URL="https://parabank.parasoft.com/parabank"
python -m pytest -v
```

Untuk membuat laporan HTML:

```bash
python -m pytest -v --html=../results/selenium-report.html --self-contained-html
```

Skenario yang membutuhkan akun hanya akan berjalan jika `PARABANK_USERNAME` dan `PARABANK_PASSWORD` diatur ke akun demo khusus pengujian. Jangan commit kata sandi atau data rahasia ke GitHub.

## Cara menjalankan Cypress (Windows Git Bash)

```bash
cd cypress
npm install
npx cypress verify
npx cypress run
```

Cypress menyimpan video dan screenshot kegagalan secara lokal. Periksa file tersebut sebelum dipublikasikan; jangan unggah token sesi atau informasi sensitif.

## Cara menjalankan Postman

1. Buka Postman dan impor `postman/ParaBank.postman_collection.json`.
2. Impor `postman/ParaBank.postman_environment.json`, lalu pilih environment tersebut.
3. Jalankan collection dan periksa respons serta hasil assertion pada setiap request.
4. Cocokkan kembali endpoint dan struktur respons dengan service index yang tersedia saat pengujian, karena kontrak API demo dapat berubah.

Collection dibuat konservatif. Jangan menambahkan operasi administratif yang merusak data atau menggunakan data finansial nyata.

## Cara menjalankan Apache JMeter

1. Buka `jmeter/ParaBank_ReadOnly_Smoke.jmx` menggunakan Apache JMeter.
2. Pertahankan konfigurasi awal **1 pengguna virtual dan 1 iterasi** saat menguji layanan demo publik.
3. Jalankan sekali, lalu periksa `View Results Tree` dan `Summary Report`.
4. Jangan melakukan uji load/stress pada demo publik. Untuk pengujian tersebut, gunakan lingkungan lokal atau staging yang secara eksplisit diizinkan.

## Katalon Studio

Lihat [`katalon/README.md`](katalon/README.md). Proyek native Katalon disimpan dari aplikasi Katalon Studio, bukan dibuat-buat dari file konfigurasi. Test case yang diamati bernama `TC_Login_Invalid_Credentials`; assertion saat ini memastikan elemen error terlihat. Pencocokan teks error secara persis disarankan sebagai peningkatan berikutnya.

## Dokumentasi QA

- [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md) — tujuan, ruang lingkup, strategi, risiko, kriteria masuk/keluar.
- [`docs/TEST_CASES.csv`](docs/TEST_CASES.csv) — daftar skenario uji.
- [`docs/BUG_REPORT_TEMPLATE.md`](docs/BUG_REPORT_TEMPLATE.md) — template pelaporan bug.
- [`docs/EXECUTION_LOG.md`](docs/EXECUTION_LOG.md) — hasil eksekusi yang diamati dan keterbatasannya.
- [`docs/AUDIT_REPORT.md`](docs/AUDIT_REPORT.md) — catatan pemeriksaan statis dan audit.

## Keterbatasan dan rencana peningkatan

1. Tambahkan assertion teks yang tepat pada tes invalid login Katalon.
2. Jalankan ulang seluruh suite sebelum rilis portofolio dan perbarui log sesuai hasil terbaru.
3. Tambahkan assertion alur bisnis API hanya setelah kontrak API dan akun demo yang dapat dibuang telah diverifikasi.
4. Tambahkan pengujian aksesibilitas, browser lain, dan variasi input negatif.
5. Jangan menyebut uji JMeter satu permintaan ini sebagai uji load, stress, atau kapasitas.

## Ringkasan

Proyek ini mendokumentasikan latihan QA lintas tools untuk pengujian UI, eksplorasi API, dan uji smoke HTTP dasar. Status `skipped` atau `pending` dicatat apa adanya dan tidak dihitung sebagai tes lulus. Semua hasil merupakan hasil yang diamati pada lingkungan demo, bukan jaminan hasil pada eksekusi berikutnya.
