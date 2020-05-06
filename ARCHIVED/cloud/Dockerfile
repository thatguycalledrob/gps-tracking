# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Below currently not required
# create and install local package
COPY ./pkg /app/pkg
WORKDIR /app/pkg
RUN pip install -r requirements.txt
RUN python setup.py bdist_wheel
RUN pip install dist/*

# copy secrets and imports into container
COPY requirements.txt /app
COPY key.json /app
COPY secret.txt /app
COPY app.py /app

# run the server app!
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]