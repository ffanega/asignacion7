import requests
from pprint import pprint

response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
pprint(payload)
headers2 = {
        'X-Auth-Token' : payload.get('Token')
}
response2 = requests.get("https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device",headers=headers2)
payload2 = response2.json()
pprint(payload2)
payload2=payload2.get('response')
tabla = []
for org in payload2:
    tabla.append(dict(family=org.get('family'), hostname=org.get('hostname'),
                      managementIpAddress=org.get('managementIpAddress'),
                      lastUpdated=org.get('lastUpdated'), reachabilityStatus=org.get('reachabilityStatus')))
pprint(tabla)

