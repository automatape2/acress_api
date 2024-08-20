FROM janicama/accress-base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY ./app/ /code/
COPY ./manage.py /code/
COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", "localhost:8000", "app.wsgi:application"]