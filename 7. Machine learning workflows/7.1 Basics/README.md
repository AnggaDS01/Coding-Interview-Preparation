# 7.1 Basics

### 1. [E] Supervised, Unsupervised, Weakly Supervised, Semi-Supervised, dan Active Learning

- **Supervised Learning**: Ini kayak lo ngasih guru yang selalu ngasih tahu jawaban. Lo punya dataset di mana setiap input ada label yang benar, kayak gambar kucing yang udah ditandai sebagai "kucing." Model belajar dari data yang udah lengkap ini.
  - **Contoh**: Klasifikasi gambar, kayak Google Photos yang bisa ngelompokkan foto lo berdasarkan objeknya.

- **Unsupervised Learning**: Model belajar sendiri tanpa bantuan label. Jadi, kayak lo kasih anak-anak main di taman, dan mereka harus cari cara sendiri untuk bikin kelompok. Misal, lo kasih dataset gambar dan suruh model menemukan pola tanpa tahu itu gambar kucing atau anjing.
  - **Contoh**: Clustering, seperti mengelompokkan pelanggan berdasarkan kebiasaan belanja.

- **Weakly Supervised Learning**: Di sini lo cuma kasih label yang nggak terlalu lengkap atau akurat. Jadi, model belajar dari data yang nggak sepenuhnya benar atau lengkap.
  - **Contoh**: Misal lo punya data banyak, tapi cuma sebagian kecil yang dilabeli dengan benar. Model tetap belajar walaupun datanya nggak sempurna.

- **Semi-Supervised Learning**: Ini kombinasi antara supervised dan unsupervised. Lo punya sebagian data yang berlabel dan sebagian lagi nggak berlabel, dan model belajar dari keduanya.
  - **Contoh**: Google Translate yang belajar dari kalimat terjemahan manusia (berlabel) dan dokumen-dokumen tanpa terjemahan (nggak berlabel).

- **Active Learning**: Model yang pinter, karena dia bisa "nanya" data mana yang penting buat dilabeli. Misal, model lo bingung di beberapa data, dia bakal minta lo kasih label di data yang paling membingungkan, jadi model lebih cepat pinter.
  - **Contoh**: Sistem rekomendasi yang minta feedback pengguna untuk memperbaiki prediksinya.
---
### 2. Empirical Risk Minimization
- **Risk**: Dalam konteks ini, **risk** adalah kesalahan yang dibuat model saat memprediksi. Bayangin kayak lo lagi prediksi hasil ujian, semakin besar gap antara prediksi lo dan kenyataan, semakin besar "risk" atau kerugiannya.
- **Empirical**: Disebut empirical karena kita menghitung risk ini dari **data yang ada** (empirical data), bukan data yang sempurna atau teoretis.
  - **Rumusnya**: $R_{\text{emp}}(h) = \frac{1}{n} \sum_{i=1}^{n} L(y_i, h(x_i))$
  - Di sini, $R_{\text{emp}}(h)$ adalah empirical risk, $L$ adalah loss function (biasanya error), dan $h(x_i)$ adalah prediksi model.
- **Minimizing Risk**: Untuk mengurangi risk, lo harus optimasi model lo, biasanya dengan menggunakan teknik seperti **gradient descent** buat ngurangin kesalahan prediksi.
---
### 3. [E] Occam's Razor dalam ML
- Prinsip ini bilang, kalau ada dua solusi yang sama bagusnya, pilih yang lebih sederhana. Di machine learning, lo bisa aplikasikan ini dengan memilih model yang lebih simpel.
  - **Contoh**: Kalau lo punya model neural network yang besar dan model decision tree yang kecil, dan dua-duanya punya akurasi yang mirip, pilih yang lebih kecil (karena lebih sederhana, lebih cepat, dan nggak terlalu overfitting).
---
### 4. [E] Kondisi yang Memungkinkan Deep Learning Populer dalam Satu Dekade Terakhir
Beberapa faktor yang bikin deep learning jadi populer:
- **Data**: Sekarang data lebih melimpah dibanding dulu. Lo punya akses ke miliaran gambar, teks, dan data lainnya yang bikin model deep learning bisa belajar lebih banyak.
- **Komputasi**: GPU dan TPU bikin perhitungan matematis yang berat jadi lebih cepat, bikin training neural network raksasa lebih feasible.
- **Algoritma**: Algoritma deep learning udah makin canggih, kayak penggunaan **ReLU** sebagai activation function dan **dropout** buat ngurangin overfitting.
- **Open Source**: Banyak framework kayak TensorFlow, PyTorch yang bikin deep learning jadi lebih mudah diakses siapa saja.
---
### 5. [M] Wide vs Deep Neural Network
- **Wide NN**: Lo punya banyak neuron di setiap layer tapi layer-nya sedikit. Ini kayak otak yang punya banyak koneksi tapi nggak banyak tahapan pemrosesan.
  - **Kelebihan**: Bagus buat mempelajari fitur yang sederhana dan menangani data yang nggak terlalu kompleks.
