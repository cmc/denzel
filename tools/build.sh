#docker build --no-cache -t comparator:latest .
docker build -t denzel:latest .
docker run -p 5000:5000/tcp denzel:latest
