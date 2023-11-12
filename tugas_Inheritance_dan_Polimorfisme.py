class karyawan:
    def __init__(self, nama):
        self.nama = nama
        self.gaji_pokok = 4000000
        self.tunjangan_makan_harian = 30000

    def hitung_gaji(self):
        pass

    def print_gaji_detail(self):
        print(f"Detail gaji untuk {self.nama}:")
        print(f"gaji pokok: Rp {self.gaji_pokok}")
        print(f"tunjangan makan harian: Rp {self.tunjangan_makan_harian}")
        print(f"Total gaji: Rp {self.hitung_gaji()}")
        print()


class Manager(karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.tunjangan_profesional = 1500000
        self.tunjangan_transportasi_harian = 30000

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan_profesional + self.tunjangan_transportasi_harian


class Admin(karyawan):
    def __init__(self, nama, jam_lembur=0):
        super().__init__(nama)
        self.tarif_lembur = 40000
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        return self.gaji_pokok + (self.jam_lembur * self.tarif_lembur)


class Marketing(karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.tunjangan_transportasi_harian = 50000

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan_transportasi_harian


manager1 = Manager("John")
admin1 = Admin("Doe", 5)
marketing1 = Marketing("Alice")

manager1.print_gaji_detail()
admin1.print_gaji_detail()
marketing1.print_gaji_detail()
