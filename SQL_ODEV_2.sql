PRAGMA foreign_keys = ON;

CREATE TABLE uyeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    yas INTEGER CHECK (yas > 13),
    sehir TEXT DEFAULT 'Erzincan',
    kayit TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE kitaplar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL UNIQUE
);

CREATE TABLE odunc (
    uye_id INTEGER,
    kitap_id INTEGER,
    PRIMARY KEY (uye_id, kitap_id),
    FOREIGN KEY (uye_id) REFERENCES uyeler(id) ON DELETE CASCADE,
    FOREIGN KEY (kitap_id) REFERENCES kitaplar(id)
);

INSERT INTO kitaplar (ad) VALUES
('Suç ve Ceza'),
('Kürk Mantolu Madonna'),
('Sefiller'),
('1984'),
('Simyacı');

INSERT INTO uyeler (ad, yas, sehir) VALUES
('Ali', 20, 'İstanbul'),
('Berkay', 22, 'Ankara'),
('Tuğra', 19, 'Giresun'),
('Mehmet', 25, 'Bursa'),
('Ayşe', 21, 'İzmir');

INSERT INTO uyeler (ad, yas) VALUES
('Zeynep', 23),
('Elif', 18),
('Can', 27),
('Mert', 20),
('Deniz', 24);

SELECT * FROM uyeler;

INSERT INTO uyeler (ad, yas, sehir) VALUES ('Meva', 8, 'İstanbul'); --Sonuç: CHECK constraint failed: yas > 13  

SELECT * FROM odunc;

INSERT INTO odunc (uye_id, kitap_id) VALUES (99, 1); -- Sonuç: FOREIGN KEY constraint failed

ALTER TABLE odunc ADD COLUMN gun  CURRENT_TIMESTAMP;
 
INSERT INTO odunc (uye_id, kitap_id, gun) VALUES
(1, 1, 5),
(1, 2, 12),

(2, 2, 7),
(2, 3, 20),

(3, 3, 10),
(3, 4, 25),

(4, 4, 15),
(4, 5, 30),

(5, 5, 8),
(5, 1, 18),

(6, 1, 22),
(6, 2, 35),

(7, 2, 14),
(7, 3, 40),

(8, 3, 6),
(8, 4, 28),

(9, 4, 16),
(9, 5, 45),

(10, 5, 9),
(10, 1, 32);

SELECT u.ad AS uye, k.ad AS kitap, o.gun
FROM odunc o
JOIN uyeler u ON u.id = o.uye_id
JOIN kitaplar k ON k.id = o.kitap_id;

SELECT u.ad AS uye, k.ad AS kitap, o.gun
FROM odunc o
JOIN uyeler u ON u.id = o.uye_id
JOIN kitaplar k ON k.id = o.kitap_id
WHERE o.gun > 30;

SELECT u.ad AS uye, k.ad AS kitap, o.gun
FROM odunc o
JOIN uyeler u ON u.id = o.uye_id
JOIN kitaplar k ON k.id = o.kitap_id
WHERE u.sehir = 'Erzincan';

--kitap almayanlar
SELECT u.ad AS uye, k.ad AS kitap, o.gun
FROM uyeler u
LEFT JOIN odunc o ON u.id = o.uye_id
LEFT JOIN kitaplar k ON k.id = o.kitap_id;

--Where gruplandırmadan önce çalıştşığı için having kullandık böylelikle ilk ortalamayı aldı
SELECT 
    u.ad AS uye,
    AVG(o.gun) AS ortalama_gun,
    COUNT(o.kitap_id) AS kitap_sayisi,
    MAX(o.gun) AS en_uzun_gun
FROM uyeler u
JOIN odunc o ON u.id = o.uye_id
GROUP BY u.id, u.ad
HAVING AVG(o.gun) > 20;

SELECT k.ad AS kitap, COUNT(o.kitap_id) AS odunc_sayisi
FROM kitaplar k
LEFT JOIN odunc o ON k.id = o.kitap_id
GROUP BY k.id, k.ad;

SELECT sehir, COUNT(*) AS uye_sayisi
FROM uyeler
GROUP BY sehir
ORDER BY uye_sayisi DESC;

--Subquery ile birlikte 30 günden fazla kitap tutmuş kullanıcı isimlerini listeledik
SELECT ad
FROM uyeler
WHERE id IN (
    SELECT uye_id
    FROM odunc
    WHERE gun > 30
);

SELECT ad
FROM kitaplar
WHERE id NOT IN (
    SELECT kitap_id
    FROM odunc
);

SELECT *
FROM odunc
WHERE gun > (
    SELECT AVG(gun)
    FROM odunc
);

SELECT 
    o.uye_id,
    o.kitap_id,
    o.gun,
    CASE
        WHEN o.gun > 30 THEN 'Gecikmiş'
        WHEN o.gun BETWEEN 15 AND 30 THEN 'Uyarı'
        ELSE 'Normal'
    END AS durum
FROM odunc o;

SELECT 
    ad,
    yas,
    CASE
        WHEN yas <= 18 THEN 'Genç'
        ELSE 'Yetişkin'
    END AS yas_grubu
FROM uyeler;

SELECT 
    CASE
        WHEN gun > 30 THEN 'Gecikmiş'
        WHEN gun BETWEEN 15 AND 30 THEN 'Uyarı'
        ELSE 'Normal'
    END AS durum,
    COUNT(*) AS kayit_sayisi
FROM odunc
GROUP BY 
    CASE
        WHEN gun > 30 THEN 'Gecikmiş'
        WHEN gun BETWEEN 15 AND 30 THEN 'Uyarı'
        ELSE 'Normal'
    END;
	
CREATE INDEX idx_uyeler_ad
ON uyeler(ad);

SELECT * FROM uyeler
WHERE ad LIKE 'Ali%';

ALTER TABLE uyeler
ADD COLUMN eposta TEXT;

CREATE UNIQUE INDEX idx_uyeler_eposta
ON uyeler(eposta);

UPDATE uyeler
SET eposta = 'tugradagdelen@gmail.com'
WHERE id = 1;

UPDATE uyeler
SET eposta = 'tugradagdelen@gmail.com' 
WHERE id = 2;