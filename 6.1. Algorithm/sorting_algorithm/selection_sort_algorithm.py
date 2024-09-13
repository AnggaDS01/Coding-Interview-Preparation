'''
Selection Sort memilih elemen terkecil dari array dan menukarnya dengan elemen pada posisi pertama, lalu mengulangi untuk posisi berikutnya.
'''

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

### Penjelasan Setiap Baris

'''
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