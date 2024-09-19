anak_anak = 30000
dewasa = 50000
lansia = 35000

total_harga_keseluruhan = 0
jumlah_penonton = int(input("masukan jumlah pembeli tiket :"))

for i in range (jumlah_penonton):
    usia = int(input("masukan usia anda :"))
    jumlah_tiket = int(input("jumlah tiket yang ingin dibeli :"))

    if usia <= 12:
        harga_tiket = anak_anak 
    elif usia <= 60:
        harga_tiket = dewasa
    else:
        harga_tiket = lansia

    total_harga_pembeli = harga_tiket * jumlah_tiket
    print (f"harga tiket untuk pembeli = {i+1}, dan jumlah total pembeliannya = {total_harga_pembeli} ")

    total_harga_keseluruhan = total_harga_keseluruhan + total_harga_pembeli
print (f"total harga tiket keseluruhan = {total_harga_keseluruhan}")