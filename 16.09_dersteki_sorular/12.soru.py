"""
Küçük Bir Uygulama — Basit Sepet/Alışveriş Sepete eklenen ürünlerden 100 TL üzeri olanları ayrıca listeleyen bir program yazın. Toplam tutar 500 TL üzerindeyse "%10 indirim kazandınız" mesajı gösteren bir alışveriş programı yazın.
"""

fiyatlar = [45, 120, 80, 250, 150]
print("Sepetteki tüm fiyatlar:", fiyatlar)

pahali_urunler = []

for fiyat in fiyatlar:
  if fiyat > 100:
    pahali_urunler.append(fiyat)

print("100 TL üzeri ürünler:", pahali_urunler)

toplam_tutar = 0

for fiyat in fiyatlar:
  toplam_tutar = toplam_tutar + fiyat

print("Toplam Tutar:", toplam_tutar, "TL")

if toplam_tutar > 500:
  print("Tebrikler! %10 indirim kazandınız.")
  indirimli_tutar = toplam_tutar - (toplam_tutar * 0.10)
  print("Ödenecek indirimli tutar:", indirimli_tutar, "TL")
else:
  print("İndirim için 500 TL üzeri harvcama yap.")