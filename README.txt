TUGAS KECIL 2 IF2211 STRATEGI ALGORITMA
SEMESTER II 2020/2021

NAMA : EPATA TUAH
NIM  : 13519120
KELAS: K-03

# DESKRIPSI #
Algoritma topological sort merupakan salah satu penerapan dari pendekatan
Decrease and Conquer, yakni algoritma pengurutan node pada graf non-sirkuler 
terarah atau dapat disebut Directed Acyclic Graph (DAG) dengan pemisalan node A
menuju node B, node A muncul terlebih dahulu sebelum node B pada pengurutan.
Pada program ini, algoritma topological sort digunakan dalam pembuatan rencana
pengambilan mata kuliah. Pertama, dilakukan pengecekan derajat masuk pada simpul DAG. 
Apabila derajat masuk suatu simpul adalah nol, pilih simpul tersebut. Simpul tersebut
akan dimasukkan ke rencana kuliah. Setelah dimasukkan, simpul tersebut dihapus
dan semua busur yang keluar dari simpul tersebut juga dihapus. Langkah diulangi
hingga semua simpul mata kuliah dipilih. Setelah semua simpul terpilih, tampilkan
rencana mata kuliah yang telah disusun.

# REQUIREMENT #
- Python versi 3.9

# CARA MENGGUNAKAN PROGRAM #
- Dengan program IDLE Python
1. Buka program IDLE (program dapat dicari menggunakan fitur search pada windows)
2. Pilih menu "File"
3. Pilih "Open"
4. Cari direktori src
5. Open "13519120-main.py"
6. Pilih menu "Run"
7. Pilih "Run Module"
8. Pada awal program, input terlebih dahulu nama file test yang akan diuji
   (file harus berekstensi .txt dan harus berada di folder ../test)
9. Tunggu hingga program menyelesaikan pemrosesan algoritmanya

- Dengan Command Prompt
1. Buka Command Prompt
2. Cari direktori src
3. Ketik perintah "python 13519120-main.py"
4. Pada awal program, input terlebih dahulu nama file test yang akan diuji
   (file harus berekstensi .txt dan harus berada di folder ../test)
5. Tunggu hingga program menyelesaikan pemrosesan algoritmanya




