# soal 1
kendaraan=["B 3037 EMZ","Mobil",300,"Hitam"]
print(kendaraan)

#soal 2
kendaraan.append("50jt")
kendaraan.append("4")
kendaraan.insert(4,"Honda")
kendaraan.insert(1,"Matic")
print(kendaraan)

#soal 3
luas = input("hitung luas bangun berikut!")
match luas:
    case "persegi":
        sisi=int(input("masukan nilai sisi:"))
        luas=sisi*sisi
        print(luas)
    
    case "lingkaran":
        jarijari=int(input("masukan nilai jarijari:"))
        luas=3.14*jarijari*jarijari
        print(luas)

    case "segitiga":
        alas=int(input("masukan nilai alas:"))
        tinggi=int(input("masukan nilai tinggi:"))
        luas=alas*tinggi*1/2
        print(luas)
    
