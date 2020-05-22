FROM python:3.8-slim-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# copy secret files into logic folder explicitally!
COPY ./secret.json /usr/src/app/swagger_server/logic/secret.json
#COPY ./key.json /usr/src/app/swagger_server/logic/key.json

# this is required to make stackdriver logs work properly
ENV PYTHONUNBUFFERED True

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]