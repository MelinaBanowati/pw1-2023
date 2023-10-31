Mobil=["ferarri 458","Mobil Sport","ferarri" "4,499cc"]
print (Mobil)

Mobil.append("Merah")
Mobil.append("4")
Mobil.append("10.000.000.000")

print (Mobil)

kendaraan = ["mobil", "pribadi", "dua ribu cc", "biru", "roda dua"]
kendaraan.append("satu miliyar")
kendaraan.append("turbo")
kendaraan.insert(kendaraan.index("pribadi"),"civic")
print(kendaraan)
  
ket='''selamat datang di aplikasi perhitungan silahkan pilih menu yang akan anda jalankan
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menggitung luas segitiga'''

pilihan = input(ket)

match pilihan:
    case"1"
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = float(input("masukkan sisi"))
        luasP = sisi*sisi
        print("kuas persegi yang sisinya", sisi, "adalah", luasP)
    case"2"
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari = float(input("masukkan jari-jari:"))
        luas =3.14*jari*jari
        print("luas lingkaran yang jari jarinya", jari, "adalah", int(luas))
    case"3": print("kamu memilih 3 untuk menghitung luas segitiga") 
        alas int(input("masukan alas :))
        tinggi int(input("masukan tinggi: "))
        luasS = 0.5 alas tinggi
        print ("luas segitiga yang alasnya ", alas," dan tingginya ",tinggi," adalah", int(luasS))
        case _: 
print("anda salah memilih")
