docker-machine start default
docker-machine env default | Invoke-Expression
docker-compose build
docker-compose up
