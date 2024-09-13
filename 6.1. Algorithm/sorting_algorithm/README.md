# Insertion Sort
Insertion Sort bekerja dengan membandingkan elemen saat ini dengan elemen sebelumnya dan menggesernya ke posisi yang tepat.

```py
def insertion_sort(arr):
    for i in range(1, len(arr)):  # (1)
        key = arr[i]  # (2)
        j = i - 1  # (3)
        while j >= 0 and key < arr[j]:  # (4)
            arr[j + 1] = arr[j]  # (5)
            j -= 1  # (6)
        arr[j+1] = key  # (7)
    return arr  # (8)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (9)
print(insertion_sort(arr))  # (10)
```

### Penjelasan Setiap Baris

1. **`for i in range(1, len(arr)):`**
   - **Tujuan**: Perulangan dimulai dari elemen kedua (`i = 1`) hingga elemen terakhir dalam array. `i` berfungsi sebagai index yang menunjuk elemen yang sedang di-"insert" ke bagian yang sudah terurut sebelumnya (dari `0` sampai `i-1`).
   - **Nilai**: `i` akan mengambil nilai 1 hingga 7 (sesuai panjang array).

2. **`key = arr[i]`**
   - **Tujuan**: `key` menyimpan nilai elemen array yang saat ini akan dipindahkan ke posisi yang tepat di subarray yang sudah terurut.
   - **Contoh**: Pada iterasi pertama (`i=1`), `key` adalah `34`, karena elemen kedua dari array adalah 34 (`arr[1] = 34`).

3. **`j = i - 1`**
   - **Tujuan**: `j` menunjuk indeks elemen yang ada di sebelah kiri elemen `key`. Ini digunakan untuk membandingkan elemen di subarray terurut dengan `key`.
   - **Contoh**: Ketika `i = 1`, `j = 0`, karena kita mulai membandingkan elemen sebelum `key`.

4. **`while j >= 0 and key < arr[j]:`**
   - **Tujuan**: Selama `j` lebih besar dari atau sama dengan 0 (artinya masih ada elemen di sebelah kiri untuk dibandingkan) dan `key` lebih kecil dari elemen pada `arr[j]`, kita akan menggeser elemen `arr[j]` satu posisi ke kanan. Hal ini dilakukan untuk menemukan posisi yang tepat untuk `key`.
   - **Contoh**: Saat `i = 1` dan `key = 34`, `arr[0]` adalah 64. Karena 34 lebih kecil dari 64, maka `while` dieksekusi dan elemen 64 digeser ke kanan.

5. **`arr[j + 1] = arr[j]`**
   - **Tujuan**: Elemen `arr[j]` digeser satu posisi ke kanan. Ini menciptakan ruang untuk memasukkan `key` pada posisi yang tepat.
   - **Contoh**: Saat `i = 1` dan `key = 34`, elemen `64` di `arr[0]` dipindahkan ke `arr[1]`, membuat array sementara menjadi `[64, 64, 25, 12, 22, 11, 90, 1]`.

6. **`j -= 1`**
   - **Tujuan**: `j` dikurangi satu untuk melanjutkan pengecekan elemen sebelumnya (dalam subarray terurut) dengan `key`.
   - **Contoh**: Setelah menggeser elemen 64, `j` menjadi -1. Karena -1 tidak lebih besar atau sama dengan 0, loop `while` berhenti.

7. **`arr[j + 1] = key`**
   - **Tujuan**: Setelah loop `while` selesai, `key` ditempatkan di posisi yang benar dalam subarray yang terurut.
   - **Contoh**: Pada iterasi pertama, `key` yang bernilai 34 ditempatkan pada posisi `j+1 = 0`, sehingga array sekarang menjadi `[34, 64, 25, 12, 22, 11, 90, 1]`.

8. **`return arr`**
   - **Tujuan**: Setelah seluruh array diurutkan, array yang sudah terurut dikembalikan sebagai output.

9. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
   - **Tujuan**: Ini adalah array input yang akan diurutkan oleh algoritma.

10. **`print(insertion_sort(arr))`**
    - **Output**: Algoritma menyelesaikan pengurutan, dan array yang sudah diurutkan dicetak. Output akhirnya adalah:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Urutan Pada Setiap Iterasi:

