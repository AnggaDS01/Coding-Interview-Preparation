'''
Merge Sort membagi array menjadi sub-array kecil, kemudian menggabungkannya kembali dengan urutan yang benar.
'''

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

'''
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
- Merge Sort memiliki **kompleksitas waktu O(n log n)**, karena setiap kali array dibagi menjadi

 dua (log n), dan kita perlu menggabungkan array tersebut (O(n)).
'''