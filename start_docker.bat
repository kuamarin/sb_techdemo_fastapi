docker build -t sber_demo .
docker network create my-net
docker run -p 8000:80 sber_demo