- **Iterasi 1**: `i = 1`, `key = 34`, array menjadi `[34, 64, 25, 12, 22, 11, 90, 1]`
- **Iterasi 2**: `i = 2`, `key = 25`, array menjadi `[25, 34, 64, 12, 22, 11, 90, 1]`
- **Iterasi 3**: `i = 3`, `key = 12`, array menjadi `[12, 25, 34, 64, 22, 11, 90, 1]`
- **Iterasi 4**: `i = 4`, `key = 22`, array menjadi `[12, 22, 25, 34, 64, 11, 90, 1]`
- **Iterasi 5**: `i = 5`, `key = 11`, array menjadi `[11, 12, 22, 25, 34, 64, 90, 1]`
- **Iterasi 6**: `i = 6`, `key = 90`, array tetap sama `[11, 12, 22, 25, 34, 64, 90, 1]` (karena 90 sudah di posisi yang benar).
- **Iterasi 7**: `i = 7`, `key = 1`, array menjadi `[1, 11, 12, 22, 25, 34, 64, 90]`

Itulah prosesnya! Algoritma ini bekerja dengan cara mengambil satu elemen pada satu waktu dan menempatkannya pada posisi yang tepat dalam subarray yang sudah terurut.
'''

---

# Selection Sort
Selection Sort memilih elemen terkecil dari array dan menukarnya dengan elemen pada posisi pertama, lalu mengulangi untuk posisi berikutnya.

```py
def selection_sort(arr):
    for i in range(len(arr)):  # (1)
        min_idx = i  # (2)
        for j in range(i + 1, len(arr)):  # (3)
            if arr[j] < arr[min_idx]:  # (4)
                min_idx = j  # (5)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # (6)
    return arr  # (7)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (8)
print(selection_sort(arr))  # (9)
```

### Penjelasan Setiap Baris

1. **`for i in range(len(arr)):`**
   - **Tujuan**: Melakukan iterasi `i` dari indeks pertama (`i = 0`) sampai indeks terakhir dalam array. Pada setiap iterasi, elemen pada indeks `i` dianggap sebagai elemen yang akan ditempatkan di posisi yang benar.
   - **Nilai**: `i` mengambil nilai dari 0 hingga 7 (sesuai panjang array).

2. **`min_idx = i`**
   - **Tujuan**: Inisialisasi `min_idx` dengan nilai `i`, yang menandakan bahwa elemen pada indeks `i` dianggap sementara sebagai elemen terkecil di subarray dari `i` ke `len(arr) - 1`.
   - **Contoh**: Pada iterasi pertama (`i = 0`), `min_idx = 0`, yang berarti elemen pada `arr[0]` (yaitu 64) sementara dianggap sebagai elemen terkecil.

3. **`for j in range(i + 1, len(arr)):`**
   - **Tujuan**: Loop ini melakukan iterasi untuk mencari elemen terkecil di subarray mulai dari indeks `i+1` hingga akhir array.
   - **Contoh**: Jika `i = 0`, `j` akan berjalan dari 1 sampai 7 untuk membandingkan semua elemen setelah `arr[0]`.

4. **`if arr[j] < arr[min_idx]:`**
   - **Tujuan**: Mengecek apakah elemen pada indeks `j` lebih kecil dari elemen pada indeks `min_idx`. Jika ya, maka `min_idx` diperbarui ke indeks `j`, karena elemen pada `j` lebih kecil.
   - **Contoh**: Saat `i = 0`, `j = 7`, nilai `arr[7]` (yaitu 1) lebih kecil dari `arr[0]` (yaitu 64), maka `min_idx` akan di-update menjadi 7.

5. **`min_idx = j`**
   - **Tujuan**: Memperbarui `min_idx` ke nilai `j` jika kondisi pada baris 4 terpenuhi, sehingga sekarang indeks `min_idx` menunjukkan elemen terkecil yang ditemukan sejauh ini.
   - **Contoh**: Saat `i = 0` dan `j = 7`, `min_idx` diperbarui menjadi 7, karena 1 adalah elemen terkecil.

6. **`arr[i], arr[min_idx] = arr[min_idx], arr[i]`**
   - **Tujuan**: Setelah loop `j` selesai, elemen terkecil di subarray dari `i` sampai `len(arr)-1` ditukar dengan elemen pada indeks `i`. Ini memastikan bahwa elemen terkecil berada di posisi yang benar pada setiap iterasi.
   - **Contoh**: Pada iterasi pertama, `arr[0]` ditukar dengan `arr[7]`, jadi array berubah dari `[64, 34, 25, 12, 22, 11, 90, 1]` menjadi `[1, 34, 25, 12, 22, 11, 90, 64]`.

7. **`return arr`**
   - **Tujuan**: Mengembalikan array yang sudah terurut setelah seluruh proses sorting selesai.

8. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
   - **Tujuan**: Array input yang akan diurutkan.

9. **`print(selection_sort(arr))`**
   - **Output**: Setelah algoritma Selection Sort selesai, array yang sudah terurut dicetak. Output akhirnya adalah:
   ```
   [1, 11, 12, 22, 25, 34, 64, 90]
   ```

### Proses Urutan Pada Setiap Iterasi:

- **Iterasi 1 (i = 0)**: 
   - `min_idx = 7` (karena 1 adalah elemen terkecil), array menjadi `[1, 34, 25, 12, 22, 11, 90, 64]`
- **Iterasi 2 (i = 1)**: 
   - `min_idx = 5` (karena 11 adalah elemen terkecil di subarray mulai dari `i = 1`), array menjadi `[1, 11, 25, 12, 22, 34, 90, 64]`
- **Iterasi 3 (i = 2)**: 
   - `min_idx = 3` (karena 12 adalah elemen terkecil di subarray mulai dari `i = 2`), array menjadi `[1, 11, 12, 25, 22, 34, 90, 64]`
- **Iterasi 4 (i = 3)**: 
   - `min_idx = 4` (karena 22 adalah elemen terkecil di subarray mulai dari `i = 3`), array menjadi `[1, 11, 12, 22, 25, 34, 90, 64]`
- **Iterasi 5 (i = 4)**: 
   - `min_idx = 4` (25 sudah di posisi yang benar, tidak ada perubahan), array tetap `[1, 11, 12, 22, 25, 34, 90, 64]`
- **Iterasi 6 (i = 5)**: 
   - `min_idx = 5` (34 sudah di posisi yang benar, tidak ada perubahan), array tetap `[1, 11, 12, 22, 25, 34, 90, 64]`
- **Iterasi 7 (i = 6)**: 
   - `min_idx = 7` (karena 64 lebih kecil dari 90), array menjadi `[1, 11, 12, 22, 25, 34, 64, 90]`
- **Iterasi 8 (i = 7)**: 
   - Tidak ada perubahan karena `i = 7` adalah iterasi terakhir.

### Logika Utama Selection Sort

- Pada setiap iterasi, algoritma mencari elemen terkecil di subarray yang belum diurutkan dan menukarnya dengan elemen pada indeks `i`.
- Proses ini memastikan bahwa pada setiap iterasi, elemen terkecil ditempatkan di posisi yang benar.
'''

