docker-machine create --driver virtualbox dockervm
docker-machine start dockervm
@FOR /f "tokens=*" %i IN ('docker-machine env') DO @%i
docker-compose build                
docker-compose up
REM connect with dockervm IP-address:8000/admin/core