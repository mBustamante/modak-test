FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Adds our application code to the image
RUN mkdir -p /code/
WORKDIR code

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install pip-tools && pip-sync requirements.txt

COPY ./ code/

ENV PORT=8000
EXPOSE $PORT

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000