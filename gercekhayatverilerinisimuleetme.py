import numpy as np
import matplotlib.pyplot as plt

# BÖLÜM 1: Şirket Maaş Analizi

# Görev 1: Maaşları simüle etme ve analiz
np.random.seed(42)  # Rastgelelik için seed belirleme
maaslar = np.random.randint(3000, 15001, size=500)  # 3000-15000 TL arası 500 maaş

ortalama_maas = np.mean(maaslar)
max_maas = np.max(maaslar)
min_maas = np.min(maaslar)

print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
print(f"Maksimum Maaş: {max_maas} TL")
print(f"Minimum Maaş: {min_maas} TL")

# Maaş dağılımını histogram ile görselleştirme
plt.hist(maaslar, bins=20, edgecolor='black')
plt.title('Maaş Dağılımı')
plt.xlabel('Maaş (TL)')
plt.ylabel('Çalışan Sayısı')
plt.show()

# Görev 2: Departmanlara atama ve ortalama maaş hesaplama
departmanlar = np.random.choice([1, 2, 3], size=500)  # 1: Mühendislik, 2: Muhasebe, 3: Pazarlama

muhendislik_maas = maaslar[departmanlar == 1]
muhasebe_maas = maaslar[departmanlar == 2]
pazarlama_maas = maaslar[departmanlar == 3]

print(f"Mühendislik Ortalama Maaş: {np.mean(muhendislik_maas):.2f} TL")
print(f"Muhasebe Ortalama Maaş: {np.mean(muhasebe_maas):.2f} TL")
print(f"Pazarlama Ortalama Maaş: {np.mean(pazarlama_maas):.2f} TL")

# BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz

# Görev 3: Sıcaklık verilerini simüle etme ve analiz
sicakliklar = np.random.randint(-10, 41, size=365)  # -10°C ile 40°C arası 365 günlük sıcaklık

ortalama_sicaklik = np.mean(sicakliklar)
en_sicak_gun = np.argmax(sicakliklar) + 1  # Gün indeksi 0'dan başlar, bu yüzden +1
en_soguk_gun = np.argmin(sicakliklar) + 1

print(f"Ortalama Sıcaklık: {ortalama_sicaklik:.2f}°C")
print(f"En Sıcak Gün: {en_sicak_gun}. Gün")
print(f"En Soğuk Gün: {en_soguk_gun}. Gün")

# Sıcaklık değişimlerini çizgi grafiği ile gösterme
plt.plot(range(1, 366), sicakliklar)
plt.title('Yıllık Sıcaklık Değişimi')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.show()

# BÖLÜM 3: Ürün Satış Analizi

# Görev 4: Ürün satışlarını simüle etme ve analiz
urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
satislar = np.random.randint(10, 101, size=(5, 30))  # 5 ürün için 30 günlük satış

toplam_satislar = np.sum(satislar, axis=1)
ortalama_satislar = np.mean(satislar, axis=1)

for i, urun in enumerate(urunler):
    print(f"{urun} Toplam Satış: {toplam_satislar[i]}")
    print(f"{urun} Ortalama Satış: {ortalama_satislar[i]:.2f}")

# Ürün bazında çubuk grafiği çizme
plt.bar(urunler, toplam_satislar)
plt.title('Ürün Bazında Toplam Satışlar')
plt.xlabel('Ürün')
plt.ylabel('Toplam Satış Miktarı')
plt.show()
