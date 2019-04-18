#docker build --no-cache -t comparator:latest .
docker build -t comparator:latest .
docker run -p 5000:5000/tcp comparator:latest
