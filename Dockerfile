# Базовый образ с Python
FROM python:3.12

# Установим переменную окружения для корректного взаимодействия с Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установим рабочую директорию
WORKDIR /marketplace

# Скопируем requirements.txt и установим зависимости
COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel cython
RUN apt-get update
RUN pip install -r requirements.txt

# Устанавливаем зависимости для сборки
RUN apt-get update && apt-get install -y \
    libyaml-dev \
    build-essential \
    python3-dev

# Скопируем остальные файлы проекта
COPY . .


# Открываем порт 8000
EXPOSE 8000

# Команда по умолчанию для запуска приложения
CMD ["sh", "-c", "python marketplace/manage.py migrate && python marketplace/manage.py runserver 0.0.0.0:8000"]

