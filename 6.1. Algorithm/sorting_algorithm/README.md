# 1. Insertion Sort
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

# 2. Selection Sort
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
# 3. Merge Sort
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

---
# 4. Heap Sort

Heap Sort membangun heap dari array dan kemudian melakukan sorting dengan mengekstrak elemen terbesar dan menempatkannya pada posisi akhir.

```python
def heapify(arr, n, i):  # (1)
    largest = i  # (2)
    left = 2 * i + 1  # (3)
    right = 2 * i + 2  # (4)

    if left < n and arr[i] < arr[left]:  # (5)
        largest = left  # (6)

    if right < n and arr[largest] < arr[right]:  # (7)
        largest = right  # (8)

    if largest != i:  # (9)
        arr[i], arr[largest] = arr[largest], arr[i]  # (10)
        heapify(arr, n, largest)  # (11)

def heap_sort(arr):  # (12)
    n = len(arr)  # (13)

    for i in range(n // 2 - 1, -1, -1):  # (14)
        heapify(arr, n, i)  # (15)

    for i in range(n - 1, 0, -1):  # (16)
        arr[i], arr[0] = arr[0], arr[i]  # (17)
        heapify(arr, i, 0)  # (18)

    return arr  # (19)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (20)
print(heap_sort(arr))  # (21)
```

### Penjelasan Setiap Baris

#### Fungsi **heapify(arr, n, i)**

1. **`def heapify(arr, n, i):`**
   - **Tujuan**: Membuat sebuah heap (binary heap) dengan elemen terbesar di root. Ini dikenal sebagai "max-heapify".
   - **Contoh**: Untuk array `[64, 34, 25, 12, 22, 11, 90, 1]` dengan `n = 8` dan `i = 0`, kita mulai membangun heap.

2. **`largest = i`**
   - **Tujuan**: Menyimpan indeks dari elemen terbesar. Pada awalnya, diasumsikan bahwa elemen di indeks `i` adalah yang terbesar.

3. **`left = 2 * i + 1`**
   - **Tujuan**: Menghitung indeks dari anak kiri node dengan indeks `i` dalam binary heap.
   - **Contoh**: Untuk `i = 0`, `left = 1`.

4. **`right = 2 * i + 2`**
   - **Tujuan**: Menghitung indeks dari anak kanan node dengan indeks `i`.
   - **Contoh**: Untuk `i = 0`, `right = 2`.

5. **`if left < n and arr[i] < arr[left]:`**
   - **Tujuan**: Mengecek apakah anak kiri `left` lebih besar dari elemen induknya di `i`.
   - **Contoh**: Jika `left = 1` dan `arr[1]` lebih besar dari `arr[0]`, `largest` akan diperbarui.

6. **`largest = left`**
   - **Tujuan**: Jika anak kiri lebih besar dari induknya, maka `largest` di-update menjadi indeks `left`.

7. **`if right < n and arr[largest] < arr[right]:`**
   - **Tujuan**: Mengecek apakah anak kanan `right` lebih besar dari elemen terbesar saat ini (antara `i` dan anak kiri).
   - **Contoh**: Jika `right = 2` dan `arr[2]` lebih besar dari `arr[largest]`, `largest` diperbarui.

8. **`largest = right`**
   - **Tujuan**: Jika anak kanan lebih besar dari `largest`, maka `largest` di-update menjadi `right`.

9. **`if largest != i:`**
   - **Tujuan**: Jika elemen terbesar bukan elemen induk, maka dilakukan penukaran posisi antara elemen terbesar dan induknya.

10. **`arr[i], arr[largest] = arr[largest], arr[i]`**
    - **Tujuan**: Menukar elemen di indeks `i` dengan elemen di indeks `largest`.

11. **`heapify(arr, n, largest)`**
    - **Tujuan**: Rekursi untuk memastikan bahwa sub-tree yang baru ditukar juga memenuhi aturan heap.

#### Fungsi **heap_sort(arr)**

12. **`def heap_sort(arr):`**
    - **Tujuan**: Fungsi utama untuk melakukan Heap Sort.

13. **`n = len(arr)`**
    - **Tujuan**: Menyimpan panjang array.

14. **`for i in range(n // 2 - 1, -1, -1):`**
    - **Tujuan**: Membuat heap dari array, dimulai dari node non-daun (bagian bawah ke atas).

15. **`heapify(arr, n, i)`**
    - **Tujuan**: Memanggil fungsi `heapify` untuk memastikan sub-tree dengan root di `i` adalah heap.

