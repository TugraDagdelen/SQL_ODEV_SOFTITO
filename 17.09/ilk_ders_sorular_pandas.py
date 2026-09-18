import pandas as pd


"""
Pandas Kurulumu ve İçe Aktarma Pandas kütüphanesini pd takma adıyla içe aktaran kodu yazın. Pandas'ın hangi versiyonda kurulu olduğunu pd.version ile kontrol edin.
"""
print(pd.__version__)

print("-----------------------------------------")

"""
Series — Tek Boyutlu Veri Yapısı [100, 200, 300, 400] değerlerinden bir Series oluşturup yazdırın. Şehir isimlerini index, nüfuslarını değer olarak kullanan bir Series oluşturun (en az 4 şehir). Oluşturduğunuz Series'ten belirli bir şehrin nüfusunu index adıyla seçip yazdırın. Bir Series'teki tüm değerlerin toplamını .sum() ile bulun.
"""
seri1 = pd.Series([100,200,300,400])
print(seri1)

nufus= pd.Series([1600000,5000000,4000000,2000000],
index=["İstanbul","Ankara","İzmir","Bursa"]
)

print("Şehir Nüfusları:\n",nufus)

print("Toplam Nüfus:",nufus.sum())

print("-----------------------------------------")

"""
DataFrame — Tablo Yapısı urun, fiyat ve stok sütunlarından oluşan, en az 5 satırlık bir DataFrame oluşturun. Sınıf arkadaşlarınızın isim, yaş ve bölüm bilgilerini içeren bir DataFrame oluşturup yazdırın. Oluşturduğunuz DataFrame'in kaç satır ve kaç sütundan oluştuğunu söyleyin (koda bakmadan tahmin edip sonra kontrol edin).
"""

urun_verisi = {
    "urun": ["Laptop", "Kablosuz Mouse", "Mekanik Klavye", "Monitör", "Kulaklık"],
    "fiyat": [28000, 450, 1500, 4200, 950],
    "stok": [12, 85, 40, 25, 60]
}

urunler_df = pd.DataFrame(urun_verisi)
print("--- ÜRÜN TABLOSU ---")
print(urunler_df)

ogrenci_verisi = {
    "isim": ["Berkay", "Ebrar", "Sude", "Ömer"],
    "yas": [21, 21, 22, 21],
    "bolum": [
        "Bilgisayar Mühendisliği",
        "Bilgisayar Mühendisliği",
        "Yazılım Mühendisliği",
        "Bilgisayar Mühendisliği"
    ]
}

ogrenciler_df = pd.DataFrame(ogrenci_verisi)

print("\n--- ÖĞRENCİ TABLOSU ---")
print(ogrenciler_df)

boyut = ogrenciler_df.shape

print("\nTablonun Boyutu (Satır, Sütun):", boyut)
print(f"Gerçekleşen: {boyut[0]} satır ve {boyut[1]} sütun.")


print("-----------------------------------------")


"""
CSV Dosyası Okuma ve Yazma Sorular 3'te oluşturduğunuz DataFrame'i ogrenciler.csv adıyla kaydedin. Kaydettiğiniz CSV dosyasını tekrar okuyup ekrana yazdırın. index=False parametresini kullanmadan bir CSV kaydedin ve dosyayı açıp aradaki farkı gözlemleyin.
"""

df = pd.read_csv("17.09\calisanlar.csv")
print("--- CSV'DEN OKUNAN TABLO ---")
print(df)

print("-----------------------------------------")

"""
Veriyi İnceleme (İlk Bakış) Bir DataFrame oluşturup .head() ve .tail() ile ilk 3 ve son 2 satırını görüntüleyin. .shape ile DataFrame'in boyutunu öğrenin. .info() kullanarak sütunların veri tiplerini inceleyin. .describe() ile sayısal bir sütunun (örneğin yaş veya maaş) ortalama, min ve max değerlerini bulun.
"""

df = pd.read_csv("17.09/calisanlar.csv")

