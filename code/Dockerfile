FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY  . .
WORKDIR /backend
CMD ["gunicorn",  "-k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 2 server:app"]