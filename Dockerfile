# Используйте базовый образ Python
FROM python:3.8

# Установите переменную окружения для управления выводом
ENV PYTHONUNBUFFERED 1

# Создайте директорию для кода проекта внутри контейнера
RUN mkdir /app
WORKDIR /app

# Копируйте зависимости и установите их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копируйте код вашего проекта внутрь контейнера
COPY . /app/

# Установите Gunicorn (или другой WSGI-сервер)
RUN pip install gunicorn

# Запустите Gunicorn при запуске контейнера
CMD ["gunicorn", "krypta.wsgi:application", "--bind", "0.0.0.0:8000"]
