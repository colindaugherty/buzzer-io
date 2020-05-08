FROM ubuntu:latest
USER root
RUN apt-get update
RUN apt-get -y install curl gnupg python3-pip
RUN curl -sL https://deb.nodesource.com/setup_14.x  | bash -
RUN apt-get -y install nodejs
RUN mkdir /code
WORKDIR /code
RUN npm install -g @angular/cli
RUN npm install ngx-socket-io
ADD requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /code/frontend/buzzer-io
RUN ng build --prod
WORKDIR /code
RUN rm -rf ./backend/static
RUN bash -c 'ln ./frontend/buzzer-io/dist ./backend/static'
CMD ["python3", "server.py"]
EXPOSE 5000
