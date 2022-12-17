
# Memanggil 
from Volume import HitungLuas


next = True
while (next):

    print("MENGHITUNG LUAS VOLUME")
    print("1. Persegi")
    print("2. Segitiga")
    print("3. Lingkaran")
    print("0. Exit")

    try:
        menu = int(input("Pilih Menu : "))

        if (menu == 1):
            persegi = HitungLuas()
            p = input("Masukkan Panjang : ")
            l = input("Masukkan Lebar   : ")
            persegi.setPersegi(p, l)
            print(f"Luas Persegi : {persegi.getLuasPersegi()}")

        elif (menu == 2):
            segitiga = HitungLuas()
            a = input("Masukkan Alas   : ")
            t = input("Masukkan Tinggi : ")
            segitiga.setSegitiga(a, t)
            print(f"Luas Segitiga : {segitiga.getLuasSegitiga()} ")
        elif (menu == 3):
            lingkaran = HitungLuas()
            j = input("Masukkan jari-jari : ")
            lingkaran.setLingkaran(j)
            print(f"Luas Lingkaran : {lingkaran.getLuasLingkaran()} ")
        elif (menu == 0):
            print("Program Exit")
            break


        stop = HitungLuas.stop()
        if stop == True:
            next = False
    
    except:
        print("Don't input string, please input number!")