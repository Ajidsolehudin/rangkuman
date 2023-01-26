while(True):
    print("\n")
    print("=======================================")
    print("KALKULATOR NILAI AKHIR MAHASISWA STT YBSI")
    print("=======================================")

    nama = input("Masukkan nama Mahasiswa : ")
    nim = int(input("Masukkan NIM Mahasiswa : "))
    matkul = input("Masukkan nama Mata kuliah : ")
    nilai_absen = int(input("Masukkan nilai absen : "))
    nilai_tugas = int(input("Masukkan nilai tugas : "))
    nilai_uts = int(input("Masukkan nilai uts : "))
    nilai_uas = int(input("Masukkan nilai uas : "))
    print("\n")

    R_absen = nilai_absen * 20 / 100
    R_tugas = nilai_tugas * 25 / 100
    R_uts = nilai_uts * 25 / 100
    R_uas = nilai_uas * 30 / 100

    nilai_akhir = R_absen + R_tugas + R_uts + R_uas

    print("++++++++++++HASIL++++++++++++++")

    if nilai_akhir >= 80 :
        print("Nama Mahasiswa : ",nama)
        print("NIM : ",nim)
        print("Mata Kuliah : ",matkul)
        print("Nilai Akhir  : ",nilai_akhir)
        print ("Grade : A")
    elif nilai_akhir >= 75 :
        print("Nama Mahasiswa : ",nama)
        print("NIM : ",nim)
        print("Mata Kuliah : ",matkul)
        print("Nilai Akhir  : ",nilai_akhir)
        print ("Grade : B")
    elif nilai_akhir >= 60 :
        print("Nama Mahasiswa : ",nama)
        print("NIM : ",nim)
        print("Mata Kuliah : ",matkul)
        print("Nilai Akhir  : ",nilai_akhir)
        print ("Grade : C")
    elif nilai_akhir >= 40 :
        print("Nama Mahasiswa : ",nama)
        print("NIM : ",nim)
        print("Mata Kuliah : ",matkul)
        print("Nilai Akhir  : ",nilai_akhir)
        print ("Grade : D")
    elif nilai_akhir >= 0 :
        print("Nama Mahasiswa : ",nama)
        print("NIM : ",nim)
        print("Mata Kuliah : ",matkul)
        print("Nilai Akhir  : ",nilai_akhir)
        print ("Grade : E")
    else :
        print ("Nilai tidak valid")

    if nilai_akhir >= 60 :
        print("Kamu lulus")
    else :
        print("Kamu tidak lulus")

    print("++++++++++++HASIL++++++++++++++")