16. **`for i in range(n - 1, 0, -1):`**
    - **Tujuan**: Setelah heap terbentuk, elemen terbesar (di root) dipindahkan ke akhir array, dan sisa array di-heapify lagi untuk menemukan elemen terbesar berikutnya.

17. **`arr[i], arr[0] = arr[0], arr[i]`**
    - **Tujuan**: Menukar elemen terbesar (root) dengan elemen terakhir dari array.

18. **`heapify(arr, i, 0)`**
    - **Tujuan**: Heapify sisa array, kecuali elemen terakhir yang sudah dipindahkan ke tempat yang benar.

19. **`return arr`**
    - **Tujuan**: Mengembalikan array yang sudah terurut.

20. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

21. **`print(heap_sort(arr))`**
    - **Output**: Setelah algoritma Heap Sort selesai, array yang sudah terurut dicetak:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Utama dalam Heap Sort:

1. **Membangun Heap**:
   - Heap Sort memulai dengan membangun **max-heap** dari array input.
   - Max-heap adalah binary heap di mana setiap node lebih besar dari kedua anaknya, dan elemen terbesar selalu berada di root.

2. **Penukaran dan Pengurutan**:
   - Setelah heap terbentuk, elemen terbesar (root) dipindahkan ke akhir array.
   - Heap diatur ulang untuk elemen yang tersisa dan proses ini diulang sampai array terurut.

### Proses Heapify:

- **Heapify** dimulai dari node non-daun yang paling bawah (di indeks `n // 2 - 1`) dan berjalan mundur ke root. Setiap kali menemukan elemen yang lebih kecil dari salah satu anaknya, elemen tersebut ditukar, dan proses ini diulang untuk memastikan heap memenuhi aturan max-heap.

### Contoh Langkah Heap Sort:

1. **Array Awal**: `[64, 34, 25, 12, 22, 11, 90, 1]`
2. **Max-Heap Awal**: Setelah heapify:
   ```
   [90, 64, 25, 34, 22, 11, 12, 1]
   ```
3. **Penukaran 1**: Elemen `90` (root) ditukar dengan elemen terakhir `1`:
   ```
   [1, 64, 25, 34, 22, 11, 12, 90]
   ```
   Lalu di-heapify lagi:
   ```
   [64, 34, 25, 1, 22, 11, 12, 90]
   ```

4. **Penukaran 2**: Elemen `64` ditukar dengan `12`:
   ```
   [12, 34, 25, 1, 22, 11, 64, 90]
   ```
   Lalu di-heapify lagi:
   ```
   [34, 22, 25, 1, 12, 11, 64, 90]
   ```

5. **Proses ini berlanjut** hingga seluruh array terurut menjadi:
   ```
   [1, 11, 12, 22, 25, 34, 64, 90]
   ```

### Kompleksitas Waktu Heap Sort:

- **Worst-case time complexity**: O(n log n) karena untuk setiap elemen kita perlu melakukan operasi heapify yang memiliki kompleksitas logaritmik, dan proses ini dilakukan untuk n elemen.

---
# 5. Quick Sort

Quick Sort menggunakan pivot untuk membagi array menjadi dua bagian dan kemudian melakukan sorting secara rekursif.

```python
def partition(arr, low, high):  # (1)
    pivot = arr[high]  # (2)
    i = low - 1  # (3)
    for j in range(low, high):  # (4)
        if arr[j] <= pivot:  # (5)
            i += 1  # (6)
            arr[i], arr[j] = arr[j], arr[i]  # (7)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # (8)
    return i + 1  # (9)

def quick_sort(arr, low, high):  # (10)
    if low < high:  # (11)
        pivot = partition(arr, low, high)  # (12)
        quick_sort(arr, low, pivot - 1)  # (13)
        quick_sort(arr, pivot + 1, high)  # (14)
    return arr  # (15)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (16)
print(quick_sort(arr, 0, len(arr) - 1))  # (17)
```

### Penjelasan Setiap Baris

#### Fungsi **partition(arr, low, high)**

1. **`def partition(arr, low, high):`**
   - **Tujuan**: Fungsi ini digunakan untuk membagi array menjadi dua bagian berdasarkan **pivot** dan mengembalikan indeks posisi dari pivot yang telah dipindahkan ke posisi yang benar.

2. **`pivot = arr[high]`**
   - **Tujuan**: Pivot adalah elemen terakhir dari subarray yang diproses saat ini.
   - **Contoh**: Untuk array `[64, 34, 25, 12, 22, 11, 90, 1]` dan `high = 7`, pivot adalah `1`.

3. **`i = low - 1`**
   - **Tujuan**: Menyiapkan indeks `i` yang menunjukkan posisi elemen terakhir yang lebih kecil atau sama dengan pivot.

