import requests
import simplejson as json
import time
import os

from pprint import pprint

inicio = time.time()
i=0

while True:

    response = requests.post('https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token', headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
    response.raise_for_status()
    payload=response.json()
    headers2 = {
            'X-Auth-Token' : payload.get('Token')
    }
    response2 = requests.get("https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device",headers=headers2)
    payload2 = response2.json()
    payload2=payload2.get('response')
    
    tabla = []

    for org in payload2:
        tabla.append(dict(hostname=org.get('hostname'), reachabilityStatus=org.get('reachabilityStatus')))

    i = i+1
    
    with open ('tarea8.json','w') as f:
        json.dump(tabla,f)

    final= time.time()
    print ("El archivo se actualizo", i, "veces")
    time.sleep(300)
    
    if final - inicio >= 3000:
        break
    
    print ("El programa ha finalizado")

