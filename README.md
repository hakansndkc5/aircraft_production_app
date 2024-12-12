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

## Kullanılan Teknolojiler
- **Backend:** Django Framework
- **Frontend:** Tailwind CSS
- **Veritabanı:** PostgreSQL
- **Containerization:** Docker
- **Testler:** Unit testler ile kapsamlı doğrulama