4. **`for j in range(low, high):`**
   - **Tujuan**: Iterasi melalui elemen array dari indeks `low` hingga `high - 1`.

5. **`if arr[j] <= pivot:`**
   - **Tujuan**: Memeriksa apakah elemen array `arr[j]` lebih kecil atau sama dengan pivot.

6. **`i += 1`**
   - **Tujuan**: Jika elemen `arr[j]` lebih kecil dari atau sama dengan pivot, kita meningkatkan indeks `i` untuk menunjukkan bahwa elemen yang lebih kecil ini telah ditemukan.

7. **`arr[i], arr[j] = arr[j], arr[i]`**
   - **Tujuan**: Menukar elemen `arr[i]` dengan elemen `arr[j]` sehingga elemen yang lebih kecil dari pivot berada di sebelah kiri.

8. **`arr[i + 1], arr[high] = arr[high], arr[i + 1]`**
   - **Tujuan**: Setelah iterasi selesai, menukar pivot dengan elemen pertama yang lebih besar dari pivot, sehingga pivot berada di posisi yang benar dalam array.

9. **`return i + 1`**
   - **Tujuan**: Mengembalikan indeks pivot setelah diposisikan dengan benar.

#### Fungsi **quick_sort(arr, low, high)**

10. **`def quick_sort(arr, low, high):`**
    - **Tujuan**: Fungsi utama untuk mengurutkan array menggunakan algoritma **Quick Sort**.

11. **`if low < high:`**
    - **Tujuan**: Kondisi rekursif, memastikan bahwa array yang akan diurutkan memiliki lebih dari satu elemen.

12. **`pivot = partition(arr, low, high)`**
    - **Tujuan**: Memanggil fungsi `partition` untuk mengatur posisi pivot dan membagi array menjadi dua bagian.

13. **`quick_sort(arr, low, pivot - 1)`**
    - **Tujuan**: Melakukan rekursi untuk mengurutkan bagian kiri array, yaitu elemen-elemen yang lebih kecil dari pivot.

14. **`quick_sort(arr, pivot + 1, high)`**
    - **Tujuan**: Melakukan rekursi untuk mengurutkan bagian kanan array, yaitu elemen-elemen yang lebih besar dari pivot.

15. **`return arr`**
    - **Tujuan**: Mengembalikan array yang sudah diurutkan.

16. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

17. **`print(quick_sort(arr, 0, len(arr) - 1))`**
    - **Output**: Setelah algoritma Quick Sort selesai, array yang sudah diurutkan akan dicetak:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Utama dalam Quick Sort:

1. **Partitioning**:
   - Pada setiap tahap rekursi, array dipecah menjadi dua bagian dengan memilih **pivot** (elemen terakhir dalam subarray saat ini). Elemen yang lebih kecil dari pivot dipindahkan ke kiri, dan yang lebih besar dipindahkan ke kanan.

2. **Rekursi**:
   - Setelah array dibagi menjadi dua bagian, Quick Sort dipanggil secara rekursif untuk mengurutkan kedua bagian tersebut secara terpisah hingga semua elemen berada di posisi yang benar.

### Contoh Langkah Quick Sort:

1. **Array Awal**: `[64, 34, 25, 12, 22, 11, 90, 1]`
2. **Langkah Pertama (Pivot = 1)**:
   - Setelah partition dengan pivot `1`, array menjadi:
   ```
   [1, 34, 25, 12, 22, 11, 90, 64]
   ```
   Pivot `1` sudah di posisi yang benar.

3. **Langkah Kedua (Pivot = 64)**:
   - Mengurutkan bagian kanan dengan pivot `64`, array menjadi:
   ```
   [1, 11, 25, 12, 22, 34, 64, 90]
   ```

4. **Langkah Ketiga (Pivot = 11)**:
   - Mengurutkan bagian kiri dengan pivot `11`, array menjadi:
   ```
   [1, 11, 25, 12, 22, 34, 64, 90]
   ```

5. **Langkah Keempat (Pivot = 34)**:
   - Mengurutkan bagian kiri lagi dengan pivot `34`, array menjadi:
   ```
   [1, 11, 12, 22, 25, 34, 64, 90]
   ```

6. **Proses selesai** dan array terurut menjadi:
   ```
   [1, 11, 12, 22, 25, 34, 64, 90]
   ```

### Kompleksitas Waktu Quick Sort:

- **Worst-case time complexity**: O(n²), terjadi jika pivot selalu elemen terbesar atau terkecil (misalnya, jika array sudah terurut).
- **Average-case time complexity**: O(n log n), yang merupakan kompleksitas rata-rata dalam banyak kasus.

