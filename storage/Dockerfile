FROM python:3.12-alpine

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /internal-storage

CMD ["python", "app.py"]
