# tambah_video.py
# Script untuk menambahkan video promosi ke file "Daftar Menu Restoran.html"

NAMA_FILE = "Daftar Menu Restoran.html"

# 1. Baca file HTML yang sudah ada
with open(NAMA_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# 2. Cek apakah video sudah pernah ditambahkan (biar tidak dobel)
if 'id="promoVideo"' in html:
    print("⚠️  Video sudah ada di file. Tidak ditambahkan lagi.")
else:
    # 3. Siapkan blok CSS untuk video
    css_video = """
        /* ====== VIDEO PROMOSI ====== */
        .promo-section {
            max-width: 800px;
            margin: 0 auto 30px;
            text-align: center;
        }
        .promo-section h2 {
            text-align: left;
        }
        .video-wrapper {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            background: #000;
        }
        .video-wrapper video {
            width: 100%;
            display: block;
        }
    """

    # 4. Siapkan blok HTML untuk video
    html_video = """    <!-- ====== VIDEO PROMOSI 30 DETIK ====== -->
    <section class="promo-section">
        <h2>🎬 Video Promosi Spesial</h2>
        <div class="video-wrapper">
            <video id="promoVideo" controls autoplay muted loop playsinline>
                <source src="promosi.mp4" type="video/mp4">
                Browser Anda tidak mendukung tag video.
            </video>
        </div>
    </section>

"""

    # 5. Sisipkan CSS tepat sebelum </style>
    html = html.replace("</style>", css_video + "\n    </style>", 1)

    # 6. Sisipkan HTML video tepat sebelum <!-- Judul Utama -->
    html = html.replace("    <!-- Judul Utama -->", html_video + "    <!-- Judul Utama -->", 1)

    # 7. Simpan kembali ke file
    with open(NAMA_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Berhasil! Video promosi sudah ditambahkan ke", NAMA_FILE)