### Kesimpulan:
Algoritma **Quick Sort** sangat cepat dan efisien dalam mengurutkan array, terutama ketika memilih pivot yang baik sehingga membagi array menjadi dua bagian yang seimbang.

---
# 6. Counting Sort

Counting Sort bekerja dengan menghitung kemunculan setiap elemen dan kemudian menempatkannya pada posisi yang tepat.

```python
def counting_sort(arr):  # (1)
    max_val = max(arr)  # (2)
    count = [0] * (max_val + 1)  # (3)
    output = [0] * len(arr)  # (4)

    for num in arr:  # (5)
        count[num] += 1  # (6)

    for i in range(1, len(count)):  # (7)
        count[i] += count[i - 1]  # (8)

    for num in reversed(arr):  # (9)
        output[count[num] - 1] = num  # (10)
        count[num] -= 1  # (11)

    return output  # (12)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (13)
print(counting_sort(arr))  # (14)
```

### Penjelasan Setiap Baris

1. **`def counting_sort(arr):`**
   - **Tujuan**: Mendefinisikan fungsi **Counting Sort** untuk mengurutkan array berdasarkan hitungan frekuensi.

2. **`max_val = max(arr)`**
   - **Tujuan**: Menemukan nilai maksimum dalam array. Ini akan digunakan untuk menentukan ukuran array `count`.
   - **Contoh**: Untuk array `[64, 34, 25, 12, 22, 11, 90, 1]`, `max_val` adalah `90`.

3. **`count = [0] * (max_val + 1)`**
   - **Tujuan**: Membuat array `count` yang berisi nol, dengan panjang `max_val + 1`. Ini digunakan untuk menyimpan jumlah kemunculan setiap elemen dalam array asli.
   - **Contoh**: Dengan `max_val = 90`, array `count` berukuran 91, semuanya nol.

4. **`output = [0] * len(arr)`**
   - **Tujuan**: Membuat array `output` yang kosong dan berukuran sama dengan array asli. Array ini akan diisi dengan elemen-elemen terurut.

5. **`for num in arr:`**
   - **Tujuan**: Iterasi melalui setiap elemen dalam array asli.

6. **`count[num] += 1`**
   - **Tujuan**: Menghitung jumlah kemunculan setiap elemen dalam array asli dan menyimpannya dalam array `count`.
   - **Contoh**: Misal, array `[64, 34, 25, 12, 22, 11, 90, 1]` akan memperbarui `count[64]`, `count[34]`, `count[25]`, dst.

7. **`for i in range(1, len(count)):`**
   - **Tujuan**: Mengubah array `count` menjadi array yang menyimpan posisi elemen-elemen dalam array yang sudah diurutkan.

8. **`count[i] += count[i - 1]`**
   - **Tujuan**: Setiap elemen dalam array `count` diubah menjadi jumlah kumulatif dari elemen-elemen sebelumnya.
   - **Contoh**: Jika `count[1] = 1`, `count[2] = 2`, dst., maka `count[2]` akan berisi posisi `2` dalam array output yang terurut.

9. **`for num in reversed(arr):`**
   - **Tujuan**: Iterasi mundur melalui array asli untuk memastikan stabilitas sorting. Sorting stabil memastikan bahwa elemen-elemen dengan nilai yang sama tetap pada urutan yang sama dengan urutan aslinya.

10. **`output[count[num] - 1] = num`**
    - **Tujuan**: Mengisi array `output` dengan elemen-elemen yang sudah diurutkan berdasarkan posisi yang disimpan dalam array `count`.
    - **Contoh**: Misalnya, jika `count[64] = 6`, maka elemen `64` akan ditempatkan di indeks ke-5 (`output[5]`).

11. **`count[num] -= 1`**
    - **Tujuan**: Mengurangi hitungan di array `count` setelah elemen ditempatkan ke array `output`. Ini memastikan elemen berikutnya dengan nilai yang sama ditempatkan pada posisi yang benar.

12. **`return output`**
    - **Tujuan**: Mengembalikan array yang sudah diurutkan.

#### Bagian Utama Fungsi Counting Sort

13. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

14. **`print(counting_sort(arr))`**
    - **Output**: Array setelah diurutkan menggunakan Counting Sort:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Utama dalam Counting Sort

1. **Inisialisasi `count` dan `output`**:
   - Array `count` disiapkan dengan ukuran sebesar nilai maksimum dalam array `arr`. Setiap indeks dalam `count` menyimpan jumlah elemen dengan nilai tersebut.

2. **Mengisi Array `count`**:
   - Setiap elemen dari array asli (`arr`) diperiksa, dan array `count` diperbarui untuk menyimpan berapa kali setiap elemen muncul.

