#### RESTCONF LAB 8.3.7
#### Use a Python Script to Send a PUT Request
#### Step 1: Import modules and disable SSL warnings
import json
import requests
requests.packages.urllib3.disable_warnings()
#### Step 2: Create the variables that will be the components of the request
IP_HOST="192.168.44.46"
RESTCONF_USERNAME="admin"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
api_url = f"https://{IP_HOST}/restconf/data/ietf-interfaces:interfaces/interface=Loopback120"
headers = { "Accept": "application/yang-data+json",  "Content-type":"application/yang-data+json"  }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

yangConfig = {
  "ietf-interfaces:interface": {
     "name": "loopback120",
     "description": "RESTCONF loopback 120",
     "type": "iana-if-type:softwareLoopback",
     "enabled": True,
     "ietf-ip:ipv4": {
         "address": [
             {
                 "ip": "10.10.11.12",
                 "netmask": "255.255.255.0"
             }
         ]
     },
 "ietf-ip:ipv6": {}
 }
}

#### Step 3: Create a variable to send the request and store the JSON response
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
 print("STATUS OK: {}".format(resp.status_code))
else:
 print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
