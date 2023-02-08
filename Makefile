install:
	docker-compose build
	docker-compose up -d

install-prod:
	docker-compose -f docker-compose-prod.yml build
	docker-compose -f docker-compose-prod.yml up -d

clean-install:
	docker-compose down --remove-orphans --volumes
	docker-compose build --no-cache --pull --force-rm
	docker-compose up -d

clean-install-prod:
	docker-compose -f docker-compose-prod.yml down --remove-orphans --volumes
	docker-compose -f docker-compose-prod.yml build --no-cache --pull --force-rm
	docker-compose -f docker-compose-prod.yml up -d

migrate:
	docker-compose exec web python manage.py migrate

migrate-prod:
	docker-compose -f docker-compose-prod.yml exec web python manage.py migrate

start:
	docker-compose up -d

start-prod:
	docker-compose -f docker-compose-prod.yml up -d

stop:
	docker-compose stop

stop-prod:
	docker-compose -f docker-compose-prod.yml stop