print("--- İLK 3 SATIR ---")
print(df.head(3))

print("\n--- SON 2 SATIR ---")
print(df.tail(2))

print("\n--- BOYUT (Satır, Sütun) ---")
print(df.shape)

print("\n--- SÜTUN BİLGİLERİ ---")
df.info()

print("\n--- SAYISAL ÖZET ---")
print(df.describe())

print("-----------------------------------------")


"""
Sütun ve Satır Seçme Bir DataFrame'den sadece "isim" sütununu seçip yazdırın. "isim" ve "yas" sütunlarını birlikte seçip yazdırın. .loc[] kullanarak DataFrame'in ilk 3 satırını seçin. .iloc[] kullanarak 2. satır ile 2. sütunun kesiştiği değeri bulun.
"""

df = pd.read_csv("17.09/calisanlar.csv")
print(df["isim"])
print(df[["isim", "yas"]])
print(df.loc[0:2])
print(df.iloc[1, 1])

print("-----------------------------------------")

"""
Filtreleme (Koşullu Seçim) Yaşı 25'ten büyük olan kişileri filtreleyip listeleyin. Maaşı 20000 ile 30000 arasında olan kişileri bulun (iki koşulu & ile birleştirin). Belirli bir şehirde (örneğin "İstanbul") yaşayan kişileri filtreleyin. Yaşı 20'den küçük VEYA 40'tan büyük olanları | operatörüyle bulun.
"""

df = pd.read_csv("17.09/calisanlar.csv")

print(df[df["yas"] > 25])

print(df[(df["maas"] >= 20000) & (df["maas"] <= 30000)])

print(df[df["sehir"] == "İstanbul"])

print(df[(df["yas"] < 20) | (df["yas"] > 40)])

print("-----------------------------------------")


"""
Yeni Sütun Ekleme ve Güncelleme Bir DataFrame'e "dogum_yili" sütunu ekleyin (2026 - yas formülüyle). Maaş sütunundaki tüm değerleri %10 artırıp güncelleyin. apply() ve lambda kullanarak yaşı 18'den büyük olanlara "Yetişkin", küçük olanlara "Çocuk" yazan yeni bir sütun oluşturun.
"""

df = pd.read_csv("17.09/calisanlar.csv")

df["dogum_yili"] = 2026 - df["yas"]

df["maas"] = df["maas"] * 1.10

df["durum"] = df["yas"].apply(lambda x: "Yetişkin" if x >= 18 else "Çocuk")

print(df)


print("-----------------------------------------")

"""
Sıralama Bir DataFrame'i "yas" sütununa göre küçükten büyüğe sıralayın. Aynı DataFrame'i "maas" sütununa göre büyükten küçüğe sıralayın. İki sütuna göre aynı anda sıralama yapın (örneğin önce "sehir", sonra "yas").
"""
df = pd.read_csv("17.09/calisanlar.csv")
print(df.sort_values(by="yas"))
print(df.sort_values(by="maas", ascending=False))
print(df.sort_values(by=["sehir", "yas"]))

print("-----------------------------------------")

"""
Bonus Mini Ödev: Sınıfınızdaki (hayali) 6 öğrencinin isim, üç ders notu ve şehir bilgisini içeren bir DataFrame oluşturun. Ortalaması 70'in üzerinde olan öğrencileri filtreleyip, sonucu yaşa göre sıralayıp yazdırın.
"""

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif"],
    "yas": [21, 20, 23, 22, 19, 21],
    "sehir": ["İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul", "Ankara"],
    "not1": [60, 85, 45, 90, 75, 55],
    "not2": [70, 90, 50, 95, 80, 60],
    "not3": [65, 80, 60, 85, 70, 50]
}
df = pd.DataFrame(veri)

df["ortalama"] = (df["not1"] + df["not2"] + df["not3"]) / 3

basarililar = df[df["ortalama"] > 70]

sonuc = basarililar.sort_values(by="yas")

print(sonuc)