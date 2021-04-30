#Menggunakan Variabel
angka = 10

# Param 1 : Maksimal
for i in range(angka) :
  print("Angka ke : ")
  print(i)

# Param 2 : Min, Maks (Sifat Increment)
for i in range(angka, 20) :
  print("Angka ke : ")
  print(i)

# Param 3 : Min, Maks, Lompatan = (Bersifat Incre) / Maks, Min, Lompatan = (Bersifat Decre)
for i in range(angka, 1, -1) :
  print("Angka ke : ")
  print(i)

#Array
array = [1,2,3,4]

for i in array :
  print(i, end = '')