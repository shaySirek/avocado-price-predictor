# Python base image
FROM python:3.7

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

RUN mkdir /.cache && chmod g+w /.cache .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]