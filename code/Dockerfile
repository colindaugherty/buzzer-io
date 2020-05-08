FROM ubuntu:latest
USER root
RUN apt-get update
RUN apt-get -y install curl gnupg python3-pip
RUN curl -sL https://deb.nodesource.com/setup_14.x  | bash -
RUN apt-get -y install nodejs
RUN mkdir /code
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN npm install -g @angular/cli
RUN pip3 install -r requirements.txt
COPY . /code
WORKDIR /code/frontend/buzzer-io
RUN npm update
RUN npm install
RUN ng build --prod
WORKDIR /code
CMD ["python3", "backend/server.py"]
EXPOSE 5000
