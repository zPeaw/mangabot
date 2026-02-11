

# Discord Manga Bildirim Botu

Bu proje, belirlenen bir web sitesini otomatik olarak izleyen ve yeni eklenen
içerikleri bir Discord kullanıcısına özel mesaj (DM) olarak gönderen bir
bildirim sistemidir.

Amaç; minimum insan müdahalesi ile, güvenilir ve tekrar etmeyen bir
takip mekanizması sağlamaktır.

Bot uzun süre çalışmaya uygun, basit ama genişletilebilir bir mimariye sahiptir.

---

## İçindekiler

- Proje Amacı
- Özellikler
- Sistem Mimarisi
- Çalışma Akışı
- Dosya Yapısı
- Gereksinimler
- Kurulum
- Ortam Değişkenleri
- Yapılandırma
- Çalıştırma
- Veri Yönetimi
- Zamanlayıcı Mantığı
- Güvenlik
- Performans Tavsiyeleri
- Yaygın Hatalar ve Çözümleri
- Hosting / Sunucu Kurulumu
- Ölçeklendirme
- Geliştirme Yol Haritası

---

## Proje Amacı

Yeni içerikleri manuel kontrol etmek yerine bu süreci otomatikleştirmek.

Sistem:

- siteyi izler  
- değişiklikleri tespit eder  
- kullanıcıyı bilgilendirir  
- geçmişi saklar  

ve tüm bunları sürekli çalışabilecek şekilde yapar.

---

## Özellikler

✔ Otomatik web sitesi tarama  
✔ Yeni içerik tespiti  
✔ Tekrar gönderimi engelleme  
✔ Discord DM gönderimi  
✔ JSON ile veri kalıcılığı  
✔ Headless (görünmez) tarayıcı  
✔ Arka planda uzun süre çalışma  
✔ Basit kurulum  
✔ Kolay genişletilebilir yapı  

---

## Sistem Mimarisi

Proje üç ana parçadan oluşur:

### 1) Discord Katmanı
Mesaj gönderimi ve zamanlayıcıyı yönetir.

### 2) Scraper Katmanı
Web sitesinden veriyi çeker ve düzenler.

### 3) Veri Katmanı
Geçmişi tutar ve karşılaştırma yapmayı sağlar.

---

## Çalışma Akışı

Her kontrol döngüsünde:

1. Site açılır.  
2. Güncel liste çıkarılır.  
3. `known.json` ile karşılaştırılır.  
4. Yeni olanlar belirlenir.  
5. Discord üzerinden gönderilir.  
6. Yeni liste kaydedilir.  

---



---

## Gereksinimler

- Python 3.9+
- Google Chrome veya Chromium
- İnternet bağlantısı

---

## Kurulum

### Depoyu indir

git clone <repo>
cd manga-bot

git clone <repo>
cd manga-bot

### Bağımlılıkları yükle

pip install -r requirements.txt


### DISCORD_TOKEN
Bot hesabının gizli anahtarıdır.

### USER_ID
Mesaj gönderilecek Discord kullanıcısı.

---

## Yapılandırma

`config.py` dosyasından değiştirilebilir:

- kontrol sıklığı  
- temizlik süresi  
- hedef site  
- veri dosyaları  

### Örnek – Günde 1 kez:


---

## Çalıştırma


Bot başlatıldığında:

- hemen kontrol yapar  
- sonra belirlenen süreyi bekler  
- döngü sonsuza kadar devam eder  

---

## Veri Yönetimi

### known.json
Daha önce işlenen içerikleri tutar.  
Bu dosya sayesinde tekrar gönderim olmaz.

### sent_messages.json
Mesajların zaman bilgisini tutar.  
Otomatik silme sistemlerinde kullanılır.

---

## Zamanlayıcı Mantığı

Bot `discord.ext.tasks.loop` kullanır.

Avantajları:

- basit  
- güvenilir  
- async uyumlu  
- uzun süreli çalışmaya uygun  

---

## Güvenlik

**En kritik nokta budur.**

`.env` dosyasını paylaşma.  
GitHub’a yükleme.

Token çalınırsa biri:

- botu kontrol edebilir  
- spam atabilir  
- sunuculara zarar verebilir  

Token sızdıysa hemen yenisini üret.

### Önerilen `.gitignore`

---

## Performans Tavsiyeleri

Site nadir güncelleniyorsa sık kontrol etmek mantıksızdır.

Günlük kullanım için:


Bu:

- sistemi yormaz  
- ban riskini azaltır  
- daha stabildir  

---

## Yaygın Hatalar ve Çözümleri

### Bot mesaj atmıyor
- USER_ID yanlış olabilir  
- kullanıcı DM kapalı olabilir  
- token hatalı olabilir  

### Chrome hatası
Tarayıcı kurulu olmayabilir.

### Hep aynı mesaj geliyor
`known.json` silinmiş olabilir.

---

## Hosting / Sunucu Kurulumu

Uygun ortamlar:

- VPS  
- ev sunucusu  
- Docker  
- bulut servisleri  

Sürekli çalışacağı için ekran açık kalmak zorunda değildir.

---

## Ölçeklendirme

Projeyi büyütmek için:

- çoklu kullanıcı  
- rol bazlı gönderim  
- farklı siteler  
- merkezi veritabanı  
- API sistemi  

eklenebilir.

---

## Geliştirme Yol Haritası

Planlanabilecek ileri seviye özellikler:

- Discord komutları  
- embed tasarımı  
- gelişmiş log sistemi  
- hata bildirimleri  
- web panel  
- otomatik güncelleme  
- cache mekanizması  

---

## Sonuç

Bu bot basit ama sağlam bir bildirim altyapısı sunar.
Az bakım ister, sürekli çalışır ve kolayca genişletilebilir.

---

## Dosya Yapısı

