from utils.dnsUtils import getHostByName, getSubDomains
from utils.counter import Counter
from collections import deque
import threading


def bruteForceDNS(domain, subDomains=None, threadsAmmount=200):
    if subDomains is None:
        try:
            subDomains = getSubDomains()
        except:
            print("No sub domain was found")

    query = deque(subDomains)
    threads = []
    result = []

    queryLenght = len(query)
    counter = Counter(0, queryLenght)

    def bruteForce():
        while len(query) > 0:
            counter.count()
            dns = query.popleft() + domain
            ip = getHostByName(dns)

            if ip is None:
                continue

            result.append(dns)
            print(counter.get() + "|" + " DNS Found: " + dns)

    for i in range(threadsAmmount):
        thread = threading.Thread(target=bruteForce)
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return result
