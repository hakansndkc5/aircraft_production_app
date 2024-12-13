# Uçak Üretim Yönetim Sistemi

Bu proje, uçak parçalarını yönetmek, üretim süreçlerini kontrol etmek ve ekip iş birliğini kolaylaştırmak için geliştirilmiş bir uçak üretim yönetim sistemidir. Django framework'ü ve Tailwind CSS kullanılarak modern ve kullanıcı dostu bir yapı sunulmuştur.

## Kurulum

### Gereksinimler
- Python 3.11+
- Docker
- PostgreSQL

### Kurulum Adımları
1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/hakansndkc5/aircraft_production_app.git
   cd aircraft_production_app
   ```

2. **Docker konteynerlerini başlatın:**
   ```bash
   docker-compose up --build
   ```

3. **Django uygulamasını yeniden başlatın:**
   Docker konteynerleri build edildikten sonra `django_app` konteynerını bir kez yeniden başlatmanız gerekmektedir.

4. **Projeye erişim:**
   Tarayıcınızda [http://127.0.0.1:8000](http://127.0.0.1:8000) adresini açın.

---

Projenin ekran görüntüleri **Screenshots** adlı dosyadadır. Buna ek olarak projenin çalıştırılan bir videosu da aşağıdaki google drive linkine eklenmiştir:
https://drive.google.com/drive/folders/1paqjZvB8oOQdgDXjWcyW3OAebno-C9A7?usp=share_link


## Kullanılan Teknolojiler
- **Backend:** Django Framework
- **Frontend:** Tailwind CSS
- **Veritabanı:** PostgreSQL
- **Containerization:** Docker
- **Testler:** Unit testler ile doğrulama


Bazı görüntüler:

<img width="1507" alt="Screenshot 2024-12-13 at 08 05 30" src="https://github.com/user-attachments/assets/445bb1d3-37ca-4168-9e8a-fe3e2032fbb4" />

![image](https://github.com/user-attachments/assets/c008ef75-c5b0-41dc-97dd-c0544e653f55)

![image](https://github.com/user-attachments/assets/d3335ff4-67a2-4e01-b12c-df9a711be8fe)




