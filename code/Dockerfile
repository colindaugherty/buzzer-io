FROM ubuntu:latest
USER root
RUN apt-get update
RUN apt-get -y install curl gnupg python3-pip
RUN curl -sL https://deb.nodesource.com/setup_14.x  | bash -
RUN apt-get -y install nodejs
RUN mkdir /code
COPY ./requirements.txt /code/requirements.txt
WORKDIR /code
RUN npm update
RUN npm install -g @angular/cli
RUN npm install --save-dev @angular-devkit/build-angular
RUN npm install ngx-socket-io
RUN pip3 install -r requirements.txt
COPY . /code
WORKDIR /code/frontend/buzzer-io
RUN ng build --prod
WORKDIR /code
RUN rm -rf /code/backend/static
RUN bash -c 'ln /code/frontend/buzzer-io/dist /code/backend/static'
CMD ["python3", "server.py"]
EXPOSE 5000
