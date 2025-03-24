FROM python:3.12

WORKDIR /app

COPY backend/project/requirements.txt .

# Устанавливаем netcat
RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/project/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY backend/project /app/

CMD ["/app/entrypoint.sh"]
