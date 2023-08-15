from flask_restful import Resource
import os, requests, pickle

# add './caddy_root.crt' to verify for security



class WhoIsHome(Resource):
    
    def get(self):
        with open('unifi_cookie', 'rb') as f:
            cookie = pickle.load(f)
        
        code = requests.get('https://unifi.local/api/self', verify=False).status_code

        if code != 200:
            user=os.environ.get("UNIFI_API_USER")
            password=os.environ.get("UNIFI_API_PASSWORD")
            headers = {"Accept": "application/json","Content-Type": "application/json"}
            data = {'username': user, 'password': password}
            cookie = requests.post('https://unifi.local/api/login', headers = headers,  json = data, verify=False).cookies
            with open('unifi_cookie', 'wb') as f:
                pickle.dump(cookie, f)

        
        result = []
        data = requests.get('https://unifi.local/api/s/default/stat/sta', cookies=cookie, verify=False).json()


        for device in data.get('data', []):
            name = device.get('name')
            if name and '-PHONE' in name:
                result.append({'name': name.split('-')[0]})
        return result
