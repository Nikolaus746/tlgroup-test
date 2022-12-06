# образ на основе которого создаём контейнер
FROM python:3.10-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# переменные окружения для python
#- Python не будет создавать файлы кэша .pyc;
ENV PYTHONDONTWRITEBYTECODE 1
# - не помещает в буфер потоки stdout и stderr.
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgresql
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
