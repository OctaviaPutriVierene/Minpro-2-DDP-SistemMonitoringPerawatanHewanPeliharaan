# Minpro-2-DDP-SistemMonitoringPerawatanHewanPeliharaan
Nama  : Octavia Putri Vierene<br>
NIM   : 2609116012<br>
Kelas : A<br>
Judul : Sistem monitoring perawatan hewan peliharaan<br>

Penjelasan Program:<br>

Penjelasan Flowchart:<br>
Alur Login Sistem Monitoring

• Mulai & Input: Program dimulai dengan menampilkan menu login, lalu pengguna diminta memasukkan username.

• Fitur Stop: Jika username yang diketik adalah "stop", program langsung berhenti otomatis.

• Validasi Akun: Jika bukan "stop", pengguna memasukkan password. Sistem akan memeriksa apakah username terdaftar dan password-nya benar. Jika salah, muncul pesan kesalahan.

• Pengecekan Role: Jika login berhasil, sistem memisahkan hak akses:

  1. Jika akun adalah Admin, pengguna diarahkan ke Menu Admin.<br>
  Setelah masuk sebagai Admin, sistem menampilkan 8 opsi menu<br>
	2. Jika bukan Admin (Pengguna), diarahkan ke Menu Pengguna.<br>
  Setelah masuk sebagai Pengguna biasa, sistem menampilkan 5 opsi menu dengan hak akses yang lebih terbatas

<img width="401" height="689" alt="image" src="https://github.com/user-attachments/assets/32e43b7c-78de-49d8-8748-e7322392bd04" />

<img width="357" height="545" alt="image" src="https://github.com/user-attachments/assets/b17e7167-fb50-4458-a41b-f430a160abda" />


<img width="477" height="641" alt="image" src="https://github.com/user-attachments/assets/346b7c4a-a3ac-4b20-a7e4-ccd9338765b8" />


Output Login Admin:<br> 
Saat pertama kali program dijalankan, sistem akan meminta pengguna untuk memasukkan *username* dan *password*
<img width="324" height="413" alt="image" src="https://github.com/user-attachments/assets/f6a839c0-84dc-4e60-a576-09629abb1432" />

Jika, berhasil login sebagai ADMIN maka sistem akan menampilkan 8 menu.<br>

  
Output Login User:<br>
<img width="353" height="381" alt="image" src="https://github.com/user-attachments/assets/d629bce8-609e-47be-a703-c966ba568184" />

Jika, berhasil login sebagai USER/PENGGUNA maka sistem akan menampilkan 5 menu.<br>

Output Menu 5:<br>
<img width="361" height="381" alt="image" src="https://github.com/user-attachments/assets/79401196-e07b-4382-aa2f-1490cb98813a" />

Ketika kita login sebagai admin dan memilih menu 5, library `random` akan membuatkan 3 digit kode acak secara otomatis. Lalu admin dapat menginput nama dan jenis hewan<br>

Output Menu 1:<br>
Ketika Admin/Pengguna memilih menu 1, sistem akan menampilkan  semua data hewan yang terdaftar.<br>
<img width="312" height="253" alt="image" src="https://github.com/user-attachments/assets/5492eddd-5f15-44ad-a961-af12c570176b" />

Output Menu 2:<br>
Ketika Admin/Pengguna memilih menu 2 dan menginput kode yang valid maka sistem akan menampilkan hewan yang dicari.<br>
<img width="567" height="473" alt="image" src="https://github.com/user-attachments/assets/a588a7c9-69ca-4a3c-bb93-d3e5adb81333" />

Output Menu 3:<br>
Ketika Admin/Pengguna memilih nomor 3 dan 4, maka pengguna dan admin bisa mengubah status makan dan minum hewan. Dengan cara memasukkan kode yang valid.
Lalu, memilih `Sudah` dan `Belum`<br>
<img width="395" height="351" alt="image" src="https://github.com/user-attachments/assets/3114a58d-fd07-4353-a0cb-62b5528ce6a9" />

Output Menu 6:<br>
Ketika Admin memilih menu 6, admin dapat menghapus hewan dengan cara menginput kode yang valid<br>
<img width="424" height="355" alt="image" src="https://github.com/user-attachments/assets/e5815068-d6a5-42d1-a5ad-2afe8413c434" />

Output Menu 7:<br>
Ketika Admin memilih menu 7, maka admin dapat menghapus status yang tadinya sudah menjadi belum<br>
<img width="386" height="301" alt="image" src="https://github.com/user-attachments/assets/b346b29d-c6b7-4830-8340-3e511d244b6a" />

Output Menu 8 dan 5:<br>
Ketika Admin/ Pengguna memilih 8 dan 5, maka akan dia arahkan keluar dari menu.<br>
<img width="302" height="110" alt="image" src="https://github.com/user-attachments/assets/5f38ad9d-439b-4fbc-894a-ee5fce04a513" />


