# **Cashier Project**

### **Backgorund Project**

Seseorang ingin membuat sistem kasir dengan self-service oriented pada supermarket miliknya, 
sehingga pelanggan di supermarket tersebut bisa langsung menginput item beserta jumlah dan harganya tanpa bantuan orang lain.  Sistem kasir ini diharapkan dapat menampilkan hasil dari total barang yang dibeli beserta diskon dengan ketentuan yang berlaku. 
Sistem ini juga memungkin orang yang tidak berada di supermarket tersebut juga dapat memesan barang tersebut.

### **Requirements / Objective dan Alur Program**

1. Membuat program untuk menampung list pada barang yang akan dibeli.
	- Langkah pertama kita membutuhkan input pada method add_item() berupa nama, qty dan harga.
	- Input masuk ke proses method add_item() dengan output berupa list.
	- Jika terjadi ketidaksesuaian input yang diharapkan, sistem akan mengalami error.

2. Membuat program untuk mengubah nama item, jumlah dan harga item jika terjadi kesalahan input.
	- Langkah pertama kita membutuhkan input parameter pada method update_item_name() berupa item_name, nama baru. Pada method update_item_qty() berupa item_name dan qty_baru. Pada method update_item_price berupa item_name dan price_baru.
	- Input masuk ke proses method dengan output berupa list item yang sudah terganti
	- Jika terjadi ketidaksesuaian input yang diharapkan, sistem akan mengalami error.

3. Membuat program untuk menghapus sebagian atau seluruh item pada database yang telah diinput sebelumnya.
	- Langkah pertama kita membutuhkan input parameter pada method delete_item() berupa nama_item.
	- Input masuk ke proses method dengan output list barang yang tersisa.
	- Jika terjadi ketidaksesuaian input yang diharapkan, sistem akan mengalami error.
	
4. Membuat program untuk menampilkan apa saja yang telah terinput untuk memastikan apakah terjadi kesalahan atau tidak.
	- Langkah pertama kita tidak membutuhkan input parameter pada method reset_transaction() seperti pada method sebelumnya.
	- Input masuk ke proses method dan list barang akan tereset (berupa list kosong).
	- Jika terjadi ketidaksesuaian input yang diharapkan, sistem akan mengalami error.
	
5. Membuat program untuk menghitung seluruh harga setelah diskon dengan beberapa ketentuan.
	- Langkah pertama kita tidak membutuhkan input parameter seperti pada method sebelumnya di method total_price() dengan asumsi database tidak kosong atau direset menggunakan method reset_transaction().
	- Input masuk ke proses method dan akan menampilkan list barang yang akan dibayar beserta harga setelah diskon.
	- Jika terjadi ketidaksesuaian input yang diharapkan, sistem akan mengalami error.

## **Penjelasan Code**

1. Fungsi 1

	
	
	
	
	
	
	
	
