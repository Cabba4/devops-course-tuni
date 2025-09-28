## Setup

Podman has been used instead of docker while working on this assignment, however that should not effect anything

podman-compose is same as docker-compose

### Build images
```
podman-compose build
```
### Run project
```
podman-compose up -d
```
### Cleanup
```
podman-compose down
podman image prune -a # Removes ALL images
```
### vStorage and storage container cleanup
```
echo "" > vstorage
echo "" > internal-storage/log.txt
```
or run the cleanup script
```
./cleanup.sh
```