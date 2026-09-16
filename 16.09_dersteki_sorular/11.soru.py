"""
Küçük Bir Uygulama — Not Ortalaması Hesaplama Kullanıcıdan 4 dersin notunu alıp ortalamayı hesaplayan ve harf notuna (AA, BA, BB...) çeviren bir program yazın. Girilen notlardan en yüksek ve en düşük notu bulup ekrana yazdırın.
"""

not1 = float(input("1. ders notunu girin: "))
not2 = float(input("2. ders notunu girin: "))
not3 = float(input("3. ders notunu girin: "))
not4 = float(input("4. ders notunu girin: "))

toplam = not1 + not2 + not3 + not4
ortalama = toplam / 4

print("Not Ortalamanız:", ortalama)

if ortalama >= 90:
  harf_notu = "AA"
elif ortalama >= 85:
  harf_notu = "BA"
elif ortalama >= 80:
  harf_notu = "BB"
elif ortalama >= 75:
  harf_notu = "CB"
elif ortalama >= 70:
  harf_notu = "CC"
elif ortalama >= 60:
  harf_notu = "DC"
elif ortalama >= 50:
  harf_notu = "DD"
else:
  harf_notu = "FF"

print("Harf Notunuz:", harf_notu)


notlar = [not1, not2, not3, not4]

en_yuksek = notlar[0]
en_dusuk = notlar[0]

for not_degeri in notlar:
  if not_degeri > en_yuksek:
    en_yuksek = not_degeri
  if not_degeri < en_dusuk:
    en_dusuk = not_degeri

print("En Yüksek Not:", en_yuksek)
print("En Düşük Not:", en_dusuk)