- **Deep NN**: Lo punya banyak layer, tapi mungkin jumlah neuron di setiap layer nggak terlalu banyak. Ini kayak proses berpikir bertahap, lebih mendalam.
  - **Kelebihan**: Lebih bagus buat mempelajari fitur yang kompleks dan hierarki, kayak deteksi objek di gambar.
---
### 6. [H] Universal Approximation Theorem: Kenapa Neural Network Sederhana Nggak Bisa Capai Error yang Kecil Banget?
- **Universal Approximation Theorem** bilang kalau neural network dengan satu hidden layer bisa memprediksi fungsi kontinu apa pun dalam rentang tertentu. Jadi, kenapa nggak bisa dapet error kecil banget?
  - **Jawabannya**: Meski bisa mendekati fungsi kontinu, lo tetap butuh **parameter yang cukup banyak** dan **aktivasi yang tepat** untuk meminimalisir error. Kalau lo cuma pakai jaringan kecil atau jumlah neuron yang terbatas, model nggak bakal bisa nangkep pola yang kompleks.
  - Contohnya, lo mungkin bisa niru bentuk kurva dengan beberapa neuron, tapi semakin detail bentuknya, semakin banyak neuron yang lo butuhin buat ngepasin setiap lekukan. Selain itu, ada juga tantangan **overfitting** kalau jaringan terlalu kompleks, yang bikin model malah lebih jelek di data baru.
  
  Neural network yang sederhana juga bisa terjebak di **saddle points** atau **local minima**, yang bisa bikin error nggak bisa lebih kecil lagi.
---
### 7. [E] Saddle Points dan Local Minima, Mana yang Lebih Mengganggu Training NN Besar?
- **Saddle Points**: Ini titik di mana gradient turun di satu arah tapi naik di arah lain. Di sini model bisa stuck karena gradient descent nggak tahu harus jalan ke mana.
  - **Local Minima**: Titik di mana error kecil tapi belum yang paling kecil secara global. Model bisa nyangkut di sini, meskipun ada solusi yang lebih baik.
  - **Mana yang lebih mengganggu**? **Saddle points** lebih banyak bikin masalah di neural network yang besar, karena di model dengan banyak dimensi, **saddle points** jauh lebih sering muncul dibanding **local minima**. Model bisa stuck dan butuh lebih banyak usaha buat keluar dari titik ini.
---
### 8. Hyperparameters

#### i. [E] Apa Bedanya Parameters dan Hyperparameters?
- **Parameters**: Ini yang dipelajari oleh model dari data selama training, misalnya bobot (weights) di neural network.
- **Hyperparameters**: Ini yang harus di-set **sebelum** training dimulai, misalnya jumlah hidden layers, learning rate, batch size, dll.
  - **Contoh**: Di neural network, **parameters** adalah bobot di tiap koneksi antar neuron, sementara **hyperparameters** kayak jumlah layer atau ukuran batch.

#### ii. [E] Kenapa Hyperparameter Tuning Penting?
- Hyperparameter tuning penting karena bisa **ngaruh besar ke performa model lo**. Kalau salah set, bisa overfitting (model terlalu pinter di training data tapi jelek di data baru) atau underfitting (model nggak cukup pinter buat nangkep pola dari data). Jadi, dengan setting yang pas, model lo bisa dapet performa terbaik.

#### iii. [M] Algoritma untuk Hyperparameter Tuning
Ada beberapa cara buat **tuning hyperparameters**:
- **Grid Search**: Lo cobain semua kombinasi hyperparameters yang mungkin dalam range yang udah ditentukan.
  - **Contoh**: Misal lo mau coba learning rate $\{0.001, 0.01, 0.1\}$ dan batch size $\{32, 64, 128\}$, lo bakal nge-train model untuk semua kombinasi ini.
