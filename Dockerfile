FROM python:3.10

RUN pip install poetry

COPY poetry.lock pyproject.toml /

RUN poetry update && poetry install

COPY count.py .
COPY .env .

CMD ["poetry", "run", "python", "count.py"]
