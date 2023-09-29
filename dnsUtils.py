from fileUtils import getFileLines
import socket


def getSubDomains():
    rawSubdomains = getFileLines("subdomains.txt")
    return list(map(lambda subDomain: subDomain.strip("\n") + ".", rawSubdomains))


def bruteForceDNS(domain, subDomains):
    for subDomain in subDomains:
        dns = subDomain.strip("\n") + domain

        result = getHostByName(dns)

        if result is None:
            continue

        print("DNS Found: " + dns)


def getHostByName(dns):
    try:
        return socket.gethostbyname(dns)
    except socket.gaierror:
        return None
