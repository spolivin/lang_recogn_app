FROM python:3.9-slim-bookworm

COPY ./app /code/app
COPY ./requirements/requirements-server.txt /code/requirements-server.txt

WORKDIR /code

RUN pip install --no-cache-dir --upgrade -r requirements-server.txt

ENV PYTHONPATH="$PYTHONPATH:/code/app"

EXPOSE 80

CMD ["uvicorn", "app.server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
