from flask_restful import Resource
import os, requests

# add './caddy_root.crt' to verify for security
# make cookies persistent
# define error

class WhoIsHome(Resource):
    
    def get(self):
        # get variables for connection
        host = os.environ.get("UNIFI_HOST_URL")
        site = os.environ.get("UNIFI_SITE")
        user = os.environ.get("UNIFI_API_USER")
        password = os.environ.get("UNIFI_API_PASSWORD")

        # prepare headers and data
        headers = {"Accept": "application/json","Content-Type": "application/json"}
        data = {'username': user, 'password': password}

        # create a session and get connected devices
        s = requests.session()

        login = s.post(f"{host}/api/login", headers = headers,  json = data, verify=False)
        data = s.get(f"{host}/api/s/{site}/stat/sta", verify=False).json()

        # only return devices with name ending in -PHONE
        result = []
        for device in data.get('data', []):
            name = device.get('name')
            if name and '-PHONE' in name:
                result.append({'name': name.split('-')[0]})
        return result
