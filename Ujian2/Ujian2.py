pasien = int(input("masukan ukuran"))

for i in range (pasien):
    berat = int(input("masukan berat badan (kg): "))
    tinggi = int(input("masukan tinggi badan (m): "))

bmi = ("berat badan / tinggi badan^2")

if bmi < 18.5:
    print("kurus")
elif bmi == 18.5 <=bmi  <24.9:
    print("normal")
elif bmi  == 25 <=bmi <29.9:
    print("kelebihan berat badan")
else:
    print("obesitas")