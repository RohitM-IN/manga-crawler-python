import requests
import time
import sys
from joblib import Parallel, delayed

f  = open('checked.txt', 'w')
f.flush()
f.close()

def getProxy():
    retry = 0
    while((sum(1 for line in open('checked.txt')) < 1) and retry < 10):
        try:
            proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1700&country=all&ssl=all&anonymity=all&simplified=true").text.splitlines( )
            print(len(proxies))
            Parallel(n_jobs=10)(delayed(test)(proxy) for proxy in proxies)
            print(sum(1 for line in open('checked.txt')))
            retry += 1
        except:
            return None

def test(proxy):
    try:
        proxies = {'http': proxy}
        # r = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=5)
        r = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if r.status_code == 200:
            f = open('checked.txt', 'a')
            f.write(proxy + "\n")
            f.close()
            count = count + 1
        #     return True
        # else:
        #     return False
    except:
        return False

getProxy()