3. **Membangun Array Kumulatif `count`**:
   - Array `count` diubah menjadi array kumulatif, yang memberi tahu kita posisi akhir dari setiap elemen dalam array output yang sudah diurutkan.

4. **Mengisi Array `output`**:
   - Iterasi mundur digunakan untuk mengisi array `output` dengan elemen-elemen dari array asli berdasarkan posisi yang ditentukan dalam array kumulatif `count`. Ini memastikan sorting stabil.

5. **Mengembalikan Array Terurut**:
   - Array `output` yang berisi elemen-elemen terurut dikembalikan sebagai hasil akhir.

### Contoh Langkah-Langkah Counting Sort

#### Langkah 1: Inisialisasi
- Array input: `[64, 34, 25, 12, 22, 11, 90, 1]`
- `max_val = 90`
- `count = [0] * 91`  (array panjang 91 berisi 0)
- `output = [0] * 8`  (array panjang 8 berisi 0)

#### Langkah 2: Hitung Frekuensi
- Menghitung jumlah kemunculan setiap elemen di `arr` dan mengisi array `count`:
  ```
  count[1] = 1, count[11] = 1, count[12] = 1, count[22] = 1, count[25] = 1, count[34] = 1, count[64] = 1, count[90] = 1
  ```

#### Langkah 3: Array Kumulatif
- Mengubah array `count` menjadi kumulatif untuk menentukan posisi elemen:
  ```
  count[1] = 1, count[11] = 2, count[12] = 3, count[22] = 4, count[25] = 5, count[34] = 6, count[64] = 7, count[90] = 8
  ```

#### Langkah 4: Mengisi Array Output
- Iterasi mundur mengisi array `output`:
  ```
  output[7] = 90, output[6] = 64, output[5] = 34, output[4] = 25, output[3] = 22, output[2] = 12, output[1] = 11, output[0] = 1
  ```

#### Hasil Akhir
- Array terurut: `[1, 11, 12, 22, 25, 34, 64, 90]`

### Kompleksitas Waktu Counting Sort
- **Time complexity**: O(n + k), di mana `n` adalah jumlah elemen dalam array, dan `k` adalah nilai maksimum elemen dalam array.
- **Space complexity**: O(k + n), karena memerlukan array tambahan `count` dan `output`.

### Kesimpulan
**Counting Sort** sangat efisien jika elemen-elemen dalam array memiliki rentang nilai yang kecil, karena memanfaatkan array frekuensi untuk mengurutkan elemen-elemen dalam waktu linear.

---

# 7. Radix Sort

Radix Sort bekerja dengan mengurutkan angka berdasarkan digit dari yang paling sedikit hingga paling banyak.

```python
def counting_sort_for_radix(arr, exp):  # (1)
    n = len(arr)  # (2)
    output = [0] * n  # (3)
    count = [0] * 10  # (4)

    for i in range(n):  # (5)
        index = arr[i] // exp  # (6)
        count[index % 10] += 1  # (7)

    for i in range(1, 10):  # (8)
        count[i] += count[i - 1]  # (9)

    i = n - 1  # (10)
    while i >= 0:  # (11)
        index = arr[i] // exp  # (12)
        output[count[index % 10] - 1] = arr[i]  # (13)
        count[index % 10] -= 1  # (14)
        i -= 1  # (15)

    for i in range(len(arr)):  # (16)
        arr[i] = output[i]  # (17)

def radix_sort(arr):  # (18)
    max_val = max(arr)  # (19)
    exp = 1  # (20)
    while max_val // exp > 0:  # (21)
        counting_sort_for_radix(arr, exp)  # (22)
        exp *= 10  # (23)
    return arr  # (24)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (25)
print(radix_sort(arr))  # (26)
```

### Penjelasan Setiap Baris

1. **`def counting_sort_for_radix(arr, exp):`**
   - **Tujuan**: Fungsi ini merupakan **Counting Sort** yang disesuaikan untuk digunakan pada **Radix Sort**, bekerja pada digit tertentu (`exp`).
   
2. **`n = len(arr)`**
   - **Tujuan**: Mendapatkan panjang array `arr`.

3. **`output = [0] * n`**
   - **Tujuan**: Membuat array `output` berukuran sama dengan `arr` untuk menyimpan hasil sorting sementara.

4. **`count = [0] * 10`**
   - **Tujuan**: Membuat array `count` dengan panjang 10 (karena hanya ada 10 digit, yaitu 0 sampai 9) untuk menyimpan jumlah kemunculan setiap digit.

