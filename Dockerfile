FROM python:3.7-alpine

RUN pip3 --no-cache-dir install --upgrade \
    pip==19.3.1 \
    pipenv==2018.11.26

COPY Pipfile* /

RUN pipenv install --system --deploy

COPY count.py .
COPY .env .

CMD ["python", "count.py"]
