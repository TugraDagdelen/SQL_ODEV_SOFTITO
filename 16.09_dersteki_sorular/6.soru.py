"""
Döngü İçinde Koşul Kullanma 1'den 20'ye kadar olan sayılardan sadece 3'e tam bölünenleri yazdırın. Bir liste içindeki sayılardan negatif olanları ayrı, pozitif olanları ayrı yazdırın.
"""

for sayi in range(1, 21):
  if sayi % 3 == 0:
    print(sayi)

sayilar = [-12, 5, 0, -3, 18, -7, 24, -1, 9]

pozitifler = []
negatifler = []

for sayi in sayilar:
  if sayi > 0:
    pozitifler.append(sayi)
  elif sayi < 0:
    negatifler.append(sayi)

print("Pozitif sayılar:", pozitifler)
print("Negatif sayılar:", negatifler)
