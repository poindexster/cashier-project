# **Cashier Project**


## **Background Project**

Seseorang ingin membuat sistem kasir dengan self-service oriented pada supermarket miliknya, 
sehingga pelanggan di supermarket tersebut bisa langsung menginput item beserta jumlah dan harganya tanpa bantuan orang lain.  Sistem kasir ini diharapkan dapat menampilkan hasil dari total barang yang dibeli beserta diskon dengan ketentuan yang berlaku. 
Sistem ini juga memungkin orang yang tidak berada di supermarket tersebut juga dapat memesan barang tersebut.



## **Requirements/Objective and Program Flow**

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




## **Code Explanation**

1. Fungsi 1
![f1](https://user-images.githubusercontent.com/103387586/206279781-46b6c1fd-d297-48fc-88a4-40a44ae28760.png)

2. Fungsi 2
![f2](https://user-images.githubusercontent.com/103387586/206279826-75481aea-7c3c-4550-91bc-afc097ae10ef.png)

3. Fungsi 3
![f3](https://user-images.githubusercontent.com/103387586/206279834-72a6ecb5-14ec-41b5-9286-1ade81abafa4.png)

4. Fungsi 4
![f4](https://user-images.githubusercontent.com/103387586/206279836-af27fb14-5c41-479e-b020-b1da0c51d1d6.png)

5. Fungsi 5
![f5](https://user-images.githubusercontent.com/103387586/206279842-7dc00fe2-3826-4f61-94a1-d641aa9e7ede.png)

6. Fungsi 6
![f6](https://user-images.githubusercontent.com/103387586/206279845-3fb9236a-a5d9-4520-85bc-f27f00eb0500.png)

7. Fungsi 7
![f7](https://user-images.githubusercontent.com/103387586/206279848-25f35e90-6565-4326-8e40-a9de036f4364.png)

8. Fungsi 8
![f8](https://user-images.githubusercontent.com/103387586/206279852-f611e211-ad82-47cd-8d12-b26f74344e76.png)

9. Fungsi 9
![f9](https://user-images.githubusercontent.com/103387586/206279857-e8535898-671b-4779-ae91-041e6f358247.png)

10. Fungsi 10
![f10](https://user-images.githubusercontent.com/103387586/206279858-2b5e3f3b-9f81-4e86-aa85-23c7bcd9342e.png)

## **Test Case**
1. Test Case 1
- Pada test case ini, customer ingin menambahkan list item dengan menggunakan method add_item() dengan output berupa list barang tersebut.
![t1](https://user-images.githubusercontent.com/103387586/206279864-cf2bfb5e-c8a5-4d2b-b403-3ce6f03cb2f1.png)

2. Test Case 2
- Pada test case ini, customer ingin menghapus salah satu item dengan menggunakan method delete_item() sehingga menyisakan barang yang ingin benar-benar dibeli.
![t2](https://user-images.githubusercontent.com/103387586/206279868-cce4524e-aedd-44e0-8223-f2f9cd59124d.png)

3. Test Case 3
- Pada test case ini, customer ingin menghapus seluruh barang yang telah dilist sebelumnya atau mereset daftar belanjaan sehingga menghasilkan output list kosong dan akan menunjukkan sebuah pesan yang menandakan list item telah direset.
![t3](https://user-images.githubusercontent.com/103387586/206279872-a5047b41-c9f8-4944-8a75-45cce42ebdfe.png)

4. Test Case 4
- Pada test case ini, customer ingin mengetahui apa saja barang yang telah dibeli beserta total dari seluruh harga setelah potongan yang berlaku dengan daftar belanjaan yang baru.
![t4](https://user-images.githubusercontent.com/103387586/206279876-41c6c895-4021-471b-bfda-787cf6e3c2bd.png)



## **Conclusion and Future Work**
Dengan membuat program sederhana tersebut, diharapkan customer dapat membuat order secara mandiri dari supermarket tersebut maupun dari tempat customer berada, namun masih terdapat beberapa fitur yang harus ditambah jika programmer ada waktu lebih, yaitu membuat defence programming mechanism yang lebih complex, menambah fitur voucher jika memungkinkan dan memiliki sistem input yang lebih interaktif.









	
	
	
	
	
	
	
	
