jumlah_pasien = float(input("masukan jumlah pasien:"))
nama = input("masukan nama anda:")
print(nama)

for i in range (jumlah_pasien):
    berat = float(input("masukan bb:"))
    tinggi = float(input("masukan tb:"))

    bmi = ("bb/tb**2")
    if bmi < 19.5:
        print("kurus")
    elif bmi >= 19.5 and bmi < 24.9:
        print("normal")
    elif bmi >=25 and bmi <29.9:
        print("Kelebihan bb")
    else:
        print("invalid")