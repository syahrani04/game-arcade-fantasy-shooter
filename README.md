# 🧚 Fantasy Fairy Shooter

Game 2D bergaya *arcade shooter* yang dibuat dengan **Python** dan **PyOpenGL (GLUT)**. Kamu mengendalikan seorang peri bersayap yang menembakkan peluru ajaib untuk menghancurkan bunga, bintang, dan jamur yang berjatuhan dari langit. Kumpulkan skor setinggi mungkin dan jaga tiga nyawamu.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![PyOpenGL](https://img.shields.io/badge/PyOpenGL-GLUT-5586A4)
![Resolusi](https://img.shields.io/badge/Window-800x600-lightgrey)

---

## 🎮 Tampilan Game

| Layar | Yang ditampilkan |
|-------|------------------|
| **Layar awal** | Judul `FANTASY FAIRY SHOOTER` dan teks `Press SPACE to Start` di atas latar gradasi biru dengan bintang jatuh. |
| **Saat bermain** | Peri di bagian bawah, peluru ajaib berwarna-warni, musuh yang jatuh, dan panel info di pojok kiri atas. |
| **Game over** | Teks `GAME OVER`, `Final Score: <skor>`, dan `Press R to Restart`. |

**Panel info (pojok kiri atas)** menampilkan `Score:` berisi angka skor saat ini, dan `Nyawa:` berisi ikon hati merah sesuai sisa nyawa (maksimal 3).

---

## 🕹️ Cara Bermain

1. Jalankan game, lalu tekan **SPACE** untuk memulai.
2. Gerakkan peri dengan **tombol panah** ke segala arah.
3. **Tahan SPACE** untuk menembak terus-menerus.
4. Tembak musuh sebelum mencapai dasar layar. Setiap musuh yang hancur memberi **+10 poin**.
5. Jika nyawa habis, layar *Game Over* muncul. Tekan **R** untuk kembali ke layar awal.

### Kontrol

| Tombol | Fungsi |
|--------|--------|
| ⬅️ ➡️ ⬆️ ⬇️ | Menggerakkan peri (kiri, kanan, atas, bawah) |
| `SPACE` | Memulai game dan menembak (tahan untuk tembakan beruntun) |
| `R` | Restart setelah *Game Over* |

---

## ✨ Elemen Game

### Peri (pemain)
- Digambar dari sayap biru muda (4 lingkaran), tubuh oval pink, kepala, dan mahkota kecil berwarna kuning.
- Mulai di tengah bawah layar (posisi 400, 60).
- Bergerak 10 piksel per frame dan dibatasi agar tidak keluar dari layar.

### Peluru Ajaib
- Sekali tekan menembakkan **3 peluru sekaligus**: kuning (tengah), cyan (kiri), dan magenta (kanan).
- Tiap peluru berbentuk peri mini bersayap yang melaju ke atas.
- Jeda antar tembakan 0,2 detik, jadi sekitar 5 salvo per detik jika SPACE ditahan.

### Musuh
Tiga jenis musuh muncul acak dari atas layar, masing-masing dengan warna acak:

| Jenis | Bentuk |
|-------|--------|
| 🌸 Bunga | Kelopak berwarna acak dengan pusat kuning |
| ⭐ Bintang | Bintang bersudut lima |
| 🍄 Jamur | Topi setengah lingkaran dengan batang krem |

Musuh jatuh lurus ke bawah dan muncul di posisi horizontal acak.

### Latar & Efek
- **Latar** berupa gradasi biru langit.
- **Bintang jatuh** berwarna putih kebiruan turun perlahan sebagai hiasan latar.
- **Efek ledakan** berupa cincin kuning singkat di titik musuh yang tertembak.

---

## 📏 Aturan & Skor

| Aturan | Nilai |
|--------|-------|
| Skor per musuh yang hancur | **+10** |
| Nyawa awal | **3** (ditampilkan sebagai hati) |
| Pengurang nyawa | Musuh lolos hingga melewati batas bawah layar |
| Syarat kalah | Nyawa mencapai 0 |
| Deteksi tabrakan | Jarak peluru ke pusat musuh kurang dari 30 piksel |

---

## 🛠️ Spesifikasi Teknis

- **Ukuran window:** 800 × 600 piksel (judul window: *Fantasy Fairy Shooter*)
- **Frame rate:** sekitar 30 FPS (timer 33 ms), dengan *double buffering*
- **Proyeksi:** ortografik 2D (`gluOrtho2D`)
- **Input:** keyboard saja (tombol ASCII dan tombol khusus GLUT)

### Teknik Grafika
Game ini memakai kombinasi algoritma rasterisasi dan primitif OpenGL:

- **Midpoint Circle** (`circle.py`) untuk badan bintang latar dan efek ledakan.
- **Midpoint Line** (`line.py`) untuk ekor bintang latar.
- **Primitif OpenGL** (`GL_TRIANGLE_FAN`, `GL_POLYGON`, `GL_QUADS`, `GL_TRIANGLES`) untuk peri, peluru, musuh, hati, dan latar gradasi.

---

## 🚀 Instalasi & Menjalankan

### Prasyarat
- **Python 3.8+**
- **PyOpenGL** dan **GLUT/freeglut**

### 1. Install dependensi
```bash
pip install PyOpenGL PyOpenGL_accelerate
```

> Folder `OpenGL/` sudah disertakan di dalam proyek (termasuk `freeglut` untuk Windows). Jika game langsung berjalan, langkah ini bisa dilewati.

Khusus **Linux**, pasang freeglut terlebih dahulu:
```bash
sudo apt install freeglut3-dev
```
Di **macOS**, GLUT sudah tersedia bawaan sistem.

### 2. Jalankan game
```bash
cd "Fantasy Shooter Game"
python main.py
```

---

## 📁 Struktur Proyek

```
game arcade/
├── README.md
└── Fantasy Shooter Game/
    ├── main.py       # Loop game, input, HUD, tabrakan, layar awal & game over
    ├── classes.py    # Kelas Fairy, MagicBullet, FlowerEnemy, dan Star
    ├── circle.py     # Algoritma Midpoint Circle
    ├── line.py       # Algoritma Midpoint Line
    └── OpenGL/       # Library PyOpenGL yang ikut disertakan
```

---

## 📌 Ringkasan Kelas

| Kelas | File | Peran |
|-------|------|-------|
| `Fairy` | `classes.py` | Karakter pemain |
| `MagicBullet` | `classes.py` | Peluru yang ditembakkan pemain |
| `FlowerEnemy` | `classes.py` | Musuh (bunga, bintang, atau jamur) |
| `Star` | `classes.py` | Bintang jatuh pada latar |
| `MidpointCircle()` | `circle.py` | Fungsi menggambar lingkaran |
| `MidpointLine()` | `line.py` | Fungsi menggambar garis |

---

Selamat bermain! 🌟
