"""
while Döngüsü ile Basit Sayaç 10'dan 1'e geri sayan bir while döngüsü yazın. Kullanıcıdan şifre alıp doğru şifreyi girene kadar tekrar tekrar soran bir program yazın.
"""

sayac = 10

while sayac >= 1:
  print(sayac)
  sayac -= 1

print("Geri sayım bitti!")

dogru_sifre = "123"
girilen_sifre = ""

while girilen_sifre != dogru_sifre:
  girilen_sifre = input("Şifreyi girin: ")

  if girilen_sifre != dogru_sifre:
    print("Hatalı şifre, lütfen tekrar deneyin.")

print("Giriş başarılı! Hoş geldiniz.")