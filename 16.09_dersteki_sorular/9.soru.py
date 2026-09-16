"""
Liste Oluşturma ve İşleme Boş bir liste oluşturup kullanıcıdan 5 tane şehir adı alıp listeye ekleyin, sonra listeyi numaralandırarak yazdırın. Bir listeye eklenen ürünlerden istenilen birini remove() ile silin ve güncel listeyi gösterin
"""

sehirler = []

sehir1 = input("1. şehri yazın: ")
sehirler.append(sehir1)

sehir2 = input("2. şehri yazın: ")
sehirler.append(sehir2)

sehir3 = input("3. şehri yazın: ")
sehirler.append(sehir3)

sehir4 = input("4. şehri yazın: ")
sehirler.append(sehir4)

sehir5 = input("5. şehri yazın: ")
sehirler.append(sehir5)

print("\nEklenen Şehirler:")
sayac = 1
for sehir in sehirler:
  print(sayac, "-", sehir)
  sayac = sayac + 1

urunler = ["Elma", "Ekmek", "Süt", "Peynir"]
print("Mevcut liste:", urunler)

silinecek = input("Silmek istediğin ürünü gir: ")
urunler.remove(silinecek)

print("Güncel liste:", urunler)