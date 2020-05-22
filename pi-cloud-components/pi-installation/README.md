# Pi client libary and functionality

## Requirements
Python 3.5.2+

The following files in this directory:
```
1.   secret.json  ->      this is a "password" - nothing fancy just classic private-private key
                          the file format is as follows:

                          {
                            "secret": "my-secret-here"
                            "url": "my-url-here"
                          }

                        Note that this will need to match the secret.json in the cloud-server folder!!
```

## Usage
To test, first double check that your secret.json is in your pi-installation folder.

next, test your Apis with the following:
```
python3 test-apis.py
```
