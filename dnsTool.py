from dnsUtils import bruteForceDNS, getSubDomains


def main(domain):
    print("Program started")

    subDomains = getSubDomains()

    print(f"Starting bruteforce on {domain}")
    bruteForceDNS(domain, subDomains)


main("Google.com")
