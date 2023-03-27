# Этап, на котором выполняются подготовительные действия
FROM python:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY main.py

RUN mkdir -p /templates
COPY /templates/index.html /app/templates
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
CMD [ "python", "./main.py"]