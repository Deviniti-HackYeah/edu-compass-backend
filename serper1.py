import http.client
import json
import os
import hashlib

cache_dir="/tmp/gpt"




def callSerper(message):
    

    file_name = "serper_" + hashlib.md5(str(message).encode()).hexdigest() + ".txt"
    file_path = os.path.join(cache_dir, file_name)
    
    try:
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                result = f.read()
      
        return json.loads(result)
    except:
        pass


    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
        "q": message,
        "gl": "pl",
       "hl": "pl"
    })
    headers = {
        'X-API-KEY': '***REMOVED***',
        'Content-Type': 'application/json'
    }

    conn.request("POST", "/search", payload, headers)
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")

    with open(file_path, "w", encoding="utf-8") as f:
      f.write(decoded)
    return json.loads(decoded)

resp = callSerper("Politechnika Warszawska budownictwo drogowe oraz transport  rekrutacja")
print(resp["organic"])