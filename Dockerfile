# Python 3.11 tabanlı imaj kullan
FROM python:3.11-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Pip'i güncelle
RUN pip install --upgrade pip

# Gereklilikleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Uygulama için portları dinle
EXPOSE 8000

# Başlangıç komutu
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
