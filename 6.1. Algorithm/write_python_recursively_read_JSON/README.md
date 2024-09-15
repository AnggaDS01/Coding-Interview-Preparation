# Recursive JSON Reader

```python
import json  # (1)

def read_json_recursively(data):  # (2)
    results = []  # (3)
    if isinstance(data, dict):  # (4)
        for key, value in data.items():  # (5)
            result = f"Key: {key}, Value: {value}"  # (6)
            results.append(result)  # (7)
            results.extend(read_json_recursively(value))  # (8)
            print(result)  # (9)
    elif isinstance(data, list):  # (10)
        for value in data:  # (11)
            read_json_recursively(value)  # (12)
            results.extend(read_json_recursively(value))  # (13)
    else:  # (14)
        result = f"Value: {data}"  # (15)
        results.append(result)  # (16)
        print(result)  # (17)

    return results  # (18)

with open('./data/file.json', 'r') as file:  # (19)
    file_json = json.load(file)  # (20)

results = read_json_recursively(file_json)  # (21)

print(results)  # (22)
```

### Penjelasan Setiap Baris

1. **`import json`**
   - **Tujuan**: Mengimpor modul `json` untuk menangani parsing file JSON. JSON digunakan untuk membaca, menulis, dan memproses data dalam format JSON.

2. **`def read_json_recursively(data):`**
   - **Tujuan**: Mendefinisikan fungsi `read_json_recursively` yang menerima satu parameter `data`. Tujuannya adalah membaca elemen-elemen dalam data JSON secara rekursif, baik itu dictionary (`dict`) maupun list (`list`).

3. **`results = []`**
   - **Tujuan**: Inisialisasi list `results` untuk menyimpan hasil dari proses membaca elemen-elemen JSON. Setiap kunci dan nilai akan ditambahkan ke dalam list ini.

4. **`if isinstance(data, dict):`**
   - **Tujuan**: Mengecek apakah tipe data yang sedang diperiksa adalah dictionary (`dict`). Jika iya, program akan mengeksekusi blok kode untuk mengolah key-value pair dari dictionary tersebut.

5. **`for key, value in data.items():`**
   - **Tujuan**: Iterasi melalui setiap pasangan key-value dalam dictionary `data`. Looping ini memproses setiap key dan value secara rekursif.

6. **`result = f"Key: {key}, Value: {value}"`**
   - **Tujuan**: Format string untuk menampilkan key dan value dalam format `"Key: key, Value: value"`. Ini berguna untuk menampilkan dan menyimpan informasi key-value dari dictionary.

7. **`results.append(result)`**
   - **Tujuan**: Menambahkan hasil yang baru saja diformat (`result`) ke list `results`.

8. **`results.extend(read_json_recursively(value))`**
   - **Tujuan**: Melakukan pemanggilan rekursif terhadap nilai (`value`) saat ini. Jika nilai tersebut adalah dictionary atau list, maka fungsi ini akan kembali memprosesnya secara rekursif, dan hasilnya akan ditambahkan ke `results`.

9. **`print(result)`**
   - **Tujuan**: Mencetak hasil (`result`) ke layar agar pengguna dapat melihat key dan value dari elemen yang sedang diproses.

10. **`elif isinstance(data, list):`**
    - **Tujuan**: Jika tipe data bukan dictionary melainkan list, maka blok ini akan dieksekusi. List diperlakukan berbeda karena tidak ada key, hanya value yang perlu diproses.

11. **`for value in data:`**
    - **Tujuan**: Melakukan iterasi melalui setiap elemen di dalam list `data`. Setiap value akan diproses secara rekursif dengan memanggil fungsi yang sama.

12. **`read_json_recursively(value)`**
    - **Tujuan**: Memproses setiap elemen di dalam list secara rekursif. Jika elemen tersebut adalah dictionary atau list, maka proses akan berulang.

13. **`results.extend(read_json_recursively(value))`**
    - **Tujuan**: Menggabungkan hasil dari pemanggilan rekursif terhadap elemen dalam list `value` dengan `results`.

14. **`else:`**
    - **Tujuan**: Blok ini akan dijalankan jika tipe data bukan dictionary atau list (misalnya tipe data dasar seperti string, integer, dll.).

