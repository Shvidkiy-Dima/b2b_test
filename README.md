# RUN
docker-compose up

# SWAGGER
http://localhost:8000/swagger/ 


# TESTS
docker exec -it <container_id> sh

poetry run python manage.py test apps

# RUFF
poetry run ruff check --config pyproject.toml --fix 

poetry run ruff format --config pyproject.toml
