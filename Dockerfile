FROM python:3.8

COPY ./ovisbot/  /ovisbot/ovisbot/
COPY poetry.lock pyproject.toml logging.ini /ovisbot/

WORKDIR /ovisbot

RUN pip install poetry==1.1.4
RUN poetry install

CMD poetry run python -m ovisbot run