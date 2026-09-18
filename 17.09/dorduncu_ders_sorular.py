

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


"""
Hazırlık ve Ortam Ayarları
Analiz için gerekli kütüphaneler (pandas, numpy, matplotlib, seaborn, scipy) nasıl içe aktarılır?
Grafiklerin görsel stili (tema, renk paleti, boyut) nasıl standart hale getirilir?
Sonuçların tekrarlanabilir olması için rastgelelik nasıl sabitlenir (random_state/seed)?
Pandas'ta tüm sütun/satırların ve ondalık sayıların okunabilir biçimde görüntülenmesi nasıl sağlanır?
"""
# Rastgelelik sabitleme
np.random.seed(42)

# Grafik stili
sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10, 6)

# Pandas görüntüleme ayarları
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 120)
pd.set_option("display.float_format", "{:.2f}".format)


"""
Örnek (Sentetik) Veri Setinin Oluşturulması
1000 müşteriden oluşan örnek bir veri seti (yaş, gelir, şehir, abonelik tipi, kayıt tarihi, aylık harcama, memnuniyet puanı, churn) nasıl üretilir?
Gerçek dünya verilerindeki tutarsızlıkları simüle etmek için şehir isimlerinde kasıtlı yazım farklılıkları (İstanbul/istanbul, Ankara/ANKARA) nasıl eklenir?
"""

# 1000 müşteri oluşturma
n = 1000

df = pd.DataFrame({
    "musteri_id": range(1, n + 1),

    "yas": np.random.randint(18, 65, n),

    "gelir": np.random.normal(30000, 10000, n).round(2),

    "sehir": np.random.choice(
        ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"],
        n
    ),

    "abonelik_tipi": np.random.choice(
        ["Aylık", "Yıllık", "Premium"],
        n
    ),

    "kayit_tarihi": pd.date_range(
        start="2022-01-01",
        periods=n,
        freq="D"
    ),

    "aylik_harcama": np.random.normal(
        1500, 500, n
    ).round(2),

    "memnuniyet_puani": np.random.randint(
        1, 11, n
    ),

    "churn": np.random.choice(
        [0, 1],
        n,
        p=[0.8, 0.2]
    )
})

# Gelir ve harcama negatif olmasın
df["gelir"] = df["gelir"].clip(lower=1000)
df["aylik_harcama"] = df["aylik_harcama"].clip(lower=100)

# Şehir isimlerinde kasıtlı yazım farklılıkları
df.loc[0:9, "sehir"] = "istanbul"
df.loc[10:19, "sehir"] = "ANKARA"
df.loc[20:29, "sehir"] = " İzmir "
df.loc[30:39, "sehir"] = "bursa"

df.head()



"""
Kasıtlı "Kirli Veri" Enjeksiyonu
Veri setine eksik değerler (gelir, yaş, memnuniyet puanı sütunlarında) nasıl eklenir?
Gelir sütununda aşırı uç değerler (outlier) nasıl oluşturulur?
Yaş sütununa mantıksız değerler (-5, 150 gibi) nasıl eklenir?
Veri setine kasıtlı olarak yinelenen (duplicate) satırlar nasıl eklenir?
"""


# Eksik değerler ekleme
df.loc[np.random.choice(df.index, 30, replace=False), "gelir"] = np.nan

df.loc[np.random.choice(df.index, 20, replace=False), "yas"] = np.nan

df.loc[
    np.random.choice(df.index, 25, replace=False),
    "memnuniyet_puani"
] = np.nan

# Gelir sütununda outlier oluşturma
df.loc[50, "gelir"] = 1000000
df.loc[51, "gelir"] = 1500000

# Yaş sütununa mantıksız değerler ekleme
df.loc[60, "yas"] = -5
df.loc[61, "yas"] = 150

# Duplicate satırlar ekleme
df = pd.concat(
    [df, df.iloc[[100, 200, 300]]],
    ignore_index=True
)

print("Kirli veri oluşturuldu.")
print(df.shape)



"""
Veri Setine Genel Bakış
Veri setinin kaç satır ve kaç sütundan oluştuğu nasıl kontrol edilir?
Sütunların veri tipleri ve dolu/boş hücre sayıları (.info()) nasıl incelenir?
Veri setinin ilk, son ve rastgele seçilmiş birkaç satırı nasıl görüntülenir?

"""


# Satır ve sütun sayısı
df.shape

# Veri tipleri ve eksik değerler
df.info()

# İlk 5 satır
df.head()

# Son 5 satır
df.tail()

# Rastgele 5 satır
df.sample(5, random_state=42)



"""
Eksik Değer Analizi
Her sütundaki eksik değer sayısı, benzersiz değer sayısı ve eksik değer yüzdesini gösteren bir özet tablo nasıl oluşturulur?
Eksik değerlerin veri setindeki dağılımı bir ısı haritası (heatmap) ile nasıl görselleştirilir?
"""


# Özet tablo oluşturma
eksik_ozet = pd.DataFrame({
    "eksik_deger_sayisi": df.isnull().sum(),
    "benzersiz_deger_sayisi": df.nunique(),
    "eksik_yuzdesi": (
        df.isnull().sum() / len(df) * 100
    ).round(2)
})

eksik_ozet

