"""
Basit Fonksiyon Tanımlama Bir sayının küpünü (3. kuvvetini) alan kup_al adlı bir fonksiyon yazın. İki sayıyı parametre olarak alıp toplamını döndüren bir fonksiyon yazın.
"""

def kup_al(sayi):
  return sayi**3

sonuc_kup = kup_al(4)
print("4'ün küpü:", sonuc_kup)

def topla(sayi1, sayi2):
  return sayi1 + sayi2

sonuc_toplam = topla(15, 27)
print("Toplam:", sonuc_toplam)