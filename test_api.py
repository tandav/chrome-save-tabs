import requests

host = 'http://localhost:5000'


json = {
    'root': '/Users/tandav/',
    'path': '/Users/tandav/Documents/spaces/taxonomy/annoy',
}
# r = requests.post(host + '/last_dir_in_path', json=json)
r = requests.post(host + '/bookmark', json=json)

# print(r.status_code)
# print(r.status_code, r.json())
