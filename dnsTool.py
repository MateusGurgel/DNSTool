from functions.dnsBruteforce import bruteForceDNS
from utils.dnsUtils import isValidDomain
import functions.whoIs as whoIs


def main():
    banner = """
         /$$$$$$$  /$$   /$$  /$$$$$$        /$$$$$$$$                  /$$
        | $$__  $$| $$$ | $$ /$$__  $$      |__  $$__/                 | $$
        | $$  \ $$| $$$$| $$| $$  \__/         | $$  /$$$$$$   /$$$$$$ | $$
        | $$  | $$| $$ $$ $$|  $$$$$$          | $$ /$$__  $$ /$$__  $$| $$
        | $$  | $$| $$  $$$$ \____  $$         | $$| $$  \ $$| $$  \ $$| $$
        | $$  | $$| $$\  $$$ /$$  \ $$         | $$| $$  | $$| $$  | $$| $$
        | $$$$$$$/| $$ \  $$|  $$$$$$/         | $$|  $$$$$$/|  $$$$$$/| $$
        |_______/ |__/  \__/ \______/          |__/ \______/  \______/ |__/             
                                                                   
    """

    print(banner)

    domain = input("What domain do you want to explore? | ")

    while not isValidDomain(domain):
        domain = input("Invalid domain, please try again | ")

    print()
    print("Searching for who is information...")
    print()

    whoISResult = whoIs.query(domain)

    print()
    print("Searching for subdomains...")
    print()

    bruteforceResult = bruteForceDNS(domain)


main()
