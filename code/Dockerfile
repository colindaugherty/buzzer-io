FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY  . .
WORKDIR /backend
CMD ["gunicorn",  "--worker-class", "eventlet", "-w", "2", "-b", "0.0.0.0:5000", "server:app"]