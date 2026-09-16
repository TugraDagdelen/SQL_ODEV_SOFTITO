"""
Değişkenlerle Basit Hesaplamalar Bir ürünün birim fiyatını ve adedini değişkenlerde tutup toplam tutarı hesaplayın. maas adlı bir değişkene 8000 değeri verin, sonra += kullanarak 1500 TL zam ekleyip yeni maaşı yazdırın."""
birim_fiyat = 125.50
adet = 4
toplam_tutar = birim_fiyat * adet

print("Birim Fiyat:", birim_fiyat, "TL")
print("Adet:", adet)
print("Toplam Tutar:", toplam_tutar, "TL")

maas = 8000
maas += 1500

print("Yeni Maaş:", maas, "TL")