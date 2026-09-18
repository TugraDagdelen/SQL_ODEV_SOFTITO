import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
---## Bölüm 1 — SeriesSoru 1.1: Bir kırtasiyedeki ürünlerin stok adetlerini tutan bir Series oluşturun: index = ['Kalem','Defter','Silgi','Cetvel'], değerler = [300, 150, 80, 45].Soru 1.2: 'Silgi' ürününün stok adedini index adıyla seçip yazdırın.Soru 1.3: Stoğu en az olan ürünü .idxmin() ile bulun.Soru 1.4: Tüm ürünlerin toplam stok adedini .sum() ile hesaplayın.
"""

# Soru 1.1: Stok adetlerini tutan Series oluşturma
urunler = ["Kalem", "Defter", "Silgi", "Cetvel"]
stoklar = [300, 150, 80, 45]

stok_serisi = pd.Series(data=stoklar, index=urunler)
print(stok_serisi)

# Soru 1.2: 'Silgi' ürününün stok adedini index adıyla seçme
silgi_stok = stok_serisi["Silgi"]
print("Silgi adedi:", silgi_stok)

# Soru 1.3: Stoğu en az olan ürünü .idxmin() ile bulma
en_az_urun = stok_serisi.idxmin()
print("En az stoğu olan ürün:", en_az_urun)

# Soru 1.4: Tüm ürünlerin toplam stok adedini .sum() ile hesaplama
toplam_stok = stok_serisi.sum()
print("Toplam stok adedi:", toplam_stok)

print("----------------------------------------")

"""
---## Bölüm 2 — DataFrame OluşturmaSoru 2.1: Bir spor salonundaki üyeleri temsil eden, uye_adi, paket_turu (örn. Aylık, Yıllık) ve odenen_tutar sütunlarından oluşan, en az 5 satırlık bir DataFrame oluşturun.Soru 2.2: .shape ile kaç üye ve kaç bilgi sütunu olduğunu kontrol edin.Soru 2.3: .columns ile sütun isimlerini listeleyin.
"""

# Soru 2.1: Spor salonu üyeleri için DataFrame oluşturma
veri = {
    'uye_adi': ['Ahmet', 'Ayşe', 'Mehmet', 'Zeynep', 'Can'],
    'paket_turu': ['Aylık', 'Yıllık', 'Aylık', 'Yıllık', 'Aylık'],
    'odenen_tutar': [1500, 12000, 1500, 13500, 1600]
}

df = pd.DataFrame(veri)
print(df)

# Soru 2.2: .shape ile satır ve sütun sayısını kontrol etme
satir_sutun_sayisi = df.shape
print("Boyut (Satır, Sütun):", satir_sutun_sayisi)

# Soru 2.3: .columns ile sütun isimlerini listeleme
sutunlar = df.columns
print("Sütun İsimleri:", sutunlar)

print("----------------------------------------")

"""
---## Bölüm 3 — CSV/Excel Okuma (Kavramsal)Gerçek bir dosyanız olmasa da sözdizimini test edelim.Soru 3.1: "satislar.csv" adlı bir dosyayı okuyup df_csv değişkenine atayan kodu yazın (dosya olmadığı için hata verecektir, bu normaldir — sadece doğru sözdizimini yazın).Soru 3.2: "rapor.xlsx" adlı bir Excel dosyasını okuyup df_excel değişkenine atayan kodu yazın.
"""

# Soru 3.1: CSV dosyasını okuma
df_csv = pd.read_csv("17.09/satislar.csv")

# Soru 3.2: Excel dosyasını okuma
df_excel = pd.read_excel("rapor.xlsx")

print("----------------------------------------")

"""
---## Bölüm 4 — Veriyi İncelemeAşağıdaki hücreyi çalıştırarak bir e-ticaret sipariş verisi oluşturun:
"""

df = pd.DataFrame({
    "siparis_no": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "kargo_suresi": [2, 5, 3, np.nan, 1, 4, 6],
    "urun_adedi": [1, 3, 2, 5, 1, 2, 4],
    "toplam_tutar": [150.0, 480.5, 220.0, 610.0, 90.0, 310.0, 720.0],
})
print(df)

# Soru 4.1: İlk 3 ve son 2 siparişi görüntüleme
print("--- İlk 3 Sipariş ---")
print(df.head(3))

print("\n--- Son 2 Sipariş ---")
print(df.tail(2))

# Soru 4.2: Eksik verileri tespit etme (.info() kargo_suresi sütununda 6 non-null olduğunu gösterir, yani 1 eksik var)
print("\n--- Veri Özeti (info) ---")
df.info()

# Soru 4.3: Sayısal sütunların istatistiklerini inceleme
print("\n--- İstatistiksel Özet (describe) ---")
print(df.describe())

print("----------------------------------------")

"""
---## Bölüm 5 — Sütun ve Satır SeçmeYukarıdaki sipariş `df`'ini kullanarak:**Soru 5.1:** Sadece `siparis_no` ve `toplam_tutar` sütunlarını seçip yazdırın.**Soru 5.2:** `.loc[]` ile 0'dan 3'e kadar olan (0-3 dahil) satırları seçin.**Soru 5.3:** `.iloc[]` ile ilk 4 satırın son 2 sütununu seçin.
"""

# Soru 5.1: Sadece siparis_no ve toplam_tutar sütunlarını seçme (çift köşeli parantez kullanılır)
sutunlar = df[["siparis_no", "toplam_tutar"]]
print("--- Soru 5.1 ---")
print(sutunlar)

# Soru 5.2: .loc[] ile 0'dan 3'e kadar satırları seçme (etiket bazlıdır, 3 dahildir)
satirlar_loc = df.loc[0:3]
print("\n--- Soru 5.2 (.loc) ---")
print(satirlar_loc)

# Soru 5.3: .iloc[] ile ilk 4 satır (0:4) ve son 2 sütun (-2:) seçimi (indeks/sıra bazlıdır, bitiş dahil değildir)
secim_iloc = df.iloc[0:4, -2:]
print("\n--- Soru 5.3 (.iloc) ---")
print(secim_iloc)

print("----------------------------------------")

"""
---## Bölüm 6 — Filtreleme ve Yeni SütunSoru 6.1: Toplam tutarı 300 TL'nin üzerinde olan siparişleri filtreleyin.Soru 6.2: Ürün adedi 2'den fazla VE toplam tutar 200 TL'den fazla olan siparişleri bulun (& kullanın).Soru 6.3: birim_fiyat adında yeni bir sütun ekleyin; değeri toplam_tutar / urun_adedi olsun.Soru 6.4: apply ve lambda kullanarak kargo süresi 3 günden fazlaysa "Yavaş", değilse "Hızlı" yazan bir kargo_durumu sütunu oluşturun.
"""

# Soru 6.1: Toplam tutarı 300 TL'nin üzerinde olan siparişler
tutar_300_ustu = df[df["toplam_tutar"] > 300]
print("--- Soru 6.1 ---")
print(tutar_300_ustu)

# Soru 6.2: Ürün adedi > 2 VE toplam tutar > 200 olanlar (& ile her şart parantez içine alınır)
coklu_filtre = df[(df["urun_adedi"] > 2) & (df["toplam_tutar"] > 200)]
print("\n--- Soru 6.2 ---")
print(coklu_filtre)

# Soru 6.3: birim_fiyat adında yeni bir sütun ekleme
df["birim_fiyat"] = df["toplam_tutar"] / df["urun_adedi"]
print("\n--- Soru 6.3 ---")
print(df[["siparis_no", "birim_fiyat"]])

# Soru 6.4: apply ve lambda ile kargo_durumu sütunu ekleme
df["kargo_durumu"] = df["kargo_suresi"].apply(
    lambda x: "Yavaş" if x > 3 else "Hızlı"
)
print("\n--- Soru 6.4 (Tablonun Son Hali) ---")
print(df)

print("----------------------------------------")

"""
---## Bölüm 7 — SıralamaSoru 7.1: Siparişleri toplam_tutar sütununa göre büyükten küçüğe sıralayın.Soru 7.2: Siparişleri önce urun_adedi, sonra kargo_suresi sütununa göre (ikisi de küçükten büyüğe) sıralayın (bir listede iki sütun verin).
"""

# Soru 7.1: Toplam tutara göre büyükten küçüğe sıralama (ascending=False)
sirali_tutar = df.sort_values(by="toplam_tutar", ascending=False)
print("--- Soru 7.1 ---")
print(sirali_tutar)

# Soru 7.2: Önce urun_adedi, sonra kargo_suresi sütununa göre küçükten büyüğe sıralama
sirali_coklu = df.sort_values(by=["urun_adedi", "kargo_suresi"], ascending=True)
print("\n--- Soru 7.2 ---")
print(sirali_coklu)

print("----------------------------------------")

"""
---## Bölüm 8 — Eksik Veri (NaN)Soru 8.1: kargo_suresi sütununda kaç eksik değer olduğunu bulun.Soru 8.2: Eksik kargo süresini sütunun medyanı ile doldurup df_dolu adlı yeni bir DataFrame oluşturun.Soru 8.3: Eksik değer içeren satırı silerek df_temiz adlı yeni bir DataFrame oluşturun ve satır sayısının değiştiğini .shape ile doğrulayın.
"""

# Soru 8.1: kargo_suresi sütununda kaç eksik değer olduğunu bulma
eksik_sayisi = df['kargo_suresi'].isna().sum()
print("kargo_suresi eksik değer sayısı:", eksik_sayisi)

# Soru 8.2: Eksik değerleri medyan ile doldurup df_dolu oluşturma
medyan_deger = df['kargo_suresi'].median()
df_dolu = df.copy()
df_dolu['kargo_suresi'] = df_dolu['kargo_suresi'].fillna(medyan_deger)
print("\n--- df_dolu (Eksik veriler medyan ile dolduruldu) ---")
print(df_dolu[['siparis_no', 'kargo_suresi']])

# Soru 8.3: Eksik değer içeren satırları silerek df_temiz oluşturma ve .shape kontrolü
df_temiz = df.dropna()
print("\n--- df_temiz Boyut Kontrolü ---")
print("Orijinal df boyutu:", df.shape)
print("df_temiz boyutu:   ", df_temiz.shape)

print("----------------------------------------")

"""
---## Bölüm 9 — Merge (Tabloları Birleştirme)Aşağıdaki iki tabloyu kullanın:

