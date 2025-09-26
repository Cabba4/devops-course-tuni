# Use official Golang image
FROM golang:1.21

WORKDIR /app

# Copy source
COPY main.go .

# Build binary
RUN go build -o service2 main.go

# Create vstorage directory
RUN touch /vstorage

# Expose port
EXPOSE 8201

# Run binary
CMD ["./service2"]
