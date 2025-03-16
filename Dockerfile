# Wybór oficjalnego obrazu Python z obsługą pakietów systemowych
FROM python:3.10

# Ustawienie katalogu roboczego
WORKDIR /app

# Instalacja pakietów systemowych wymaganych dla SQLite3 i innych zależności
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Skopiowanie plików aplikacji do obrazu Dockera
COPY . /app

# Instalacja wymaganych bibliotek Pythona
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Ustawienie domyślnej komendy uruchamiającej bota
CMD ["python", "vacation_price_bot.py"]