musteriler = pd.DataFrame({    "musteri_id": [1, 2, 3, 4],    "ad": ["Baran", "Ceylin", "Emre", "Fulya"]})siparisler = pd.DataFrame({    "musteri_id": [1, 2, 5],    "urun": ["Kulaklık", "Şarj Kablosu", "Powerbank"],    "tutar": [450, 90, 320]})

Soru 9.1: musteriler ve siparisler tablolarını inner join ile birleştirin — kaç müşterinin siparişi eşleşiyor?Soru 9.2: Aynı tabloları left join ile birleştirin — hiç siparişi olmayan müşteri(ler) sonuçta ne görünüyor?Soru 9.3: Aynı tabloları outer join ile birleştirip, hem eşleşmeyen müşterileri hem eşleşmeyen siparişleri gözlemleyin.
"""
musteriler = pd.DataFrame({
    "musteri_id": [1, 2, 3, 4],
    "ad": ["Baran", "Ceylin", "Emre", "Fulya"],
})

siparisler = pd.DataFrame({
    "musteri_id": [1, 2, 5],
    "urun": ["Kulaklık", "Şarj Kablosu", "Powerbank"],
    "tutar": [450, 90, 320],
})

# Soru 9.1: Inner Join (Sadece her iki tabloda da ortak olan musteri_id'ler gelir)
df_inner = pd.merge(musteriler, siparisler, on="musteri_id", how="inner")
print("--- Soru 9.1: Inner Join ---")
print(df_inner)
print(
    f"Eşleşen müşteri sayısı: {len(df_inner)}"
)  # 2 müşteri eşleşir: Baran ve Ceylin

# Soru 9.2: Left Join (musteriler tablosundaki herkes kalır, siparişi olmayanlara NaN gelir)
df_left = pd.merge(musteriler, siparisler, on="musteri_id", how="left")
print("\n--- Soru 9.2: Left Join ---")
print(df_left)
# Emre ve Fulya'nın siparişi olmadığı için urun ve tutar kısımlarında NaN (boş) görünür.

# Soru 9.3: Outer Join (Her iki tablodaki tüm kayıtlar gelir, eşleşmeyen alanlar NaN olur)
df_outer = pd.merge(musteriler, siparisler, on="musteri_id", how="outer")
print("\n--- Soru 9.3: Outer Join ---")
print(df_outer)
# Hem siparişi olmayan Emre ve Fulya hem de müşterisi tabloda olmayan 5 numaralı sipariş listelenir.

print("----------------------------------------")


"""
---## Bölüm 10 — ConcatSoru 10.1: hafta1 = pd.DataFrame({"gun":["Pzt","Sal"], "adet":[20,35]}) ve hafta2 = pd.DataFrame({"gun":["Çar","Per"], "adet":[28,40]}) tablolarını ignore_index=True ile alt alta birleştirin.Soru 10.2: gelir = pd.DataFrame({"toplam_gelir":[1000,1750]}) tablosunu, hafta1 tablosuyla axis=1 kullanarak yan yana birleştirin.
"""

# Tabloların oluşturulması
hafta1 = pd.DataFrame({"gun": ["Pzt", "Sal"], "adet": [20, 35]})
hafta2 = pd.DataFrame({"gun": ["Çar", "Per"], "adet": [28, 40]})
gelir = pd.DataFrame({"toplam_gelir": [1000, 1750]})

# Soru 10.1: Alt alta birleştirme (ignore_index=True indeksleri 0, 1, 2, 3 diye sıfırlar)
df_alt_alta = pd.concat([hafta1, hafta2], ignore_index=True)
print("--- Soru 10.1: Alt Alta Birleştirme ---")
print(df_alt_alta)

# Soru 10.2: Yan yana birleştirme (axis=1 sütun bazında yan yana ekler)
df_yan_yana = pd.concat([hafta1, gelir], axis=1)
print("\n--- Soru 10.2: Yan Yana Birleştirme ---")
print(df_yan_yana)

print("----------------------------------------")

"""
---## Bölüm 11 — GroupByAşağıdaki veriyi kullanın:
df_calisan = pd.DataFrame({    "sube": ["Kadıköy", "Beşiktaş", "Kadıköy", "Şişli", "Beşiktaş"],    "ad": ["Baran", "Ceylin", "Emre", "Fulya", "Gökhan"],    "satis": [12000, 18500, 9500, 21000, 16000]})
Soru 11.1: Şubeye göre toplam satışı bulun.Soru 11.2: Şubeye göre ortalama satışı bulun.Soru 11.3: .agg(["sum","mean","count"]) kullanarak şube başına üç istatistiği aynı anda hesaplayın.
"""

df_calisan = pd.DataFrame({
    "sube": ["Kadıköy", "Beşiktaş", "Kadıköy", "Şişli", "Beşiktaş"],
    "ad": ["Baran", "Ceylin", "Emre", "Fulya", "Gökhan"],
    "satis": [12000, 18500, 9500, 21000, 16000],
})

# Soru 11.1: Şubeye göre toplam satış (.sum())
toplam_satis = df_calisan.groupby("sube")["satis"].sum()
print("--- Soru 11.1: Şubeye Göre Toplam Satış ---")
print(toplam_satis)

# Soru 11.2: Şubeye göre ortalama satış (.mean())
ortalama_satis = df_calisan.groupby("sube")["satis"].mean()
print("\n--- Soru 11.2: Şubeye Göre Ortalama Satış ---")
print(ortalama_satis)

# Soru 11.3: .agg() ile toplam, ortalama ve kişi sayısını tek seferde hesaplama
istatistikler = df_calisan.groupby("sube")["satis"].agg(["sum", "mean", "count"])
print("\n--- Soru 11.3: Çoklu İstatistik (.agg) ---")
print(istatistikler)

print("----------------------------------------")

"""
---## Bölüm 12 — Pivot TableAşağıdaki veriyi kullanın:

