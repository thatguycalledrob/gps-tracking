# Swagger generated server

## Overview


## Requirements
go 1.14

The following files in this directory:
```
1.   key.json     ->      this is your GCP project service account key
```

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/pi/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/pi/v1/swagger.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```