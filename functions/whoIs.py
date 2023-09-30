import whois


def __isRegistered(domain):
    try:
        w = whois.whois(domain)
    except Exception:
        return False
    else:
        return bool(w.domain)


def query(domain):
    if not __isRegistered(domain):
        print("The domain does not exists on any registry")
        return None

    query = whois.whois(domain)
    print(query.text)
    return query.text


query("google.com")
