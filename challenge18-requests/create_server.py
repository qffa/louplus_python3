import requests

def create_server(name, host):
    server = {
            'name': name,
            'host': host
            }

    url = 'http://localhost:5000/servers/'

    r = requests.post(url, json = server)


    return  r.json()


if __name__ == '__main__':
    print(create_server('test10101010101010101010', '127.0.0.1'))
