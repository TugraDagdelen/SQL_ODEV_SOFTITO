"""
Araba Sınıfı
python

marka, model ve hiz (km/s) bilgilerini tutan bir Araba sınıfı oluşturun.
hızlandır(artis) metodu ile hızı artırın.
bilgi_goster() metodu ile araç bilgilerini yazdırın.
"""

class Araba:

    def __init__(self,marka,model,hiz=0):
        self.marka = marka
        self.model = model
        self.hiz = hiz

    def hizlandir(self,artis):
        self.hiz += artis
        print(f"ARAÇ HIZLANDI GÜNCEL HIZ {self.hiz}km")


    def bilgi_goster(self):
        print(f"marka: {self.marka}")
        print(f"model: {self.model}")
        print(f"hiz: {self.hiz}")


araba1= Araba("BMW","M5")

araba1.bilgi_goster()

araba1.hizlandir(150)

araba1.hizlandir(20)

araba1.bilgi_goster()

print("-----------------------------------")
"""
Dikdörtgen Sınıfı
python

uzunluk ve genislik bilgilerini tutan bir Dikdortgen sınıfı oluşturun.
alan_hesapla() metodu ile alanı hesaplayın (uzunluk * genislik).
cevre_hesapla() metodu ile çevreyi hesaplayın (2 * (uzunluk + genislik)).
"""


class Dikdortgen:

    def __init__(self,uzunluk,genislik):
        self.uzunluk=uzunluk
        self.genislik=genislik

    def alan_hesaplama(self):
        alan = self.uzunluk *self.genislik
        return alan

    def cevre_hesaplama(self):
        cevre=2*(self.uzunluk + self.genislik)
        return cevre

dikdortgen1= Dikdortgen(10,5)

alan_sonucu= dikdortgen1.alan_hesaplama()
print(alan_sonucu)

cevre_sonucu= dikdortgen1.cevre_hesaplama()
print(cevre_sonucu)


print("-----------------------------------")


"""
Kitap Sınıfı
python

ad, yazar ve sayfa_sayisi bilgilerini tutan bir Kitap sınıfı oluşturun.
ozet() metodu ile "Suç ve Ceza - Dostoyevski (671 sayfa)" formatında bilgi döndürün.
"""
class Kitap:

    def __init__(self,ad,yazar,sayfa_sayisi):
        self.ad=ad
        self.yazar=yazar
        self.sayfa_sayisi = sayfa_sayisi

    def ozet(self):
        return f"{self.ad} -{self.yazar} - {self.sayfa_sayisi} kadar sayfa"

kitap1=Kitap("Kürk Mantolu Madonna","Sabahattin Ali",160)

print(kitap1.ozet())