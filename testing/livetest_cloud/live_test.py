import requests
import os

if __name__ == '__main__':
    secret_file = os.path.abspath(os.path.join("..", "..", "cloud","secret.txt"))
    with open(secret_file, 'r+') as f:
        secret = f.read()

    url = "https://van-tracker-lcn55j3ska-ew.a.run.app"

    print("url = ", url)
    print("secret = ", secret)

    auth_headers = {"Authorization": secret}

    r = requests.get(f"{url}/positions", headers=auth_headers)
    print("done")
    print(r.status_code)
    print(r.text)

    r = requests.post(f"{url}/position", json={"data": "test_container"}, headers=auth_headers)
    print("done")
    print(r.status_code)
    print(r.text)


    #assert(r.status_code == 201)
