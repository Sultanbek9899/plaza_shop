FROM python:3.8.6-alpine3.12
LABEL maintainer="Sultanbek Beksultanov <sultanbek9899@gmail.com>"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN apk add --no-cache gcc postgresql-dev \
    linux-headers musl-dev libffi-dev \
    libxml2-dev libxslt-dev imagemagick-dev \
    zlib-dev py3-magic  make \
    && rm -rf /var/apt/list/*
WORKDIR /app

COPY requirements ./requirements/

RUN pip install --upgrade pip && pip install -r requirements/development.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "./dockerfiles/app/docker-entrypoint.sh"]

