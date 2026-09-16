"""
elif ile Çoklu Koşullar Kullanıcıdan sıcaklık değeri alıp; 30 üstü "Sıcak", 15-30 arası "Ilıman", 15 altı "Soğuk" yazdıran bir program yazın. Kullanıcıdan bir ay numarası (1-12) alıp hangi mevsime ait olduğunu elif ile bulun.

"""

sicaklik = float(input("Hava sıcaklığını girin: "))

if sicaklik > 30:
  print("Hava Durumu: Sıcak")
elif sicaklik >= 15:
  print("Hava Durumu: Ilıman")
else:
  print("Hava Durumu: Soğuk")

ay = int(input("Ay numarasını girin: "))

if ay in (12, 1, 2):
  print("Mevsim: Kış")
elif ay in (3, 4, 5):
  print("Mevsim: İlkbahar")
elif ay in (6, 7, 8):
  print("Mevsim: Yaz")
elif ay in (9, 10, 11):
  print("Mevsim: Sonbahar")
else:
  print("Geçersiz ay numarası girdiniz! (1 ile 12 arasında olmalıdır)")
