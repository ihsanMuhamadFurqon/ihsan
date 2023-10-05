kalimat = "ini adalah kalimat"
paragrap = """ini adalah paragrap. 
paragrap terdiri dari beberapa baris"""
print (kalimat)
print (paragrap)


kalimat = "ihsan muhamad furqon"
print(kalimat.upper())
print(kalimat.lower())
print(kalimat.capitalize())
print(kalimat.title())
print(kalimat.swapcase())
print(kalimat.replace("ihsan", "furqon"))
print(kalimat.replace("a", "o"))
print(kalimat.strip())
print(kalimat.split('.'))

a = "hallo guys. saya adalah programer."
tambahan = "saya ngoding pakai python."
print(a + tambahan)

umur = 23
rumah = 5
mobil = 4
emas = 10
a = "saya berumur {} tahun, rumah saya ada {}, dan mobil saya adaa {}, saya memiliki emas {} kilogram."
print(a.format(umur, rumah, mobil, emas))