5. **`for i in range(n):`**
   - **Tujuan**: Iterasi melalui setiap elemen dalam array `arr`.

6. **`index = arr[i] // exp`**
   - **Tujuan**: Menghitung nilai digit yang sedang diproses, berdasarkan posisi digit yang ditentukan oleh `exp` (ekspansi digit).

7. **`count[index % 10] += 1`**
   - **Tujuan**: Meningkatkan hitungan digit yang ditemukan di array `count`. Ini mencatat frekuensi kemunculan digit 0-9.

8. **`for i in range(1, 10):`**
   - **Tujuan**: Iterasi untuk memperbarui array `count` menjadi kumulatif.

9. **`count[i] += count[i - 1]`**
   - **Tujuan**: Mengubah array `count` menjadi kumulatif, sehingga setiap indeks berisi posisi terakhir dari digit yang bersangkutan dalam array yang diurutkan.

10. **`i = n - 1`**
    - **Tujuan**: Inisialisasi variabel `i` untuk iterasi mundur melalui array `arr`.

11. **`while i >= 0:`**
    - **Tujuan**: Iterasi mundur melalui array `arr`.

12. **`index = arr[i] // exp`**
    - **Tujuan**: Menghitung digit yang sedang diproses untuk elemen `arr[i]`.

13. **`output[count[index % 10] - 1] = arr[i]`**
    - **Tujuan**: Menempatkan elemen `arr[i]` pada posisi yang benar dalam array `output` berdasarkan nilai kumulatif dari `count`.

14. **`count[index % 10] -= 1`**
    - **Tujuan**: Mengurangi hitungan di array `count` setelah elemen ditempatkan dalam array `output`.

15. **`i -= 1`**
    - **Tujuan**: Mengurangi `i` untuk iterasi mundur.

16. **`for i in range(len(arr)):`**
    - **Tujuan**: Iterasi melalui setiap elemen dalam array `arr` untuk menyalin hasil dari array `output`.

17. **`arr[i] = output[i]`**
    - **Tujuan**: Menyalin elemen dari array `output` kembali ke array `arr` untuk menyimpan hasil sementara.

18. **`def radix_sort(arr):`**
    - **Tujuan**: Mendefinisikan fungsi **Radix Sort** yang memanfaatkan **Counting Sort** untuk mengurutkan array berdasarkan digit.

19. **`max_val = max(arr)`**
    - **Tujuan**: Menemukan nilai maksimum dalam array `arr` untuk menentukan digit paling signifikan (untuk batas iterasi).

20. **`exp = 1`**
    - **Tujuan**: Memulai dengan digit satuan (ekspansi = 1).

21. **`while max_val // exp > 0:`**
    - **Tujuan**: Looping melalui setiap digit dalam nilai elemen array dari digit satuan hingga digit tertinggi.

22. **`counting_sort_for_radix(arr, exp)`**
    - **Tujuan**: Memanggil fungsi **Counting Sort** untuk setiap digit (satuan, puluhan, ratusan, dst.).

23. **`exp *= 10`**
    - **Tujuan**: Mengubah `exp` dari 1 (digit satuan) menjadi 10 (digit puluhan), kemudian 100 (digit ratusan), dan seterusnya.

24. **`return arr`**
    - **Tujuan**: Mengembalikan array yang sudah diurutkan.

#### Bagian Utama Fungsi Radix Sort

25. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

26. **`print(radix_sort(arr))`**
    - **Output**: Array setelah diurutkan menggunakan **Radix Sort**:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Proses Utama dalam Radix Sort

1. **Inisialisasi Ekspansi (Digit Position)**:
   - Pada awalnya, algoritma bekerja pada digit satuan dengan `exp = 1`. Kemudian, `exp` akan meningkat menjadi 10, 100, dst., untuk menangani digit puluhan, ratusan, dsb.

2. **Counting Sort untuk Setiap Digit**:
   - Algoritma menggunakan **Counting Sort** untuk mengurutkan elemen berdasarkan setiap digit, dimulai dari digit paling kanan (satuan) hingga digit paling kiri (tertinggi).

3. **Iterasi Melalui Digit**:
   - Setelah setiap iterasi **Counting Sort**, `exp` akan dikalikan dengan 10 untuk berpindah ke digit berikutnya.

4. **Pengembalian Array Terurut**:
   - Setelah semua digit diproses, array akan terurut sepenuhnya.

### Contoh Langkah-Langkah Radix Sort

#### Langkah 1: Ekspansi Satuan (`exp = 1`)
- Array input: `[64, 34, 25, 12, 22, 11, 90, 1]`
- Setelah **Counting Sort** berdasarkan digit satuan: `[90, 1, 11, 12, 22, 34, 64, 25]`

