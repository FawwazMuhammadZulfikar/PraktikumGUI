try:
    a = int(input('masukkan nilai a: '))
    b = int(input('masukan nilai b: '))
    c = a / b
    print(f"{a} / {b} = {c}")

except ZeroDivisionError as e:
    print('Error : Tidak boleh bagi 0')

# Try.. Except..finally
f = ''

try:
    f = open('contoh.txt', 'r')
    liners = f.readlines()
    for line in lines:
        print(line, end='\n')

except IOError as e:
    print('Error : File Hilang')

finally:
    if f:
        f.close()