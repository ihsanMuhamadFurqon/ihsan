class mahasiswa:
    nim="2207017"
    def __init__(self,nama,nim,umur,prodi):
        self.nama=nama
        self.nim=nim
        self.umur=umur
        self.prodi=prodi
    def __str__(self):
        return f"nama saya {self.nama} \nnim saya {self.nim}"
    def tahunlahir(self):
        return 2023 - self.umur
saya = mahasiswa("ihsan","2207017",19,"sistem informasi")
print(saya)
print("saya lahir pada tahun", saya.tahunlahir())
print("prodi", saya.prodi)
print("tahun angkatan", saya.nim[:2])