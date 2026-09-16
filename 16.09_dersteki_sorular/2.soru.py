"""
İç İçe (Nested) if-else Kullanıcıdan yaş ve öğrenci olup olmadığı bilgisini alıp; 65 yaş üstü ise "Ücretsiz", öğrenci ise "İndirimli", diğer durumda "Tam ücret" yazdıran bir program yazın. Bir sayının hem pozitif hem de çift olup olmadığını iç içe if ile kontrol edin.
"""

yas = int(input("Yaşınızı girin: "))

if yas >= 65:
  print("Ücret Durumu: Ücretsiz")
else:
  ogrenci = input("Öğrenci misiniz? (evet / hayır): ")

  if ogrenci == "evet":
    print("Ücret Durumu: İndirimli")
  else:
    print("Ücret Durumu: Tam ücret")

sayi = int(input("Bir tam sayı girin: "))

if sayi > 0:
  if sayi % 2 == 0:
    print("Sayı hem pozitif hem de çifttir.")
  else:
    print("Sayı pozitiftir ama tektir.")
else:
  print("Sayı pozitif değildir.")