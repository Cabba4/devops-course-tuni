FROM python:3.12-alpine

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Create vstorage file
RUN touch /vstorage

EXPOSE 8199

CMD ["python", "app.py"]