#### Langkah 2: Ekspansi Puluhan (`exp = 10`)
- Setelah **Counting Sort** berdasarkan digit puluhan: `[1, 11, 12, 22, 25, 34, 64, 90]`

#### Hasil Akhir
- Array terurut: `[1, 11, 12, 22, 25, 34, 64, 90]`

### Kompleksitas Waktu Radix Sort
- **Time complexity**: O(d * (n + k)), di mana `d` adalah jumlah digit dalam nilai maksimum, `n` adalah jumlah elemen dalam array, dan `k` adalah jumlah nilai berbeda yang dapat diambil oleh digit (misalnya, 0-9 untuk angka desimal).
- **Space complexity**: O(n + k), karena memerlukan array tambahan `count` dan `output`.

### Kesimpulan
**Radix Sort** adalah algoritma sorting yang efisien untuk data numerik, terutama jika nilai-nilai dalam array memiliki digit yang panjang (misalnya, angka besar). Algoritma ini bekerja dengan cara mengurutkan elemen-elemen berdasarkan digit demi digit, dari digit terkecil hingga digit terbesar.

---

# 8. Bubble Sort

Bubble Sort bekerja dengan cara membandingkan elemen berdekatan dan menukarnya jika berada dalam urutan yang salah. Proses ini terus diulang sampai tidak ada lagi penukaran yang diperlukan, yang berarti daftar sudah terurut.

```python
def bubble_sort(arr):  # (1)
    n = len(arr)  # (2)
    for i in range(n):  # (3)
        swapped = False  # (4)
        for j in range(0, n - i - 1):  # (5)
            if arr[j] > arr[j + 1]:  # (6)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # (7)
                swapped = True  # (8)
        if not swapped:  # (9)
            break  # (10)
    return arr  # (11)

arr = [64, 34, 25, 12, 22, 11, 90, 1]  # (12)
print(bubble_sort(arr))  # (13)
```

### Penjelasan Setiap Baris

1. **`def bubble_sort(arr):`**
   - **Tujuan**: Mendefinisikan fungsi **Bubble Sort** yang menerima array `arr` sebagai parameter.

2. **`n = len(arr)`**
   - **Tujuan**: Menyimpan panjang array `arr` dalam variabel `n` untuk digunakan dalam looping.

3. **`for i in range(n):`**
   - **Tujuan**: Iterasi pertama untuk membatasi jumlah iterasi **Bubble Sort**, dimulai dari elemen pertama hingga elemen terakhir.

4. **`swapped = False`**
   - **Tujuan**: Inisialisasi variabel `swapped` sebagai indikator apakah ada elemen yang ditukar selama iterasi. Ini digunakan untuk mengoptimalkan algoritma dengan menghentikan iterasi jika array sudah terurut.

5. **`for j in range(0, n - i - 1):`**
   - **Tujuan**: Iterasi dalam array untuk membandingkan elemen-elemen yang bersebelahan. `n - i - 1` mengurangi jumlah elemen yang perlu diperiksa pada setiap iterasi, karena elemen terbesar sudah berada di posisi yang benar setelah setiap iterasi.

6. **`if arr[j] > arr[j + 1]:`**
   - **Tujuan**: Memeriksa apakah elemen saat ini (`arr[j]`) lebih besar dari elemen berikutnya (`arr[j + 1]`). Jika ya, mereka akan ditukar.

7. **`arr[j], arr[j + 1] = arr[j + 1], arr[j]`**
   - **Tujuan**: Menukar elemen-elemen jika mereka tidak dalam urutan yang benar (yaitu jika `arr[j] > arr[j + 1]`).

8. **`swapped = True`**
   - **Tujuan**: Mengatur `swapped` menjadi `True` karena elemen-elemen telah ditukar, yang berarti array belum terurut sepenuhnya dan iterasi berikutnya perlu dilakukan.

9. **`if not swapped:`**
   - **Tujuan**: Memeriksa apakah tidak ada elemen yang ditukar selama iterasi. Jika `swapped` masih `False`, berarti array sudah terurut dan tidak perlu iterasi lebih lanjut.

10. **`break`**
    - **Tujuan**: Menghentikan loop utama karena array sudah terurut. Ini adalah pengoptimalan untuk menghentikan proses lebih awal.

11. **`return arr`**
    - **Tujuan**: Mengembalikan array yang sudah diurutkan setelah semua iterasi selesai.

12. **`arr = [64, 34, 25, 12, 22, 11, 90, 1]`**
    - **Tujuan**: Array input yang akan diurutkan.

