import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes': 107, 'name':'Class of python', 'views': 48654}
        ,{'likes': 156, 'name':'One milion in one hour', 'views': 84666}
        ,{'likes': 846513, 'name':'Front-end with java', 'views': 846514},
        {'likes': 8965, 'name':'AWS Cloud Practitioner Certification'}]

for i in range(len(data)):
    response = requests.put(BASE + "video/3" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())