- **Random Search**: Lo cobain kombinasi hyperparameters secara acak. Ini lebih efisien dibanding grid search kalau space hyperparameters-nya besar.
- **Bayesian Optimization**: Ini cara yang lebih pintar karena algoritmanya belajar dari hasil sebelumnya dan memilih kombinasi yang punya kemungkinan lebih baik.
  - **Contoh framework**: Lo bisa pakai **Optuna** atau **Hyperopt** buat bayesian optimization.
---
### 9. Classification vs Regression

#### i. [E] Apa Beda Classification dan Regression?
- **Classification**: Lo prediksi kategori dari data, misalnya gambar ini kucing atau anjing.
  - **Contoh**: Prediksi apakah email ini spam atau bukan.
- **Regression**: Lo prediksi nilai **kontinu**, misalnya prediksi harga rumah berdasarkan luas, lokasi, dll.
  - **Contoh**: Prediksi suhu esok hari berdasarkan data cuaca sebelumnya.

#### ii. [E] Bisa Nggak Classification Diubah Jadi Regression (dan Sebaliknya)?
- **Bisa**! Lo bisa ubah **classification** jadi **regression** dengan ngeprediksi **probabilitas** tiap kelas.
  - **Contoh**: Model prediksi probabilitas suatu gambar itu 70% kucing, 30% anjing.
- Sebaliknya, lo bisa juga ubah **regression** jadi **classification** dengan cara **binarize** hasil prediksinya.
  - **Contoh**: Kalau harga rumah di bawah \$500,000, itu kelas "murah", kalau di atas itu "mahal."
---
### 10. Parametric vs Non-Parametric Methods

#### i. [E] Apa Beda Parametric dan Non-Parametric Methods?
- **Parametric**: Metode yang punya asumsi tetap tentang struktur data, dan biasanya jumlah parameternya tetap meskipun jumlah data bertambah.
  - **Contoh**: **Linear regression**—model cuma punya beberapa parameter (slope dan intercept) dan nggak berubah walau data makin banyak.
- **Non-Parametric**: Metode yang nggak punya asumsi tetap, dan jumlah parameternya bisa berubah sesuai jumlah data.
  - **Contoh**: **K-Nearest Neighbors (KNN)**—jumlah tetangga yang diperiksa bisa berubah tergantung pada data.

#### ii. [H] Kapan Pakai Parametric dan Kapan Non-Parametric?
- **Pakai Parametric** kalau lo punya data terbatas atau lo yakin bahwa asumsi model cukup buat nangkep pola dari data.
  - **Contoh**: Linear regression buat dataset kecil di mana lo yakin hubungan antar variabelnya linear.
- **Pakai Non-Parametric** kalau lo punya banyak data dan lo nggak yakin tentang pola spesifik dari data.
  - **Contoh**: KNN atau decision tree buat data kompleks di mana pola antar variabelnya nggak jelas.

---
### 11. [M] Kenapa Ensembling Model yang Dilatih Secara Independen Biasanya Meningkatkan Performa?
- **Ensembling** adalah teknik di mana lo gabung beberapa model yang dilatih secara independen untuk membuat prediksi gabungan. 
  - **Kenapa lebih baik?** Karena setiap model punya kelemahan masing-masing. Tapi kalau lo gabung banyak model, kelemahan satu model bisa diatasi oleh kekuatan model lain. Ini kayak lo dapet opini dari beberapa orang yang berbeda buat ambil keputusan, makin banyak perspektif, makin kecil kemungkinan lo salah.
  - **Contoh**: Kalau lo punya tiga model yang prediksinya sedikit berbeda, lo bisa ambil rata-rata (voting atau averaging). Jadi kalau satu model salah, model lain bisa bantu benerin.
  - **Analogi**: Ini kayak lo nonton film dari beberapa sumber review, bukan cuma satu. Kalau banyak yang bilang bagus, film itu mungkin emang bagus.
---
### 12. [M] Kenapa L1 Regularization Cenderung Bikin Sparsity dan L2 Regularization Bikin Bobot Mendekati 0?
- **L1 Regularization**: Ini nambah penalti $\lambda \sum |w|$ (nilai absolut dari bobot) ke fungsi loss. Karena ngurangin nilai absolut bobot, ini bikin beberapa bobot jadi **nol** (sparse).
  - **Kenapa?** Karena **L1** lebih suka ngedorong bobot kecil buat langsung jadi 0. Jadi, bobot yang nggak penting bakal dihapus, yang penting tetap ada. Ini bikin model lebih simpel dan efisien.
  
