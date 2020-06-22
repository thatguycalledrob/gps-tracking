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
```shell script
chmod a+x /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/test-apis.py
/usr/bin/python3 /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/test-apis.py
```

## Installation

First, install the swagger library:
```shell script
/usr/bin/python3 /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/swaggerlib/setup.py install
```

Now, install the requirements for the script
```shell script
/usr/bin/pip3 install -r /home/pi/Desktop/gps-tracking/requirements.txt
```

You may want to ensure the permissions on the gps.py file allow execution:
```shell script
chmod a+x /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/gps.py
```

The gps track is done via a cron tab. This is done on a 5 minute schedule.
Below is a one liner to add the cron job to 
```shell script
crontab -l > file; echo "*/2 * * * * /usr/bin/python3 /home/pi/Desktop/gps-tracking/pi-cloud-components/pi-installation/gps.py > /home/pi/Desktop/gps_app.log 2>&1" >> file; crontab file; rm file;
```