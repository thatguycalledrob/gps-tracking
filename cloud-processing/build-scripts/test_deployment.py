import requests

# Note, you will get a 403, unless you deploy with the # --allow-unauthenticated command

if __name__ == '__main__':
    s = requests.session()
    r = s.post('https://cloud-processing-lcn55j3ska-ew.a.run.app')
    print(r.status_code)
    print(r.text)
    s.close()