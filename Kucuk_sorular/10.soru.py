"""
Kullanıcıdan Birden Fazla Veri Alma Kullanıcıdan ad, soyad ve doğum yılını alıp yaşını hesaplayan (2026'ya göre) bir program yazın. Kullanıcıdan boy (cm) ve kilo bilgisi alıp basit BMI (vücut kitle indeksi) hesaplayan bir program yazın.

"""

ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
dogum_yili = int(input("Doğum yılınızı girin: "))

yas = 2026 - dogum_yili

print("Merhaba", ad, soyad)
print("Yaşınız:", yas)

boy_cm = float(input("Boyunuzu girin cm cinsi: "))
kilo = float(input("Kilonuzu girin kg cinsi: "))

boy_metre = boy_cm / 100

bmi = kilo / (boy_metre * boy_metre)

print("Vücut Kitle İndeksiniz (BMI):",bmi)