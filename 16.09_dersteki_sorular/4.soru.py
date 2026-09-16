
"""
  for Döngüsü ile Liste Üzerinde İşlem [5, 15, 8, 22, 3, 19] listesindeki en büyük sayıyı döngüyle bulun (max() kullanmadan). Bir liste içindeki tüm sayıların kaç tanesinin 10'dan büyük olduğunu sayan bir kod yazın.
  """

sayilar = [5, 15, 8, 22, 3, 19]

en_buyuk = sayilar[0]

for sayi in sayilar:
  if sayi > en_buyuk:
    en_buyuk = sayi

print("Listedeki en büyük sayı:", en_buyuk)

sayac = 0

for sayi in sayilar:
  if sayi > 10:
    sayac += 1

print("10'dan büyük sayı adedi:", sayac)