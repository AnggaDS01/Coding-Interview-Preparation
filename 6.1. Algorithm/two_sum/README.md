# Two Sum

```python
def two_sum(nums, target):  # (1)
    seen = {}  # (2)
    for idx, value in enumerate(nums):  # (3)
        compl = target - value  # (4)
        if compl in seen:  # (5)
            return [seen[compl], idx]  # (6)
        seen[value] = idx  # (7)
    return []  # (8)

arr = [2, 7, 11, 15]  # (9)
target = 9  # (10)
print(two_sum(arr, target))  # (11)
```

### Penjelasan Setiap Baris

1. **`def two_sum(nums, target):`**
   - **Tujuan**: Mendefinisikan fungsi **Two Sum** yang menerima array `nums` (daftar angka) dan `target` (jumlah target) sebagai parameter. Tugasnya adalah menemukan dua angka dari `nums` yang jika dijumlahkan akan sama dengan `target`.

2. **`seen = {}`**
   - **Tujuan**: Inisialisasi dictionary `seen` yang akan menyimpan pasangan nilai dari array sebagai kunci (`value`) dan indeks sebagai nilainya (`idx`). Ini akan membantu untuk memeriksa apakah angka pelengkap (`compl`) sudah pernah muncul sebelumnya.

3. **`for idx, value in enumerate(nums):`**
   - **Tujuan**: Looping melalui array `nums` dengan `idx` sebagai indeks elemen dan `value` sebagai nilai elemen di setiap iterasi. `enumerate` digunakan agar kita bisa mendapatkan indeks dan nilai sekaligus.

4. **`compl = target - value`**
   - **Tujuan**: Menghitung nilai pelengkap (`compl`) dari `value` yang sedang diperiksa, yaitu angka yang jika ditambahkan ke `value` akan menghasilkan `target`. Dengan kata lain, `compl` adalah nilai yang sedang dicari di dictionary `seen`.

   - **Contoh**: Jika `value = 2` dan `target = 9`, maka `compl = 9 - 2 = 7`.

5. **`if compl in seen:`**
   - **Tujuan**: Memeriksa apakah nilai pelengkap (`compl`) sudah pernah ditemukan sebelumnya (apakah ada di dictionary `seen`). Jika sudah ada, berarti kita menemukan pasangan angka yang jika dijumlahkan akan menghasilkan `target`.

6. **`return [seen[compl], idx]`**
   - **Tujuan**: Jika `compl` ditemukan di `seen`, kembalikan hasil berupa pasangan indeks dari elemen yang ditemukan sebelumnya (`seen[compl]`) dan indeks elemen saat ini (`idx`). Ini adalah dua indeks yang sesuai dengan `target`.

   - **Contoh**: Misalkan `value = 7`, maka `compl = 2`. Jika `compl = 2` sudah ada di `seen` dengan indeks 0, maka output adalah `[0, 1]`.

7. **`seen[value] = idx`**
   - **Tujuan**: Jika nilai pelengkap (`compl`) tidak ditemukan, maka simpan nilai saat ini (`value`) beserta indeksnya (`idx`) di dictionary `seen`. Ini berarti kita sudah "melihat" nilai ini dan bisa digunakan jika nanti ada nilai pelengkap yang sesuai.

8. **`return []`**
   - **Tujuan**: Jika tidak ada pasangan yang menghasilkan `target`, kembalikan array kosong sebagai tanda bahwa tidak ditemukan solusi.

9. **`arr = [2, 7, 11, 15]`**
   - **Tujuan**: Array input (`arr`) yang akan digunakan untuk mencari pasangan angka yang jika dijumlahkan menghasilkan `target`.

10. **`target = 9`**
    - **Tujuan**: Jumlah target yang ingin dicari dari dua angka di dalam array `arr`.

11. **`print(two_sum(arr, target))`**
    - **Output**: Mencetak hasil dari fungsi `two_sum`. Output untuk contoh ini adalah:
    ```
    [0, 1]
    ```
    Karena angka `2` (di indeks 0) dan angka `7` (di indeks 1) jika dijumlahkan menghasilkan `9`.

### Penjelasan Logika Algoritma Two Sum

1. **Memeriksa Setiap Elemen**:
   - Algoritma berjalan melalui setiap elemen dalam array `nums`. Untuk setiap elemen `value` yang ada di array, kita mencari "pasangan" elemen lain yang jika ditambahkan ke `value` akan menghasilkan `target`. Pasangan ini disebut nilai pelengkap (`compl`), yang dihitung dengan `compl = target - value`.

2. **Mencari Pasangan dengan Dictionary**:
   - Alih-alih melakukan pencarian pasangan secara brute-force (yang akan membutuhkan O(n²) waktu), algoritma ini menggunakan dictionary `seen` untuk menyimpan elemen-elemen yang telah ditemukan, bersama dengan indeks mereka. Dengan cara ini, mencari nilai pelengkap hanya membutuhkan O(1) waktu untuk setiap pencarian di dictionary, membuat algoritma lebih efisien.

3. **Proses Menghitung dan Menyimpan**:
   - Setiap kali kita menemukan angka `value`, kita menghitung nilai pelengkapnya `compl`. Jika `compl` sudah ada di `seen`, berarti kita telah menemukan dua angka yang jika dijumlahkan menghasilkan `target`, sehingga kita dapat langsung mengembalikan indeks dari kedua angka tersebut.
   - Jika tidak ada `compl`, maka kita menyimpan `value` beserta indeksnya dalam `seen`, sehingga jika nanti ditemukan nilai pelengkap, kita bisa langsung menemukannya.

### Contoh Langkah-Langkah

Misalkan array input adalah:
```
arr = [2, 7, 11, 15]
target = 9
```

1. **Langkah 1 (Elemen pertama: 2)**:
   - **value = 2**, **compl = 9 - 2 = 7**.
   - Apakah `compl = 7` ada di `seen`? Belum ada.
   - Tambahkan `2` ke dalam `seen`: `{2: 0}` (indeks 0).

2. **Langkah 2 (Elemen kedua: 7)**:
   - **value = 7**, **compl = 9 - 7 = 2**.
   - Apakah `compl = 2` ada di `seen`? Ya, `2` ada di `seen` dengan indeks 0.
   - Maka kita kembalikan `[0, 1]`, karena `arr[0] + arr[1] = 9`.

### Kesimpulan

Algoritma **Two Sum** ini sangat efisien karena menggunakan dictionary untuk melacak elemen-elemen yang telah dilihat, memungkinkan pencarian pasangan elemen dalam O(n) waktu. Ini jauh lebih cepat dibandingkan metode brute-force yang membutuhkan O(n²). 

Output dari contoh ini adalah:
```
[0, 1]
```
Yang berarti elemen di indeks 0 (`2`) dan elemen di indeks 1 (`7`) jika dijumlahkan akan menghasilkan nilai `9`.