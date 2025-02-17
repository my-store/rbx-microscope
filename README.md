# RBX MICROSCOPE
Versi 1.0 | diperbarui pada 22 Jan 2024 oleh Izzat Alharis


![Screenshot](screenshot.jpg)


Bismillah,

Aplikasi ini dibuat menggunakan bahasa pemrograman python, menggunakan library bawaan python untuk GUI nya yaitu tkinter, serta menggunakan library vision yang dikembangkan oleh perusahaan Intel yaitu OpenCV.

Dapat digunakan untuk monitoring menggunakan tiga kamera sekaligus, dalam proses uji-coba saya menggunakan satu microscope dan dua kamera digital untuk keperluan recording, untuk saat ini baru mendukung kamera USB.

Target pengembangan selanjutnya aplikasi ini mendukung wired ataupun wireless IP camera, dengan begitu aplikasi ini dapat juga digunakan untuk mengontrol CCTV.


## PANDUAN PENGGUNAAN
1. Buka folder executable
2. Unduh seluruh file didalamnya
3. Extract file bernama "extract-me.zip"
4. Buka folder hasil extract dan nanti akan ada file bernama "rbx-microscope.exe"
5. Jalankan aplikasi dengan cara double click file bernama "rbx-microscope.exe"


## PANDUAN PENGEMBANGAN/ DEVELOPMENT
1. Pastikan Python telah teristal di komputer teman-teman
2. Buka folder src
3. Unduh seluruh file didalamnya
4. Buat folder bernama "rbx-microscope" di komputer teman-teman dan masukkan seluruh hasil download kedalamnya
5. Buat virtual environment didalam folder "rbx-microscope"
   * python -m venv virt
6. Aktifkan virtual environment
   * Windows: .\virt\Scripts\activate
   * Linux: source ./virt/bin/activate
8. Install seluruh library didalam file "requirements.txt"
   * pip install -r requirements.txt
9. Jalankan file utama bernama "app.py"
   * python app.py

Silahkan lakukan perubahan pada file utama "app.py" ataupun file yang mengatur logika "camera.py" sesuai keinginan, jika teman-teman telah menguasai bahasa pemrograman Python tentunya proses modifikasi sangat menyenangkan bukan? 🤣


## AVAILABLE FEATURES
* Horizontal flip
* Vertical flip
* Toggle switch on-off
* Snapshot button


## CATATAN PENULIS
Saya membuat aplikasi ini untuk keperluan dokumentasi kegiatan di meja kerja, ini sangat berguna jika teman-teman adalah konten kreator seputar elektronik, saya tidak menjual aplikasi ini, silahkan dipakai jika teman-teman membutuhkannya, saya sangat senang jika teman-teman juga berminat mengembangkannya.

Mohon maaf jika ada kesalahan dalam penulisan, atau panduan yang saya berikan tidak membantu, teman-teman bisa menghubungi saya melalui kontak dibawah ini.


## KONTAK PENULIS
* Email: izzatalharist@gmail.com
* Telegram: https://t.me/pmtkom
