#!/bin/sh

echo "DEBUG=${DEBUG}"
echo "Waiting for PostgreSQL to be ready..."

# Ждём, пока PostgreSQL станет доступным
while ! nc -z db 5432; do
  sleep 0.5
done

echo "PostgreSQL is ready!"

# Выполняем миграции (по желанию)
python manage.py migrate

# Запускаем сервер
if [ "$DEBUG" = "True" ]; then
  echo "Running development server..."
  python manage.py runserver 0.0.0.0:8000
else
  echo "Running Gunicorn..."
  gunicorn --bind 0.0.0.0:8000 CoreRoot.wsgi:application
fi
