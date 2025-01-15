angka = ['satu', 'dua', 'tiga', 'empat', 'lima',
         'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh']

belas = " belas "
puluh = " puluh "
ratus = " ratus "
seratus = " seratus "
ribu = " ribu "
seribu = " seribu "
juta = " juta "
sejuta = " sejuta "


def terbilang(x):
    if 1 <= x <= 10:
        hasil = angka[x - 1]
    elif x == 11:
        hasil = " sebelas"
    elif 12 <= x <= 19:
        hasil = angka[x - 11] + belas
    elif 20 <= x <= 99:  # untuk puluhan
        puluhan = x // 10
        satuan = x % 10
        if satuan == 0:
            hasil = angka[puluhan - 1] + puluh
        else:
            hasil = angka[puluhan - 1] + puluh + angka[satuan - 1]
    elif 100 <= x <= 999:  # untuk ratusan
        ratusan = x // 100
        sisa = x % 100
        if ratusan == 1:  # Jika ratusan bernilai 1, gunakan kata "seratus"
            if sisa == 0:
                hasil = seratus
            else:
                hasil = seratus + terbilang(sisa)
        else:  # Untuk ratusan selain 1
            if sisa == 0:
                hasil = angka[ratusan - 1] + ratus
            else:
                hasil = angka[ratusan - 1] + ratus + terbilang(sisa)
    elif 1000 <= x <= 9999:  # Untuk ribuan
        ribuan = x // 1000
        sisa = x % 1000
        if ribuan == 1:  # Jika ribuan bernilai 1, gunakan kata "seribu"
            if sisa == 0:
                hasil = seribu
            else:
                hasil = seribu + terbilang(sisa)
        else:  # Untuk ribuan selain 1
            if sisa == 0:
                hasil = angka[ribuan - 1] + ribu
            else:
                hasil = angka[ribuan - 1] + ribu + terbilang(sisa)
    elif 10000 <= x <= 99999:  # Untuk puluhan ribu
        puluhanRibu = x // 1000
        sisa = x % 1000
        if puluhanRibu < 20:  # Untuk angka 10 ribu sampai 19 ribu
            if sisa == 0:
                hasil = terbilang(puluhanRibu) + ribu
            else:
                hasil = terbilang(puluhanRibu) + ribu + terbilang(sisa)
        else:  # Untuk angka 20 ribu ke atas
            ribuan = x // 1000
            if sisa == 0:
                hasil = terbilang(ribuan) + ribu
            else:
                hasil = terbilang(ribuan) + ribu + terbilang(sisa)

    elif 100000 <= x <= 999999:  # Untuk ratusan ribu
        ratusanRibu = x // 1000
        sisa = x % 1000
        if ratusanRibu == 1:  # Untuk angka 100 ribu sampai 190 ribu
            if sisa == 0:
                hasil = seratus + ribu
            else:
                hasil = seratus + ribu + terbilang(sisa)
        else:  # Untuk angka 200 ribu ke atas
            if sisa == 0:
                hasil = terbilang(ratusanRibu) + ribu
            else:
                hasil = terbilang(ratusanRibu) + ribu + terbilang(sisa)

    elif 1000000 <= x <= 9999999:  # Untuk jutaan
        jutaan = x // 1000000
        sisa = x % 1000000
        if jutaan == 1:
            if sisa == 0:
                hasil = sejuta
            else:
                hasil = sejuta + terbilang(sisa)
        else:
            if sisa == 0:
                hasil = terbilang(jutaan) + juta
            else:
                hasil = terbilang(jutaan) + juta + terbilang(sisa)

    elif 10000000 <= x <= 99999999:  # Untuk puluhan juta
        puluhanJuta = x // 1000000
        sisa = x % 1000000
        if puluhanJuta == 1:
            if sisa == 0:
                hasil = angka[9] + juta
            else:
                hasil = angka[9] + juta + terbilang(sisa)
        else:
            if sisa == 0:
                hasil = terbilang(puluhanJuta) + juta
            else:
                hasil = terbilang(puluhanJuta) + juta + terbilang(sisa)

    else:
        hasil = "Angka di luar jangkauan"
    
    hasil = hasil.strip()
    return " ".join(hasil.split())


print("Konversi angka ke terbilang\n")
while True:
    try:
        a =input("Masukkan angka [1 - 99.999.999]: ")
        if a.lower() =='q':
            break
        a=int(a)
        print(terbilang(a))
        break
    except ValueError:
        print("Hanya angka atau 'q' untuk keluar")
