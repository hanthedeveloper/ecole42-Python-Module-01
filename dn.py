class Araba:
    tekerlek_sayisi = 4 

    def __init__(self, marka, renk):
        self.marka = marka
        self.renk = renk

araba1 = Araba("Toyota", "Kırmızı")

# 1. Instance'ın __dict__'i
# print(araba1.__dict__)

# 2. Class'ın __dict__'i
# print(Araba.__dict__)
# {'__module__': '__main__', '__firstlineno__': 1, 'tekerlek_sayisi': 4,
# '__init__': <function Araba.__init__ at 0x727aa0407110>,
# '__static_attributes__': ('marka', 'renk'),
# '__dict__': <attribute '__dict__' of 'Araba' objects>,
# '__weakref__': <attribute '__weakref__' of 'Araba' objects>, '__doc__': None}

import math

class Plant:
    name = "bıtkı"

print(isinstance(Plant, object))
print(isinstance(42, object))           # True (Tam sayı bir nesnedir)
print(isinstance("merhaba", object))    # True (Metin bir nesnedir)
print(isinstance(True, object))         # True (Boolean bir nesnedir)
print(isinstance(print, object))        # True (Yerleşik print fonksiyonu bile bir nesnedir!)
print(isinstance(math, object))         # True (import ettiğin modül bile bir nesnedir!)
print(isinstance(None, object))         # True (Hiçlik anlamına gelen None bile bir nesnedir!)



elma = print # fonskyıonlar da nesne oldukları ıcın degıskenlere atanabılıyolar
elma("elma bu cumleyı yazdırdı. >< yay! ^^")

class Kutlama:
    pass

def sinifi_calistir(gelen_sinif):
    ornek = gelen_sinif()
    print("Gelen sınıfın türü:", type(ornek))

sinifi_calistir(Kutlama)

print(dir(5))