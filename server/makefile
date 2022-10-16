venv:
	python3 -m venv .venv 

init-dev:
	pip install -r requirements/dev.txt

init-prd:
	pip install -r requirements/prd.txt

test:
	python src/manage.py test --verbosity 2

migrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

dev:
	python src/manage.py runserver

clean:
	rm -rf .pytest_cache
	find . -name "*.pyc" -delete
	find . -name ".pytest_cache" -delete
	find . -type d -name __pycache__ -delete