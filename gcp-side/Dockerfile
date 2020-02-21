# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app


# create and install local package
WORKDIR /app/pkg/gps_utils
RUN pip install -r requirements.txt
RUN python setup.py bdist_wheel
RUN pip install dist/*

WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]