---
# Merge Sort
Merge Sort membagi array menjadi sub-array kecil, kemudian menggabungkannya kembali dengan urutan yang benar.

```py
def merge_sort(arr):
    if len(arr) > 1:  # (1)
        mid = len(arr) // 2  # (2)
        left_half = arr[:mid]  # (3)
        right_half = arr[mid:]  # (4)

        merge_sort(left_half)  # (5)
        merge_sort(right_half)  # (6)

        i = j = k = 0  # (7)
        while i < len(left_half) and j < len(right_half):  # (8)
            if left_half[i] < right_half[j]:  # (9)
                arr[k] = left_half[i]  # (10)
                i += 1  # (11)
            else:
                arr[k] = right_half[j]  # (12)
                j += 1  # (13)
            k += 1  # (14)

        while i < len(left_half):  # (15)
            arr[k] = left_half[i]  # (16)
            i += 1  # (17)
            k += 1  # (18)

        while j < len(right_half):  # (19)
            arr[k] = right_half[j]  # (20)
            j += 1  # (21)
            k += 1  # (22)
    return arr  # (23)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (24)
print(merge_sort(arr))  # (25)
```

1. **`if len(arr) > 1:`**
   - **Tujuan**: Mengecek apakah panjang array lebih dari 1. Jika array hanya berisi satu elemen, ia sudah dianggap terurut. Jika lebih dari 1, kita perlu membagi array tersebut.
   - **Contoh**: Pada awalnya, `arr` memiliki 8 elemen, sehingga proses pembagian akan dilanjutkan.

2. **`mid = len(arr) // 2`**
   - **Tujuan**: Mencari titik tengah dari array untuk membaginya menjadi dua bagian.
   - **Contoh**: Untuk array dengan 8 elemen, `mid` akan menjadi 4.

3. **`left_half = arr[:mid]`**
   - **Tujuan**: Membagi array menjadi setengah bagian kiri.
   - **Contoh**: Dengan `mid = 4`, `left_half` akan menjadi `[64, 34, 25, 12]`.

