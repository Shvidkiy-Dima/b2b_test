FROM python:3.11-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./pyproject.toml ./poetry.lock /app/

# Install Python dependencies using Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the project code into the container at /app
COPY . /app

COPY ./contrib/dev/start.sh /start.sh
COPY ./contrib/check_conn.py /app/check_conn.py

RUN chmod +x /start.sh

ENTRYPOINT ["/start.sh"]

