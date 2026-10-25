# Panduan Katalon Studio

Dokumen ini menjelaskan cara membuat dan menjalankan tes web di Katalon Studio. Proyek native Katalon perlu disimpan langsung dari aplikasi Katalon Studio; repository ini tidak menyertakan proyek `.prj` palsu yang belum diverifikasi.

## Test case yang telah dijalankan

Nama: `TC_Login_Invalid_Credentials`

Alur yang diamati:
1. Membuka browser.
2. Membuka `https://parabank.parasoft.com/parabank/index.htm`.
3. Mengisi username dummy.
4. Mengisi password dummy.
5. Mengeklik tombol login.
6. Memastikan elemen pesan error terlihat.

Hasil yang diamati pada 25 Oktober 2026: **6 langkah Passed**, durasi sekitar 16,369 detik. Assertion saat ini memeriksa visibilitas elemen error. Pemeriksaan teks persis `The username and password could not be verified.` belum ditambahkan.

## Cara membuat test case
1. Buka Katalon Studio dan buat proyek web baru.
2. Gunakan Web Recorder/Object Spy untuk memeriksa elemen di halaman target.
3. Simpan objek login dan elemen pesan error pada Object Repository.
4. Buat test case `TC_Login_Invalid_Credentials`.
5. Tambahkan verifikasi elemen error setelah klik login.
6. Jalankan dengan Chrome dan simpan laporan hasil eksekusi yang aktual.

## Catatan keamanan
- Gunakan kredensial dummy saja.
- Jangan commit kata sandi, token sesi, atau informasi sensitif.
- Jangan mengklaim tes lulus jika belum dijalankan.

## Referensi
Dokumentasi resmi Katalon: https://docs.katalon.com/
