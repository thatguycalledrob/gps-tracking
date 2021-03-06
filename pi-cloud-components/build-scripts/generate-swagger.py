import os
import re
import sys
import time
from typing import List, TextIO

import docker
from docker.errors import ContainerError

from docker.types import Mount
from os import path

from requests import HTTPError

swagger_warning: List[str] = [
    '# WARNING: File autogenerated by swagger generator.',
    '#          All changes will be lost of regeneration.',
    '#          DO NOT EDIT THIS FILE.',
    '', '', ''
]


# the purpose here is to generate the swagger client and server stub.
def run_wrapper(_client: docker.DockerClient, image: str, command: List[str], **kwargs):
    """
    Please see ContainerCollection(Collection).run(...) for the meaninig
    of these arguments

    Args:
        :param _client: (DockerClient) An instance of the docker API client
        :param image: (str) Name of the docker image to run via the docker API
        :param command: (List[str]) command to execute on the docker image
    """
    try:
        i = 1
        while i < 5:
            try:
                log_out(_client.containers.run(image, command, **kwargs))
                break
            except HTTPError as e:
                print(f"HTTP error, likely from missing or invalid docker pipe. error: {str(e)}.")
                print(f"retry {i}/5")
                time.sleep(2)  # give windows some time to sort its IO out.

    except ContainerError as e:
        log_out(e.stderr, stream=sys.stderr)
        exit(1)


def log_out(msg: bytes, stream: TextIO = sys.stdout) -> None:
    """
    this is used to wrap a docker command.
    Here the logs are returned as bytes object, this is a utility function

    Args:
        :param msg: (bytes) A bytes string to be decoded and printed
        :param stream: (TextIOWrapper) Where to output the logs to
    """
    for line in msg.decode('utf-8').split('/n'):
        print(line, file=stream)


# run with a simple python3 .\generate-swagger.py
if __name__ == '__main__':
    client = docker.from_env()

    # this refers to the entire pi-cloud-components directory
    build_directory = Mount(type='bind', source=path.abspath('..'), target='/data')

    # pull latest image
    print(client.images.pull('swaggerapi/swagger-codegen-cli:latest', decode=True))

    # create the python flask server stub from the swagger
    run_wrapper(client, 'swaggerapi/swagger-codegen-cli',
                ['generate', '-i', '/data/pi-cloud-swagger.yaml', '-l', 'python-flask', '-o', '/data/process-gps-points'],
                mounts=[build_directory], remove=True,
                detach=False, stdout=True, stderr=True)

    # create the swagger server stub
    run_wrapper(client, 'swaggerapi/swagger-codegen-cli',
                ['generate', '-i', '/data/pi-cloud-swagger.yaml', '-l', 'python', '-o',
                 '/data/pi-installation/swaggerlib'],
                mounts=[build_directory], remove=True,
                detach=False, stdout=True, stderr=True)

    # allow the docker image to release file handles
    time.sleep(2)

    # write our handlers somewhere that they won't get overwritten!
    # con_dir = path.abspath(path.join('..', 'process-gps-points', 'swagger_server', 'controllers'))
    # controllers = [f for f in os.listdir(con_dir) if (path.isfile(path.join(con_dir, f)) and not '__' in f)]
    # for c in controllers:
    #     with(open(path.join(con_dir, c), 'w')) as file:
    #         new_file: List[str] = file.readlines()
    #         print(path.join(con_dir, c))
    #         print(swagger_warning)
    #         print(new_file)
    #
    #         # prepend warning to start of file
    #         new_file = swagger_warning + new_file
    #
    #         for line in new_file:
    #             if 'def ' in line and '):' in line:
    #                 cmd = re.findall(r'def\s(\w+)\(\w+\):', line)[0]
    #                 print(cmd)
    #
    #         # overwrite old content of file
    #         file.seek(0)
    #         file.writelines('\n'.join(new_file))
    #         file.truncate()
