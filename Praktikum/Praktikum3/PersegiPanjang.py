class PersegiPanjang :

    # Construktor
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

    def ubahPanjang (self, p):
        self.panjang = p
    def ubahLebar (self, l):
        self.lebar = l
    def hitungLuas (self):
        return self.panjang * self.lebar
    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)
    def cetakLuas(self):
        print('luas persegi panjang = %.2f '% self.hitungLuas())
    def cetakKeliling(self):
        print('keliling persegi panjang = %.2f'% self.hitungKeliling())

objekPP1 = PersegiPanjang(10, 8)

objekPP2 = PersegiPanjang(9, 8)

objekPP3 = PersegiPanjang(8, 8)

objekPP1.cetakLuas()

objekPP1.cetakKeliling()

objekPP1.counter = 10