# Eksik değer ısı haritası
plt.figure(figsize=(12, 6))

sns.heatmap(
    df.isnull(),
    cbar=False,
    yticklabels=False,
    cmap="viridis"
)

plt.title("Eksik Değer Isı Haritası")
plt.show()



"""
Yinelenen Kayıtların Tespiti
Veri setinde kaç adet birebir aynı (duplicate) satır bulunduğu nasıl tespit edilir?

"""


# Duplicate satır sayısı
df.duplicated().sum()

# Duplicate satırları görüntüleme
df[df.duplicated()]



"""
Kategorik Veri Temizliği
"Şehir" sütunundaki tutarsız yazımların (büyük/küçük harf, baştaki/sondaki boşluklar) dağılımı nasıl görüntülenir?
Şehir isimleri küçük harfe çevrilip boşluklardan nasıl arındırılır?
"""

# Şehir isimlerinin mevcut dağılımı
df["sehir"].value_counts(dropna=False)

# Küçük harfe çevirme ve boşlukları temizleme
df["sehir"] = df["sehir"].str.lower().str.strip()

# Temizlenmiş şehir dağılımı
df["sehir"].value_counts()



"""
Mantık Dışı (Anomali) Değerlerin Tespiti
0'ın altında veya 100'ün üzerinde olan, gerçekçi olmayan yaş değerlerine sahip müşteriler nasıl bulunur?

"""


# 0'ın altında veya 100'ün üzerinde yaşlar
anomali_yas = df[
    (df["yas"] < 0) | (df["yas"] > 100)
]

anomali_yas



"""
Betimsel İstatistikler
Sayısal sütunların temel istatistiksel özeti (ortalama, medyan, std, min/max vb.) nasıl elde edilir?
Sayısal değişkenlerin çarpıklık (skewness) ve basıklık (kurtosis) değerleri nasıl hesaplanır?
"""


# Sayısal sütunların istatistik özeti
df.describe()

# Medyan
df.median(numeric_only=True)

# Çarpıklık (Skewness)
df.skew(numeric_only=True)

# Basıklık (Kurtosis)
df.kurtosis(numeric_only=True)

# Çarpıklık ve basıklık birlikte
istatistik_ozet = pd.DataFrame({
    "ortalama": df.mean(numeric_only=True),
    "medyan": df.median(numeric_only=True),
    "std": df.std(numeric_only=True),
    "min": df.min(numeric_only=True),
    "max": df.max(numeric_only=True),
    "skewness": df.skew(numeric_only=True),
    "kurtosis": df.kurtosis(numeric_only=True)
})

istatistik_ozet



"""
Dağılım Görselleştirmeleri
Sayısal değişkenlerin dağılımları histogram ve yoğunluk eğrisi (KDE) ile nasıl gösterilir?
Sayısal değişkenlerdeki aykırı değerler kutu grafiği (boxplot) ile nasıl görselleştirilir?

"""


# Histogram ve KDE — Gelir
plt.figure(figsize=(10, 6))

sns.histplot(
    df["gelir"].dropna(),
    kde=True,
    bins=30
)

plt.title("Gelir Dağılımı")
plt.xlabel("Gelir")
plt.ylabel("Frekans")
plt.show()

# Histogram ve KDE — Yaş
plt.figure(figsize=(10, 6))

sns.histplot(
    df["yas"].dropna(),
    kde=True,
    bins=20
)

plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Frekans")
plt.show()

# Boxplot — Gelir
plt.figure(figsize=(10, 5))

sns.boxplot(
    x=df["gelir"]
)

plt.title("Gelir Boxplot")
plt.show()

# Boxplot — Yaş
plt.figure(figsize=(10, 5))

sns.boxplot(
    x=df["yas"]
)

plt.title("Yaş Boxplot")
plt.show()

# Boxplot — Aylık harcama
plt.figure(figsize=(10, 5))

sns.boxplot(
    x=df["aylik_harcama"]
)

plt.title("Aylık Harcama Boxplot")
plt.show()


"""
Kategorik Değişken Analizi
Kategorik sütunların (şehir, abonelik tipi, memnuniyet puanı, churn) yüzdesel dağılımı nasıl hesaplanır?
"""


# Şehir yüzdesel dağılımı
df["sehir"].value_counts(normalize=True) * 100

# Abonelik tipi yüzdesel dağılımı
df["abonelik_tipi"].value_counts(normalize=True) * 100

# Memnuniyet puanı yüzdesel dağılımı
df["memnuniyet_puani"].value_counts(
    normalize=True
).sort_index() * 100

# Churn yüzdesel dağılımı
df["churn"].value_counts(normalize=True) * 100



"""
Korelasyon Analizi
Sayısal değişkenler arasındaki korelasyon matrisi nasıl hesaplanır?
Korelasyon matrisi bir ısı haritası ile nasıl görselleştirilir?
"""


# Sayısal sütunları seçme
sayisal_df = df.select_dtypes(
    include=np.number
)

# Korelasyon matrisi
korelasyon = sayisal_df.corr()

korelasyon

# Korelasyon ısı haritası
plt.figure(figsize=(12, 8))

sns.heatmap(
    korelasyon,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Korelasyon Matrisi")
plt.show()