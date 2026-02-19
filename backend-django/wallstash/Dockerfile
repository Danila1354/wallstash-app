FROM python:3.11-alpine

WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "wallstash.wsgi:application", "--bind", "0.0.0.0:8000"]