FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python","manage.py","runserver","8000"]
CMD ["celery","-A", "OCR.celery","worker","--loglevel=info"]
