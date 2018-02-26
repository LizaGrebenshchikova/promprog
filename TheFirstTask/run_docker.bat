docker-machine create --driver virtualbox dockervm
docker-machine start dockervm
@FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i
docker-compose build
docker-compose up -d db rabbit
sleep(10)
docker-compose up -d server
sleep(10)
docker-compose up client