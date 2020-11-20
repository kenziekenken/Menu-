from os import system
from json import dump, load
from datetime import datetime
 
def print_menu():
    system("cls")
    print("""
    Toko Furniture Aming
    [1]. Lihat Semua Furniture
    [2]. Tambah Produk Baru
    [3]. Cari Produk
    [4]. Hapus Produk
    [5]. Update Produk
    [6]. Tentang Aplikasi
    [Q]. Keluar
        """)

def print_header(msg):
    system("cls")
    print(msg)
 
def not_empty(container):
    if len(container) != 0:
        return True
    else:
        return False
 
def verify_ans(char):
    if char.upper() == "Y":
        return True
    else:
        return False
 
def print_data(id_contact=None, harga=True, stok=True, all_data=False):
    if id_contact != None and all_data == False:
        print(f"ID : {id_contact}")
        print(f"NAMA : {contacts[id_contact]['nama']}")
        print(f"HARGA : {contacts[id_contact]['harga']}")
        print(f"STOK : {contacts[id_contact]['stok']}")
    elif stok == False and all_data == False:
        print(f"ID : {id_contact}")
        print(f"NAMA : {contacts[id_contact]['nama']}")
        print(f"HARGA : {contacts[id_contact]['harga']}")
    elif all_data == True:
        for id_contact in contacts: # lists, string, dict
            nama = contacts[id_contact]["nama"]
            harga = contacts[id_contact]["harga"]
            stok = contacts[id_contact]["stok"]
            print(f"ID : {id_contact} - NAMA : {nama} - HARGA : {harga} - STOK : {stok}")
 
def view_contacts():
    print_header("DAFTAR FURNITURE")
    if not_empty(contacts):
        print_data(all_data=True)
    else:
        print("MAAF TIDAK ADA STOK TERSIMPAN")
    input("Tekan ENTER untuk kembali ke MENU")
 
def create_id_contact(name, price):
    hari_ini = datetime.now()
    tahun = hari_ini.year
    bulan = hari_ini.month
    hari = hari_ini.day
 
    counter = len(contacts) + 1
    first = name[0].upper()
    last_4 = price[-4:]
    
    id_contact = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
    return id_contact
 
 
 
def add_contact():
    print_header("MENAMBAHKAN PRODUK BARU")
    nama = input("NAMA \t: ")
    harga = input("HARGA \t: ")
    stok = input("STOK \t: ")
    respon = input(f"Apakah yakin ingin menambahkan produk : {nama} ? (Y/N) ")
    if verify_ans(respon):
        id_contact = create_id_contact(name=nama, price=harga)
        contacts[id_contact] = {
            "nama" : nama,
            "harga" : harga,
            "stok" : stok
        }
        saved = save_data_contacts()
        if saved:
            print("Data Produk Tersimpan.")
        else:
            print("Kesalahan saat menyimpan")
    else:
        print("Data Batal Disimpan")
    input("Tekan ENTER untuk kembali ke MENU")
 
def searching_by_name(contact):
    for id_contact in contacts:
        if contacts[id_contact]['nama'] == contact:
            return id_contact
    else:
        return False
 
def find_contact():
    print_header("MENCARI PRODUK")
    nama = input("Nama Produk yang Dicari : ")
    exists = searching_by_name(nama)
    if exists:
        print("Produk Ditemukan")
        print_data(id_contact=exists)
    else:
        print("Produk Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
def delete_contact():
    print_header("MENGHAPUS PRODUK")
    nama = input("Nama Produk yang akan Dihapus : ")
    exists = searching_by_name(nama)
    if exists:
        print_data(id_contact=exists)
        respon = input(f"Yakin ingin menghapus {nama} ? (Y/N) ")
        if verify_ans(respon):
            del contacts[exists]
            saved = save_data_contacts()
            if saved:
                print("Data Produk Telah Dihapus")
            else:
                print("Kesalahan saat menyimpan")
        else:
            print("Data Produk Batal Dihapus")
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
def update_contact_nama(id_contact):
    print(f"Nama Produk Lama : {contacts[id_contact]['nama']}")
    new_name = input("Masukkan Produk baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        contacts[id_contact]['nama'] = new_name
        print("Data Telah di simpan")
        print_data(id_contact)
    else:
        print("Data Batal diubah")
 
def update_contact_telp(id_contact):
    print(f"Harga Produk Lama : {contacts[id_contact]['harga']}")
    new_telp = input("Masukkan Harga Produk Baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        contacts[id_contact]['harga'] = new_harga
        print("Data Telah di simpan")
        print_data(id_contact)
    else:
        print("Data Batal diubah")
 
def update_contact_hobi(contact):
    print(f"Stok Produk Lama : {contacts[id_contact]['stok']}")
    new_telp = input("Masukan Stok Produk Baru : ")
    respon = input("Apakah yakin data ingin diubah (Y/N) : ")
    result = verify_ans(respon)
    if result :
        contacts[id_contact]['stok'] = new_stok
        print("Data Telah di simpan")
        print_data(id_contact)
    else:
        print("Data Batal diubah")
 
 
def update_contact():
    print_header("MENGUPDATE INFO PRODUK")
    nama = input("Nama Produk yang akan di-update : ")
    exists = searching_by_name(nama)
    if exists:
        print_data(exists)
        print("EDIT FIELD [1] NAMA - [2] HARGA - [3] STOK")
        respon = input("MASUKAN PILIHAN (1/2/3) : ")
        if respon == "1":
            update_contact_nama(exists)
        elif respon == "2":
            update_contact_telp(exists)
        elif respon == "3":
            update_contact_hobi(exists)
        saved = save_data_contacts()
        if saved:
            print("Data Produk Telah di-update.")
        else:
            print("Kesalahan saat menyimpan")
 
    else:
        print("Data Tidak Ada")
    input("Tekan ENTER untuk kembali ke MENU")
 
 
def check_user_input(char):
    char = char.upper()
    if char == "Q":
        print("BYE!!!")
        return True
    elif char == "1":
        view_contacts()
    elif char == "2":
        add_contact()
    elif char == "3":
        find_contact()
    elif char == "4":
        delete_contact()
    elif char == "5":
        update_contact()
    elif char == "6":
        pass
 
def load_data_contacts():
    with open(file_path, 'r') as file:
        data = load(file)
    return data
 
def save_data_contacts():
    with open(file_path, 'w') as file:
        dump(contacts, file)
    return True
 
 
#flag/sign/tanda menyimpan sebuah kondisi
stop = False
file_path = "furniture.json"
contacts = load_data_contacts()
while not stop:
    print_menu()
    user_input = input("Pilihan : ")
    stop = check_user_input(user_input)