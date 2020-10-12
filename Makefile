up:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

restart:
	@make down
	@make up

destroy:
	docker-compose down --rmi all --volumes

destroy-volumes:
	docker-compose down --volumes

ps:
	docker-compose ps

python:
	docker-compose exec python bash