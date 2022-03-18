#Asmawi (D0219312)

class Jenis_ikan:
    def __init__(self, inputJenis, inputHabitat, inputHarga):
        self.nama = inputJenis
        self.tinggal = inputHabitat
        self.jual = inputHarga

ikan1 = Jenis_ikan("Cupang","Rawa-rawa",250000 )
ikan2 = Jenis_ikan("Cumi-cumi","Lautan",30000)

print(ikan2.nama, ikan2.jual)