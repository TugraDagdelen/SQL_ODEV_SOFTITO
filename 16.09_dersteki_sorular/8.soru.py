"""
Fonksiyon + Koşul Birlikte Bir sayının pozitif, negatif veya sıfır olduğunu döndüren sayi_durumu adlı bir fonksiyon yazın. Üç sayı arasından en büyüğünü bulup döndüren bir fonksiyon yazın.
"""

def sayi_durumu(sayi):
  if sayi > 0:
    return "Pozitif"
  elif sayi < 0:
    return "Negatif"
  else:
    return "Sıfır"

print("15:", sayi_durumu(15))
print("-8:", sayi_durumu(-8))
print("0:", sayi_durumu(0))

def en_buyuk_bul(s1, s2, s3):
  if s1 >= s2 and s1 >= s3:
    return s1
  elif s2 >= s1 and s2 >= s3:
    return s2
  else:
    return s3

buyuk_sayi = en_buyuk_bul(24, 78, 45)
print("En büyük sayı:", buyuk_sayi)