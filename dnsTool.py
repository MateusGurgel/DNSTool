from dnsBruteforce import bruteForceDNS


def main(domain):
    print("Program started")

    print(f"Starting bruteforce on {domain}")
    bruteForceDNS(domain)


main("Google.com")
