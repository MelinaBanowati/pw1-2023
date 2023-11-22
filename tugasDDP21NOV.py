def profil(nama, alamat, gender, umur, hobby) :
   print ('Nama saya adalah', nama)
   print ('Alamat saya di', alamat)
   print ('Gender saya adalah', gender)
   print ('Umur saya', umur)
   print ('hobby saya', hobby)

#memanggil fungsi 
profil ('Melina Putri Banowati', 'Citeureup', 'perempuan', '19 tahun','menggambar')


def melihat_nilai(nilai) :
   if nilai <60 and nilai >=0:
       print('gagal')
   elif nilai <61 and nilai>=0 :
       print("baik") 
   elif nilai <71 and nilai>=0 :
       print("sangat baik") 
   elif nilai >=81 and nilai >=100:
       print('istimewa')
#memanggil fungsi
melihat_nilai(100)

def ganjil(bilangan) :
    for i in range (1,bilangan+1,2):
        print(i)

#memanggil fungsi
ganjil (9)