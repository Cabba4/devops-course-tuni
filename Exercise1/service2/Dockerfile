# Use official Golang image
FROM golang:1.21

WORKDIR /app

COPY main.go .

RUN go build -o service2 main.go

# Create vstorage file
RUN touch /vstorage

CMD ["./service2"]
