build:
	docker build -t sparkgeo/django-oauth-service:dj_oauth -f Dockerfile --no-cache .
start:
	docker-compose up -d
stop:
	docker-compose down
shell:
	docker exec -it dj_oauth bash
kill:
	docker-compose kill
	docker-compose rm -f
migrate:
	docker exec -it dj_oauth ./manage.py migrate

freshbuild:
	make kill
	make build
	make start
	make migrate
