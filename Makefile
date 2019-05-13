compose:
	docker-compose down
	docker-compose build
	docker-compose up
clean:
	docker build --no-cache -t denzel:latest . 
	docker-compose up
