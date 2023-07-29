STEPS TO FOLLOW.

1. Download zip file and Extract in your system.

2. cd OCR/

3. Create the virtualenv
! pip install virtualenv
! virtualenv env_name
! env_name\Scripts\activate   # to activate virtualenv

4. Install all the required packages
! pip install -r requirements.txt

5. Install RabbitMQ in your system from following link and It is highly recommended that RabbitMQ is also installed as an administrative account. and along with rabbitMQ Erlang must be installed using an administrative account.

https://www.rabbitmq.com/download.html

6. To create tables into database execute following two lines already added into Dockerfile.
python manage.py makemigrations
python manage.py migrate

7. Start the python server using following command
!python manage.py runserver 8000

8. Start the celery server using following command
celery -A OCR.celery worker --loglevel=info

9. Start the RabbitMQ server using following command.
cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.12.2\sbin  #### Your system path.
rabbitmq-server start.

10. Use Docker-compose.yml file to start docker container in your system.

11. Use postman collection to trigger the request and get the result.
http://localhost:8000/api/v1/OCRExtraction  ## Extract all the information from pdf.
http://localhost:8000/api/v1/StoreIntoDB    ## Store Extracted Json output into database.

! POST req and select file