df_satis = pd.DataFrame({    "sehir": ["Bursa", "Adana", "Antalya", "Bursa", "Adana"],    "kategori": ["Elektronik", "Giyim", "Elektronik", "Giyim", "Elektronik"],    "satis": [5000, 3200, 4100, 2800, 3900]})

Soru 12.1: index="sehir", columns="kategori", values="satis" ile bir pivot tablo oluşturun.Soru 12.2: Aynı pivot tabloyu aggfunc="sum" ve fill_value=0 parametreleriyle oluşturup eksik hücrelerin nasıl doldurulduğunu gözlemleyin.
"""

# Verinin oluşturulması
df_satis = pd.DataFrame({
    "sehir": ["Bursa", "Adana", "Antalya", "Bursa", "Adana"],
    "kategori": ["Elektronik", "Giyim", "Elektronik", "Giyim", "Elektronik"],
    "satis": [5000, 3200, 4100, 2800, 3900],
})

# Soru 12.1: Temel pivot tablo (varsayılan olarak ortalama/mean hesaplar)
pivot1 = df_satis.pivot_table(
    index="sehir", columns="kategori", values="satis"
)
print("--- Soru 12.1: Temel Pivot Tablo ---")
print(pivot1)

# Soru 12.2: aggfunc='sum' ile toplam alma ve fill_value=0 ile boş yerleri 0 yapma
pivot2 = df_satis.pivot_table(
    index="sehir",
    columns="kategori",
    values="satis",
    aggfunc="sum",
    fill_value=0,
)
print("\n--- Soru 12.2: Toplamlı ve Sıfır Dolgulu Pivot Tablo ---")
print(pivot2)

print("----------------------------------------")

"""
---## Bölüm 13 — Apply ile String İşlemleriSoru 13.1: df_kullanici = pd.DataFrame({"kullanici_adi": ["baran23", "CEYLIN_K", "emre.y"]}) oluşturun.Soru 13.2: apply(str.lower) kullanarak tüm kullanıcı adlarını küçük harfe çeviren bir kullanici_adi_kucuk sütunu ekleyin.Soru 13.3: apply ve lambda ile kullanıcı adının kaç karakter olduğunu gösteren bir karakter_sayisi sütunu ekleyin.
"""

# Soru 13.1: DataFrame'in oluşturulması
df_kullanici = pd.DataFrame(
    {"kullanici_adi": ["baran23", "CEYLIN_K", "emre.y"]}
)
print("--- Başlangıç Tablosu ---")
print(df_kullanici)

# Soru 13.2: str.lower ile tüm harfleri küçültme
df_kullanici["kullanici_adi_kucuk"] = df_kullanici["kullanici_adi"].apply(
    str.lower
)

# Soru 13.3: lambda ve len() ile karakter sayısını hesaplama
df_kullanici["karakter_sayisi"] = df_kullanici["kullanici_adi"].apply(
    lambda x: len(x)
)

print("\n--- Soru 13.2 ve 13.3 Sonucu ---")
print(df_kullanici)

print("----------------------------------------")

"""
---## Bölüm 14 — Veri Tipi Dönüşümü (astype)Soru 14.1: df_urun = pd.DataFrame({"urun_id":["10","11","12"], "agirlik_kg":["1.5","0.75","3.2"]}) oluşturun.Soru 14.2: .info() ile sütunların object (metin) tipinde olduğunu doğrulayın.Soru 14.3: urun_id sütununu int, agirlik_kg sütununu float tipine dönüştürüp tekrar .info() ile kontrol edin.
"""

# Soru 14.1: Metin (string) sayılardan oluşan DataFrame'i oluşturma
df_urun = pd.DataFrame(
    {"urun_id": ["10", "11", "12"], "agirlik_kg": ["1.5", "0.75", "3.2"]}
)

# Soru 14.2: Tiplerin 'object' (metin) olduğunu doğrulama
print("--- Soru 14.2: Dönüşüm Öncesi Tipler ---")
df_urun.info()

# Soru 14.3: astype() ile tipleri dönüştürme ve tekrar kontrol etme
df_urun["urun_id"] = df_urun["urun_id"].astype(int)
df_urun["agirlik_kg"] = df_urun["agirlik_kg"].astype(float)

print("\n--- Soru 14.3: Dönüşüm Sonrası Tipler ---")
df_urun.info()

print("----------------------------------------")

"""
---## Bölüm 15 — Matplotlib ile Grafik ÇizmeAşağıdaki hücreyi çalıştırarak bir yıllık çeyreklik gelir verisi oluşturun:
df_gelir = pd.DataFrame({    "ceyrek": ["Ç1", "Ç2", "Ç3", "Ç4"],    "gelir": [42000, 55000, 48000, 61000],    "gider": [30000, 38000, 33000, 40000]})
Soru 15.1: gelir değerlerini kind="line" ile, üzerinde nokta işaretleri (marker="o") olacak şekilde çizgi grafikle çizin; başlık ve eksen etiketleri ekleyin.Soru 15.2: gelir değerlerini çeyreklere göre kind="bar" ile bar grafikle çizin (renk seçiminiz size ait).Soru 15.3: gelir sütununu çeyreklerin payını gösterecek şekilde kind="pie" ile pasta grafikle çizin (autopct="%1.1f%%" kullanın).Soru 15.4: gelir ve gider sütunlarını kind="scatter" ile scatter grafikte karşılaştırın (x ekseni gelir, y ekseni gider olsun) ve grafiğin ne anlattığını bir cümleyle yorumlayın.
"""

# Verinin oluşturulması
df_gelir = pd.DataFrame({
    "ceyrek": ["Ç1", "Ç2", "Ç3", "Ç4"],
    "gelir": [42000, 55000, 48000, 61000],
    "gider": [30000, 38000, 33000, 40000],
})

# Soru 15.1: Çizgi Grafiği (kind="line", marker="o")
df_gelir.plot(
    x="ceyrek",
    y="gelir",
    kind="line",
    marker="o",
    title="Çeyreklik Gelir Grafiği",
)
plt.xlabel("Çeyrekler")
plt.ylabel("Gelir (TL)")
plt.show()

# Soru 15.2: Bar (Sütun) Grafiği (kind="bar")
df_gelir.plot(
    x="ceyrek",
    y="gelir",
    kind="bar",
    color="steelblue",
    title="Çeyreklik Gelir Dağılımı",
)
plt.xlabel("Çeyrekler")
plt.ylabel("Gelir (TL)")
plt.show()

# Soru 15.3: Pasta Grafiği (kind="pie")
# Pasta grafiği dilim isimlerini index'ten aldığı için index'i 'ceyrek' yapıyoruz
df_gelir.set_index("ceyrek")["gelir"].plot(
    kind="pie", autopct="%1.1f%%", title="Çeyreklik Gelir Payları"
)
plt.ylabel("")  # Y eksenindeki fazlalık yazıyı temizler
plt.show()

# Soru 15.4: Scatter (Dağılım) Grafiği (kind="scatter")
df_gelir.plot(
    kind="scatter",
    x="gelir",
    y="gider",
    color="darkred",
    title="Gelir ve Gider Karşılaştırması",
)
plt.xlabel("Gelir (TL)")
plt.ylabel("Gider (TL)")
plt.show()


print("----------------------------------------")

"""
---## Bonus — Kapsamlı UygulamaBir online kursun satış verisini simüle edin:1. kurs_adi, kategori (örn. Yazılım, Tasarım, Pazarlama) ve satis_adedi sütunlarından oluşan, en az 8 satırlık bir DataFrame oluşturun.2. Kategoriye göre toplam satış adedini groupby ile bulun.3. En çok satan 3 kursu .sort_values() ile bulun.4. Kategori bazında toplam satışı gösteren bir bar grafik çizin.5. apply ile satış adedi 50 üzeri olanlara "Popüler", altındakilere "Standart" yazan yeni bir sütun ekleyin.
"""

# Adım 1: En az 8 satırlık kurs satış DataFrame'i oluşturma
veri = {
    "kurs_adi": [
        "Python Giriş",
        "Web Tasarım",
        "Dijital Pazarlama",
        "İleri Veri Analizi",
        "UI/UX Tasarım",
        "SEO Uzmanlığı",
        "Mobil Uygulama",
        "Sosyal Medya",
    ],
    "kategori": [
        "Yazılım",
        "Tasarım",
        "Pazarlama",
        "Yazılım",
        "Tasarım",
        "Pazarlama",
        "Yazılım",
        "Pazarlama",
    ],
    "satis_adedi": [85, 45, 60, 40, 30, 75, 95, 20],
}

df_kurs = pd.DataFrame(veri)
print("--- Kurs Tablosu ---")
print(df_kurs)

# Adım 2: Kategoriye göre toplam satış adedini bulma
kategori_toplam = df_kurs.groupby("kategori")["satis_adedi"].sum()
print("\n--- Kategoriye Göre Toplam Satış ---")
print(kategori_toplam)

# Adım 3: En çok satan 3 kursu bulma (büyükten küçüğe sıralayıp ilk 3'ü alma)
en_cok_satanlar = df_kurs.sort_values(by="satis_adedi", ascending=False).head(3)
print("\n--- En Çok Satan 3 Kurs ---")
print(en_cok_satanlar[["kurs_adi", "satis_adedi"]])

# Adım 4: Kategori bazında toplam satışı gösteren bar grafiği
kategori_toplam.plot(
    kind="bar", color="teal", title="Kategoriye Göre Toplam Satışlar"
)
plt.xlabel("Kategori")
plt.ylabel("Toplam Satış Adedi")
plt.show()

# Adım 5: apply ile 50 üzeri için 'Popüler', altı için 'Standart' sütunu ekleme
df_kurs["durum"] = df_kurs["satis_adedi"].apply(
    lambda x: "Popüler" if x >= 50 else "Standart"
)

print("\n--- Durum Sütunu Eklenmiş Son Hali ---")
print(df_kurs)

print("----------------------------------------")