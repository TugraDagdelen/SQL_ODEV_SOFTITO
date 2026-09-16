print("Python öğreniyorum")
print("Tuğra", "Dağdelen")
print(42)
print(" SELAM")
print("ÇIKTIII")

sehir = "İstanbul"
print(sehir)

puan = 50
print("İlk puan:", puan)

puan = 75
print("Güncel puan:", puan)

tam_sayi = 25
ondalikli = 3.14
yazi = "Python"
aktif_mi = True

print(type(tam_sayi))
print(type(ondalikli))
print(type(yazi))
print(type(aktif_mi))

tip_1 = type(10)
tip_2 = type("10")
print("10 ve '10' aynı tip mi:", tip_1 == tip_2)

sayi1 = 15
sayi2 = 4

print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)
print("Bölüm:", sayi1 / sayi2)

print("Kalan (17 % 5):", 17 % 5)

print("2 üzeri 8:", 2**8)

ad = input("Adınızı girin: ")
print(f"Merhaba, {ad}!")

yas = int(input("Yaşınızı girin: "))
print("10 yıl sonraki yaşınız:", yas + 10)

a = 8
b = 12

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)

girilen_sayi = int(input("Bir sayı girin: "))
print("Sayı 100'e eşit mi?:", girilen_sayi == 100)

yas = 22
ogrenci_mi = False

print("yas > 18 and ogrenci_mi:", (yas > 18) and ogrenci_mi)
print("yas > 18 or ogrenci_mi:", (yas > 18) or ogrenci_mi)
print("not ogrenci_mi:", not ogrenci_mi)

kisi_yasi = 20
kayitli_mi = True
kosul_saglandi = (kisi_yasi > 18) and kayitli_mi
print("18'den büyük ve kayıtlı mı?:", kosul_saglandi)


sayi = float(input("Bir sayı girin: "))

if sayi > 0:
  print("Sayı pozitif")
elif sayi < 0:
  print("Sayı negatif")
else:
  print("Sayı sıfır")


  not_degeri = float(input("Sınav notunuzu girin: "))

if not_degeri >= 50:
  print("Geçti")
else:
  print("Kaldı")


  ad = "Tuğra"
soyad = "Dağdelen"
tam_ad = ad + " " + soyad
print("Tam Ad:", tam_ad)

kelime = "Yazılım"
print("Harf sayısı:", len(kelime))

metin = "Python Dersi"
print("Büyük harf:", metin.upper())
print("Küçük harf:", metin.lower())

sayi_a = float(input("Birinci sayıyı girin: "))
sayi_b = float(input("İkinci sayıyı girin: "))
print("Çarpım:", sayi_a * sayi_b)

kare_icin_sayi = float(input("Karesi alınacak sayıyı girin: "))
print("Sayının karesi:", kare_icin_sayi**2)
