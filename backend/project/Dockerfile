# Используем официальный Python-образ
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код проекта в контейнер
COPY . .

# Открываем порт (если нужно)
EXPOSE 8000

# Запускаем сервер Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CoreRoot.wsgi:application"]