4. **`right_half = arr[mid:]`**
   - **Tujuan**: Membagi array menjadi setengah bagian kanan.
   - **Contoh**: Dengan `mid = 4`, `right_half` akan menjadi `[22, 11, 90, 1]`.

5. **`merge_sort(left_half)`**
   - **Tujuan**: Memanggil rekursi `merge_sort` pada bagian kiri array untuk terus membaginya hingga menjadi subarray yang berisi satu elemen.

6. **`merge_sort(right_half)`**
   - **Tujuan**: Memanggil rekursi `merge_sort` pada bagian kanan array untuk terus membaginya hingga menjadi subarray yang berisi satu elemen.

7. **`i = j = k = 0`**
   - **Tujuan**: Inisialisasi variabel indeks untuk menggabungkan kembali dua bagian array (`left_half` dan `right_half`) ke array asli (`arr`).
   - **Contoh**: `i` untuk indeks `left_half`, `j` untuk `right_half`, dan `k` untuk array `arr`.

8. **`while i < len(left_half) and j < len(right_half):`**
   - **Tujuan**: Melakukan iterasi membandingkan elemen-elemen dari `left_half` dan `right_half` untuk digabungkan kembali ke `arr`.
   - **Contoh**: Jika `left_half = [12, 25, 34, 64]` dan `right_half = [1, 11, 22, 90]`, kita akan membandingkan setiap elemen dari kedua array.

9. **`if left_half[i] < right_half[j]:`**
   - **Tujuan**: Jika elemen di `left_half[i]` lebih kecil dari elemen di `right_half[j]`, maka elemen `left_half[i]` ditempatkan ke `arr`.

10. **`arr[k] = left_half[i]`**
    - **Tujuan**: Menyalin elemen `left_half[i]` ke `arr[k]` jika kondisi pada baris 9 terpenuhi.

11. **`i += 1`**
    - **Tujuan**: Memperbarui indeks `i` setelah menyalin elemen dari `left_half` ke `arr`.

12. **`arr[k] = right_half[j]`**
    - **Tujuan**: Jika kondisi di baris 9 tidak terpenuhi, elemen `right_half[j]` yang lebih kecil ditempatkan di `arr[k]`.

13. **`j += 1`**
    - **Tujuan**: Memperbarui indeks `j` setelah menyalin elemen dari `right_half` ke `arr`.

14. **`k += 1`**
    - **Tujuan**: Memperbarui indeks `k` setelah menempatkan elemen dari `left_half` atau `right_half` ke array `arr`.

15. **`while i < len(left_half):`**
    - **Tujuan**: Menangani sisa elemen dari `left_half` jika masih ada elemen yang belum dipindahkan ke array `arr`.

16. **`arr[k] = left_half[i]`**
    - **Tujuan**: Menyalin elemen sisa dari `left_half` ke `arr` jika `while` pada baris 8 selesai.

17. **`i += 1`**
    - **Tujuan**: Memperbarui indeks `i` setelah menyalin elemen dari `left_half`.

18. **`k += 1`**
    - **Tujuan**: Memperbarui indeks `k` setelah menyalin elemen dari `left_half`.

19. **`while j < len(right_half):`**
    - **Tujuan**: Menangani sisa elemen dari `right_half` jika masih ada elemen yang belum dipindahkan ke array `arr`.

20. **`arr[k] = right_half[j]`**
    - **Tujuan**: Menyalin elemen sisa dari `right_half` ke `arr`.

21. **`j += 1`**
    - **Tujuan**: Memperbarui indeks `j` setelah menyalin elemen dari `right_half`.

22. **`k += 1`**
    - **Tujuan**: Memperbarui indeks `k` setelah menyalin elemen dari `right_half`.

23. **`return arr`**
    - **Tujuan**: Mengembalikan array yang sudah terurut.

24. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

25. **`print(merge_sort(arr))`**
    - **Output**: Setelah algoritma Merge Sort selesai, array yang sudah terurut dicetak:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Iterasi Utama:

1. **Pembagian Array**:
   - Awalnya, `arr` dibagi menjadi dua: `[64, 34, 25, 12]` dan `[22, 11, 90, 1]`.
   - Subarray ini terus dibagi sampai tersisa elemen tunggal:
     - `[64, 34, 25, 12]` → `[64, 34]` dan `[25, 12]` → `[64]`, `[34]`, `[25]`, `[12]`.
     - `[22, 11, 90, 1]` → `[22, 11]` dan `[90, 1]` → `[22]`, `[11]`, `[90]`, `[1]`.

