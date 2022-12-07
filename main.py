
# Import Library
from tabulate import tabulate

#Class
class Transaksi:

    #FUNGSI 1: Menginisialisasi data dalam bentuk list
    def __init__(self):
        
        self.emptyList = list()

    # FUNGSI 2: Menambahkan list barang yang akan dibeli ke "database"
    def add_item(self, nama, qty, harga):
        """Fungsi ini untuk menambahkan item yang ingin dibeli
        
        Parameter:
        nama: (str) Nama item yang akan ditambahkan
        qty: (int) Jumlah item yang akan ditambahkan
        harga: (int) Harga item yang akan ditambahkan

        """
        
        try:
            list_barang = [nama, qty, harga]
            self.emptyList.append(list_barang)
            return f"Item yang dibeli adalah: {self.emptyList}"
        
        except:
            raise TypeError("Mohon diisi sesuai ketentuan")

    
    # FUNGSI 3: Memperbaharui nama item jika terjadi kesalahan nama
    def update_item_name(self, nama_item, nama_baru):
        """Fungsi ini untuk mengganti nama item dengan yang baru
        Parameter:
        nama_item: (str) Nama item yang akan diganti
        nama_baru: (str) Nama baru item 
        """

        for i in self.emptyList:
                if i[0] == nama_item:
                    i[0] = nama_baru
                
        print(self.emptyList)


    # FUNGSI 4: Memperbaharui kuantiti item jika terjadi kesalahan
    def update_item_qty(self, nama_item, qty_baru):
        """Fungsi ini untuk mengganti jumlah item dengan yang baru
        Parameter:
        nama_item: (str) Nama item yang akan diganti jumlahnya
        qty_baru: (int) Nama baru item 
        """
        
        for i in self.emptyList:
            if i[0] == nama_item:
                i[1] = qty_baru
            
        print(self.emptyList)
    

    # FUNGSI 5: Memperbaharui harga item jika terjadi kesalahan
    def update_item_price(self, nama_item, price_baru):
        """Fungsi ini untuk mengganti jumlah harga dengan yang baru
        Parameter:
        nama_item: (str) Nama item yang akan diganti harganya
        price_baru: (int) Harga baru item
        """

        for i in self.emptyList:
            if i[0] == nama_item:
                i[2] = price_baru
            
        print(self.emptyList)

    # FUNGSI 6: Menghapus item jika terjadi kesalahan input
    def delete_item(self, nama_item):
        """Fungsi ini akan menghapus satu item beserta atributnya"""

        for i in self.emptyList:
            if nama_item in i:
                self.emptyList.remove(i)
            
        print(self.emptyList)


    # FUNGSI 7: Menghapus seluruh "database" item
    def reset_transaction(self):
        """Fungsi ini akan menghapus seluruh list item yang akan dibeli"""
        
        self.emptyList.clear()
        print("Semua item berhasil dihapus")
        

    # FUNGSI 8: Menampilkan informasi barang yang terdaftar dalam bentuk list
    def recent_order(self):
        """Fungsi ini akan menampil info barang apa saja yang telah terdaftar"""
        
        print(self.emptyList)


    # FUNGSI 9: Menampilkan informasi barang dan harga final setelah diskon
    def total_price(self):
        """Fungsi ini untuk menampilkan total harga dari seluruh pembelian setelah diskon"""

        total_price = 0
        print(f"Item yang dibeli adalah: {self.emptyList}")
        for i in range(len(self.emptyList)):
            total_price = total_price + (self.emptyList[i][-1] * self.emptyList[i][-2])
        if total_price > 500000:
            total_price = total_price - (total_price * 0.1)
            print(f"Total belanja yang harus dibayarkan adalah {total_price}")
        elif total_price > 300000:
            total_price = total_price - (total_price * 0.08)
            print(f"Total belanja yang harus dibayarkan adalah {total_price}")
        elif total_price > 200000:
            total_price = total_price - (total_price * 0.05)
            print(f"Total belanja yang harus dibayarkan adalah {total_price}")
        else:
            print(f"Total belanja yang harus dibayarkan adalah {total_price} ")
        
    
    # FUNGSI 10: Menampilkan seluruh orderan dalam bentuk tabel dengan kolom total harga
    def check_order(self):
        """Fungsi ini untuk menampilkan info barang dalam format tabel"""

        try:
            list_baru = []
            for i in self.emptyList:
                list_baru.append(i)
            

            for a in list_baru:

                a.append(a[-1] * a[-2])
                

            headers = ["Nama Item", "Jumlah", "Harga", "Total"]

            print("Check Order")
            print("")
            print(tabulate(list_baru, headers, tablefmt="github"))
            print("")
            print("Pemesanan sudah benar")
        
        except:
            raise Exception("Terdapat kesalahan input data")

trnsct_123 = Transaksi()

# Test Case 1
print("Test Case 1")

print(trnsct_123.add_item("Ayam Goreng", 2, 20000))
print(trnsct_123.add_item("Pasta Gigi", 3, 15000))
print(" ")
# Test Case 2
print("Test Case 2")

trnsct_123.delete_item("Pasta Gigi")
print(" ")
# Test Case 3
print("Test Case 3")

trnsct_123.reset_transaction()
print(" ")
# Test Case 4
print("Test Case 4")

trnsct_123.add_item("Ayam Goreng", 2, 20000)
trnsct_123.add_item("Pasta Gigi", 3, 15000)
trnsct_123.add_item("Mainan Mobil", 1, 200000)
trnsct_123.add_item("Mie Instan", 5, 3000)

trnsct_123.total_price()

trnsct_123.check_order()