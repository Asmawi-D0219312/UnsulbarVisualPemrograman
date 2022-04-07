#Class
class Mahasiswa:
    
    jumlah_mahasiswa = 0 #Variable
    
    def __init__(self, inputNama, inputNim):
        self.nama = inputNama
        self.nim = inputNim
        Mahasiswa.jumlah_mahasiswa += 1
        
awi = Mahasiswa("asmawi","D0219319")
asmawi = Mahasiswa("asmawi","D0219312")

print(Mahasiswa.jumlah_mahasiswa)