2. **Penggabungan Array**:
   - Setiap subarray tunggal digabung kembali dengan membandingkan elemen-elemen dari `left_half` dan `right_half`.
   - **Contoh Penggabungan**:
     - `[64]` dan `[34]` → `[34, 64]`.
     - `[25]` dan `[12]` → `[12, 25]`.
     - `[34, 64]` dan `[12, 25]` → `[12, 25, 34, 64]`.
     - Proses ini berlanjut hingga array sepenuhnya terurut.

### Logika Utama Merge Sort

- **Divide and Conquer**: Algoritma ini bekerja dengan membagi array menjadi bagian kecil, lalu menggabungkannya kembali dengan cara yang terurut.
- Merge Sort memiliki **kompleksitas waktu O(n log n)**, karena setiap kali array dibagi menjadi dua (log n), dan kita perlu menggabungkan array tersebut (O(n)).
'''

---

### 1. **Algoritma yang Paling Cepat:**
Secara umum, algoritma **paling cepat** untuk *average case* diantaranya:

- **Quick Sort**: 
  - **Average Case Time Complexity**: \(O(n \log n)\)
  - **Worst Case**: \(O(n^2)\), tapi ini jarang terjadi kalau kita pakai optimisasi (misalnya, pilih pivot secara acak).
  - **Paling cepat** untuk *average case* karena pembagian dan penaklukan (divide and conquer) yang efisien. 

- **Merge Sort**:
  - **Time Complexity**: \(O(n \log n)\) di semua kasus.
  - Merge sort punya jaminan stabilitas dan selalu \(O(n \log n)\), walau nggak secepat Quick Sort di kebanyakan kasus praktis.

- **Heap Sort**:
  - **Time Complexity**: \(O(n \log n)\) di semua kasus.
  - Memori lebih efisien dibanding Merge Sort, tapi lebih lambat dibanding Quick Sort.

### 2. **Algoritma yang Paling Lambat:**
Beberapa algoritma lebih lambat, terutama untuk dataset besar atau ketika ada banyak elemen:

- **Bubble Sort**: 
  - **Time Complexity**: \(O(n^2)\)
  - Paling lambat, karena harus melakukan banyak perbandingan dan pertukaran elemen, jadi biasanya cuma diajarin sebagai konsep dasar, jarang dipakai di industri.

- **Selection Sort**:
  - **Time Complexity**: \(O(n^2)\)
  - Meski sedikit lebih baik dari Bubble Sort karena jumlah pertukarannya lebih sedikit, tetap aja lambat di dataset besar.

- **Insertion Sort**: 
  - **Time Complexity**: \(O(n^2)\) dalam kasus terburuk, tapi **bagus untuk dataset kecil** atau hampir terurut.
  - Dalam kasus dataset kecil atau hampir terurut, Insertion Sort bisa lebih cepat dari algoritma lain yang lebih kompleks, karena overhead-nya rendah.

### 3. **Sorting Algoritma yang Paling Populer di Kalangan Profesional:**
- **Quick Sort** adalah yang paling populer, terutama karena kecepatan rata-ratanya \(O(n \log n)\) dan penggunaan memori yang efisien.
  - Sering dipakai di aplikasi sehari-hari dan biasanya jadi *default sorting algorithm* di banyak bahasa pemrograman kayak C++ (`std::sort`).

- **Merge Sort** sangat populer dalam kasus di mana stabilitas sorting penting (misalnya, elemen-elemen yang sama tetap dalam urutan yang sama seperti sebelum disortir).
  - Contoh di Python, `sorted()` dan `list.sort()` menggunakan **Timsort**, yang merupakan gabungan dari Merge Sort dan Insertion Sort.

- **Counting Sort**, **Radix Sort**, dan **Bucket Sort** dipakai saat kita tahu rentang nilai data yang terbatas (misalnya, kalau kita mengurutkan nilai integer dalam rentang kecil). 
  - Ini sering dipakai dalam aplikasi yang memerlukan sorting dalam waktu konstan seperti di pemrosesan citra atau masalah khusus.

### 4. **Kesimpulan dari Profesional:**
- **Cepat dan Efisien (Populer)**: **Quick Sort** dan **Merge Sort**.
- **Cepat untuk Kasus Khusus**: **Counting Sort**, **Radix Sort**, **Bucket Sort** (untuk data integer dengan rentang terbatas).
- **Lambat**: **Bubble Sort**, **Selection Sort**, **Insertion Sort** (tapi bisa efisien untuk dataset kecil).