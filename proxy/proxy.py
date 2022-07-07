import requests
import time
import sys

def getProxy():
    f  = open('checked.txt', 'w')
    f.flush()
    f.close()
    retry = 0
    while((sum(1 for line in open('checked.txt')) < 1) and retry < 10):
        try:
            proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1700&country=all&ssl=all&anonymity=all&simplified=true").text.splitlines( )
            print("Proxy got:",len(proxies))
            for proxy in proxies:
                test(proxy)
            print("Proxy Working:",sum(1 for line in open('checked.txt')))
            retry += 1
        except:
            return None

def test(proxy):
    try:
        proxies = {'http': proxy}
        g = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if g.status_code == 200:
            f = open('checked.txt', 'a')
            f.write(proxy + "\n")
            f.close()
            count = count + 1

    except:
        return False