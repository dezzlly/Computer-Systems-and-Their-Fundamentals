FROM python:3.11-slim

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо requirements.txt окремо, щоб не перебудовувати весь образ при зміні коду
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо решту проєкту
COPY . .

# Відкриваємо порт
EXPOSE 8000

# Запуск FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]