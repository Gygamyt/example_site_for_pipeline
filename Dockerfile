# Используйте официальный образ Python
FROM python:3.11

# Установите рабочую директорию
WORKDIR /app/src

# Скопируйте файлы зависимостей
COPY src/requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте все файлы проекта
COPY . .

# Соберите статические файлы
RUN cd src && python manage.py collectstatic --noinput

EXPOSE 8000

WORKDIR /app/src/src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