13. **`print(bubble_sort(arr))`**
    - **Output**: Array yang sudah diurutkan setelah menjalankan **Bubble Sort**:
    ```
    [1, 11, 12, 22, 25, 34, 64, 90]
    ```

### Bagaimana Bubble Sort Bekerja

1. **Iterasi Berulang Kali**:
   - Algoritma **Bubble Sort** bekerja dengan cara membandingkan dua elemen yang bersebelahan di dalam array, lalu menukar mereka jika urutannya salah (yaitu elemen kiri lebih besar dari elemen kanan).

2. **Setelah Setiap Iterasi**:
   - Setelah satu iterasi penuh (satu loop luar), elemen terbesar di dalam subarray yang belum diurutkan akan ditempatkan di posisi terakhirnya. Oleh karena itu, jumlah elemen yang perlu diperiksa berkurang satu pada setiap iterasi berikutnya.

3. **Optimalisasi dengan Swapped**:
   - Jika tidak ada elemen yang ditukar selama iterasi penuh (loop dalam), algoritma dapat berhenti lebih awal karena array sudah terurut. Ini dilakukan dengan memeriksa variabel `swapped`.

4. **Worst-Case dan Best-Case**:
   - **Worst-case time complexity**: O(n²), terjadi ketika array diurutkan secara terbalik.
   - **Best-case time complexity**: O(n), terjadi ketika array sudah terurut sejak awal. Algoritma hanya membutuhkan satu iterasi untuk memastikan array sudah terurut.
   - **Average time complexity**: O(n²), karena masih melibatkan dua loop bersarang.

### Contoh Langkah-Langkah Bubble Sort

Misalkan array input adalah:
```
[64, 34, 25, 12, 22, 11, 90, 1]
```

#### Iterasi 1:
- Membandingkan elemen pertama dan kedua: **64 > 34**, maka ditukar:
  ```
  [34, 64, 25, 12, 22, 11, 90, 1]
  ```
- Membandingkan elemen kedua dan ketiga: **64 > 25**, maka ditukar:
  ```
  [34, 25, 64, 12, 22, 11, 90, 1]
  ```
- Dan seterusnya, hingga elemen terbesar (90) berada di posisi terakhir:
  ```
  [34, 25, 12, 22, 11, 64, 1, 90]
  ```

#### Iterasi 2:
- Proses yang sama diulangi, mengurutkan elemen terbesar berikutnya ke posisi kedua terakhir:
  ```
  [25, 12, 22, 11, 34, 1, 64, 90]
  ```

#### Iterasi 3:
- Dan seterusnya, hingga array menjadi terurut sepenuhnya:
  ```
  [1, 11, 12, 22, 25, 34, 64, 90]
  ```

### Kesimpulan
**Bubble Sort** adalah algoritma yang sederhana namun tidak terlalu efisien untuk data besar karena kompleksitas waktu yang buruk (O(n²)). Namun, algoritma ini mudah dipahami dan dapat dioptimalkan untuk berhenti lebih awal jika array sudah terurut.

---

# **Algoritma yang Paling Cepat:**
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

# **Algoritma yang Paling Lambat:**
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

# **Sorting Algoritma yang Paling Populer di Kalangan Profesional:**
- **Quick Sort** adalah yang paling populer, terutama karena kecepatan rata-ratanya \(O(n \log n)\) dan penggunaan memori yang efisien.
  - Sering dipakai di aplikasi sehari-hari dan biasanya jadi *default sorting algorithm* di banyak bahasa pemrograman kayak C++ (`std::sort`).

- **Merge Sort** sangat populer dalam kasus di mana stabilitas sorting penting (misalnya, elemen-elemen yang sama tetap dalam urutan yang sama seperti sebelum disortir).
  - Contoh di Python, `sorted()` dan `list.sort()` menggunakan **Timsort**, yang merupakan gabungan dari Merge Sort dan Insertion Sort.

- **Counting Sort**, **Radix Sort**, dan **Bucket Sort** dipakai saat kita tahu rentang nilai data yang terbatas (misalnya, kalau kita mengurutkan nilai integer dalam rentang kecil). 
  - Ini sering dipakai dalam aplikasi yang memerlukan sorting dalam waktu konstan seperti di pemrosesan citra atau masalah khusus.

# **Kesimpulan**
- **Cepat dan Efisien (Populer)**: **Quick Sort** dan **Merge Sort**.
- **Cepat untuk Kasus Khusus**: **Counting Sort**, **Radix Sort**, **Bucket Sort** (untuk data integer dengan rentang terbatas).
- **Lambat**: **Bubble Sort**, **Selection Sort**, **Insertion Sort** (tapi bisa efisien untuk dataset kecil).