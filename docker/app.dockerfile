FROM nginx:latest
MAINTAINER Daniel Prata
COPY . /var/application
WORKDIR /var/application
RUN apt update \
    && apt install -y python3.7 \
    && apt install -y python3-pip \
    && pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python3.7", "manage.py", "runserver", "0.0.0.0:8000"]