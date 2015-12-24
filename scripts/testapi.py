import requests 
payload = {'username': 'hamad', "password": "root"}
r = requests.post("http://127.0.0.1:8000/login/", data=payload)
token = r.json()['token']
headers = {'Authorization': "Token %s" % token}
r = requests.get("http://127.0.0.1:8000/activities/", headers=headers)
Html_file = open("output.json", "w")
Html_file.write(r.text)
Html_file.close()