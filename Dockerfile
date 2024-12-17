FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get install -y libpangoft2-1.0-0
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /app

RUN chmod +x ./boot.sh
ENV FLASK_APP main.py

CMD ["./boot.sh"]