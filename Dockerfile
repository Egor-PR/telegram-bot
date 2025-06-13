FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей, минимально
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    gcc \
    libffi-dev \
    libssl-dev \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# Копируем исходники бота
COPY . .

# Команда запуска
CMD ["python3", "bot.py"]
