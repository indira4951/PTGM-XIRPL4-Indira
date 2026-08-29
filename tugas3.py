suhu = float(input("Masukkan suhu: "))

if suhu <= 25:
    kondisi = "Dingin"
elif suhu <= 30:
    kondisi = "Normal"
else:
    kondisi = "Panas"

print(kondisi)