- **L2 Regularization**: Ini nambah penalti $\lambda \sum w^2$ ke fungsi loss. Karena ngurangin kuadrat bobot, ini cenderung bikin bobot-bobot kecil **mendekati 0**, tapi jarang banget bikin mereka benar-benar 0.
  - **Kenapa?** Karena penalti kuadrat bikin bobot kecil makin kecil tanpa menghapusnya sepenuhnya. Ini lebih fokus buat bikin bobot nggak terlalu ekstrim, tapi nggak bikin sparsity kaya L1.

- **Analogi**: L1 itu kayak lo ngilangin barang-barang di kamar yang nggak lo pakai lagi biar kamar lo lebih rapi (hapus total). L2 itu kayak lo masih nyimpen barang-barang, tapi lo taruh rapi dan bikin ruangan lebih efisien (ngurangin tapi nggak hapus total).
---
### 13. [E] Kenapa Performa Model ML Menurun di Produksi?
- Ada beberapa alasan kenapa performa model menurun saat di produksi:
  - **Data Drift**: Data yang digunakan waktu training berbeda sama data yang dipakai di dunia nyata. Misalnya, lo latih model buat rekomendasi belanja di tahun 2023, tapi tren belanja di 2024 berubah, jadi model lo ketinggalan.
  - **Overfitting**: Model terlalu “pinter” di data training, tapi nggak bisa generalisasi di data produksi.
  - **Perubahan Sistem**: Kalau ada update atau perubahan di sistem yang mengelola model (misalnya software), bisa bikin performa menurun.
  - **Skalabilitas**: Model bisa jalan baik di testing, tapi ketika diterapkan di skala besar (misalnya ratusan ribu request per detik), performa bisa turun karena keterbatasan resource.
---
### 14. [M] Masalah Apa yang Mungkin Muncul Saat Deploy Model Machine Learning Besar?
- **Latensi Tinggi**: Model yang besar bisa lambat buat ngasih prediksi, terutama kalau dipakai di aplikasi real-time. 
- **Konsumsi Resource Tinggi**: Model yang besar butuh lebih banyak memory dan computational power, jadi lo mungkin perlu upgrade hardware atau pake cloud service yang mahal.
- **Skalabilitas**: Model besar mungkin bisa ngasih performa oke di testing, tapi di produksi (misal ketika banyak pengguna) bisa jadi masalah, kayak terlalu banyak request buat model.
- **Compatibility**: Model bisa dilatih di lingkungan tertentu, tapi waktu lo deploy ke production environment, bisa aja ada perbedaan yang bikin error (misalnya dependency atau framework yang nggak support).
---
### 15. Performanya Bagus di Test Set tapi Jelek di Produksi

#### i. [M] Hipotesis lo tentang penyebabnya?
- **Data Mismatch**: Data yang dipakai buat training beda sama data di produksi. Misalnya, ada fitur yang hilang, atau distribusi data yang berubah (data drift).
- **Overfitting**: Model lo terlalu fokus di detail-detail data training, tapi nggak bisa generalisasi di data produksi.
- **Latency Issues**: Di produksi, ada bottleneck di waktu inferensi model (misalnya, proses prediksi yang terlalu lambat).
- **Deployment Issues**: Model mungkin nggak di-deploy dengan benar, misalnya ada bug atau incompatibility dengan software lain.

#### ii. [H] Gimana lo validasi apakah hipotesis lo benar?
- **Logging dan Monitoring**: Pasang log di setiap bagian pipeline produksi buat lihat apa yang salah. Misalnya, apakah model dapet input yang bener? Apakah ada bottleneck di computational power?
- **A/B Testing**: Deploy model lo secara bertahap ke beberapa pengguna (misal 10% audience) buat lihat apakah performanya menurun dibanding model lama.
- **Data Validation**: Cek apakah data di produksi sesuai sama yang lo pakai waktu training. Lihat apakah ada perubahan distribusi atau fitur yang hilang.

#### iii. [M] Kalau hipotesis lo benar, gimana lo perbaikinya?
- **Update Model**: Kalau masalahnya di **data drift**, lo bisa retrain model pakai data yang lebih baru atau lebih relevan.
- **Regularization**: Kalau masalahnya **overfitting**, lo bisa tambahin regularization atau tambahin data augmentation biar model lebih generalize.
- **Optimasi Latency**: Kalau masalah di **latency**, lo bisa coba buat **model compression** (misalnya, quantization) atau pake teknik **distributed inference**.
- **Fix Deployment Process**: Kalau ada masalah di **deployment**, cek ulang semua dependency dan environment tempat lo deploy model.