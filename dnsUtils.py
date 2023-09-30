from fileUtils import getFileLines
import socket


def getSubDomains():
    try:
        rawSubdomains = getFileLines("subdomains.txt")
        return list(map(lambda subDomain: subDomain.strip("\n") + ".", rawSubdomains))
    except:
        raise ValueError("No sub domain was founded")


def getHostByName(dns):
    try:
        return socket.gethostbyname(dns)
    except socket.gaierror:
        return None


# def zoneTransfer(dominio):
#    resgistrosNS = dns.resolver.query(dominio, "NS")
#    lista = []
#    for registro in resgistrosNS:
#        lista.append(str(registro))
#    for registro in lista:
#        try:
#            transferenciaZona = dns.zone.from_xfr(dns.query.xfr(registro, dominio))
#        except:
#            raise ValueError("")
#        else:
#            registroDNS = transferenciaZona.nodes.keys()
#            registroDNS.sort()
#            for n in registroDNS:
#                print(transferenciaZona[n].to_text(n))
