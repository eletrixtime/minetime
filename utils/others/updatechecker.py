VERSION = "0.0.2"
TYPE = "BETA"
PATCHNUMBER = "P4"
import requests
import json
def check():
    try:
        r = requests.get("https://raw.githubusercontent.com/EletrixtimeYT/files/main/minetime_version.json")
        v = json.loads(r.text)
        #print(r.text)
        if v["VERSION"] == VERSION:
            if v["TYPE"] == TYPE:
                if v["PATCHNUMBER"] == PATCHNUMBER:
                    return True
        else:
            #print("V1")
            return False
        
    except:
        print("Failed to check update ! (skipping)")
        return True