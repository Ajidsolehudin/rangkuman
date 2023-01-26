print("1. Hitung luas persegi")
print("2. Hitung luas lingkaran")

a = int(input("pilih opsi : "))

if a == 1 :
    def hitungLuasPersegi(sisi_persegi):
      return round(sisi_persegi * sisi_persegi,2)

    sisi_persegi = float(input('Input panjang sisi persegi: '))
    print('Luas persegi = ',hitungLuasPersegi(sisi_persegi))

elif a == 2 :
    def hitungLuasLingkaran(alas, tinggi):
        return round(0.5 * alas * tinggi)

    alas = float(input('Input alas : '))
    tinggi = float(input('Input tinggi : '))
    print('Luas lingkaran = ',hitungLuasLingkaran(alas, tinggi))

else :
    print("tidak valid")