15. **`result = f"Value: {data}"`**
    - **Tujuan**: Format string untuk menampilkan nilai sederhana (non-dictionary dan non-list) dalam format `"Value: value"`.

16. **`results.append(result)`**
    - **Tujuan**: Menambahkan hasil ke list `results`, yang berisi nilai sederhana dari elemen data.

17. **`print(result)`**
    - **Tujuan**: Mencetak nilai dari elemen sederhana ke layar agar pengguna dapat melihat hasilnya.

18. **`return results`**
    - **Tujuan**: Mengembalikan list `results` yang berisi semua hasil yang telah diproses dari dictionary dan list secara rekursif.

19. **`with open('./data/file.json', 'r') as file:`**
    - **Tujuan**: Membuka file JSON (`file.json`) yang ada di direktori `./data/` dengan mode read (`'r'`).

20. **`file_json = json.load(file)`**
    - **Tujuan**: Membaca dan memparsing isi file JSON ke dalam variabel `file_json`. Ini mengonversi data JSON menjadi struktur Python (dictionary atau list).

21. **`results = read_json_recursively(file_json)`**
    - **Tujuan**: Memanggil fungsi `read_json_recursively` dengan input `file_json` (data yang sudah diproses dari file). Hasilnya disimpan ke dalam variabel `results`.

22. **`print(results)`**
    - **Tujuan**: Mencetak isi dari list `results` yang berisi semua informasi key-value yang telah diproses dari file JSON.

### Penjelasan Logika Algoritma

Algoritma ini memproses data JSON secara **rekursif**, yang berarti ia terus memanggil dirinya sendiri saat bertemu dengan struktur bersarang (nested). Kapan pun elemen dictionary atau list ditemukan, algoritma akan masuk lebih dalam hingga elemen paling dasar ditemukan (seperti string, integer, dsb.).

1. **Jika Data adalah Dictionary**:
   - Algoritma membaca setiap key-value dari dictionary, lalu memproses key dan value secara rekursif. Jika value adalah dictionary atau list, maka algoritma masuk lebih dalam ke value tersebut.

2. **Jika Data adalah List**:
   - Algoritma memproses setiap elemen dalam list secara rekursif. List bisa berisi dictionary, list lain, atau nilai sederhana.

3. **Jika Data adalah Nilai Sederhana**:
   - Jika elemen bukan dictionary atau list (misalnya string, integer, dll.), maka ia hanya mencetak nilai tersebut dan menyimpannya dalam `results`.

### Contoh File JSON

Misalkan `file.json` berisi:

```json
{
    "name": "John",
    "age": 30,
    "children": [
        {
            "name": "Anna",
            "age": 10
        },
        {
            "name": "Ben",
            "age": 5
        }
    ],
    "married": true
}
```

### Proses yang Dilakukan:

1. **Memproses Root Dictionary**:
   - `name: John`, `age: 30`, `children` (list), dan `married: true`.
   
2. **Memproses List `children`**:
   - Untuk setiap anak di dalam list `children`, algoritma memproses dictionary yang berisi `name` dan `age`.

3. **Memproses Nilai Sederhana**:
   - Pada level terdalam, elemen-elemen seperti `"John"`, `30`, `"Anna"`, `10`, `true`, dsb., akan diproses dan dicetak.

### Output untuk JSON di Atas

```
Key: name, Value: John
Value: John
Key: age, Value: 30
Value: 30
Key: children, Value: [{'name': 'Anna', 'age': 10}, {'name': 'Ben', 'age': 5}]
Key: name, Value: Anna
Value: Anna
Key: age, Value: 10
Value: 10
Key: name, Value: Ben
Value: Ben
Key: age, Value: 5
Value: 5
Key: married, Value: True
Value: True
```

### Kesimpulan

Fungsi `read_json_recursively` memungkinkan kamu untuk membaca file JSON bersarang (nested) secara rekursif dan memproses setiap key dan value. Algoritma ini cocok untuk situasi di mana struktur data JSON bisa sangat kompleks, seperti saat terdapat dictionary di dalam dictionary atau list di dalam list.