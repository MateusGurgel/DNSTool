from dnsUtils import getHostByName, getSubDomains
from collections import deque
import threading

# def bruteForce():
#        for subDomain in subDomains:
#            dns = subDomain.strip("\n") + domain
#
#            result = getHostByName(dns)
#
#            if result is None:
#                continue
#
#            print("DNS Found: " + dns)


class Counter:
    def __init__(self, current, max):
        self.current = current
        self.max = max

    def count(self, i=1):
        self.current += i

    def show(self):
        print(f"{self.current}/{self.max}")


def bruteForceDNS(domain, subDomains=getSubDomains(), threadsAmmount=20):
    query = deque(subDomains)
    threads = []

    counter = Counter(0, len(query))

    def bruteForce():
        while len(query) > 0:
            counter.count()
            dns = query.popleft() + domain
            ip = getHostByName(dns)

            if ip is None:
                continue

            print("DNS Found: " + dns)
            counter.show()

    for i in range(threadsAmmount):
        thread = threading.Thread(target=bruteForce)
        thread.daemon = True
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
