import pythonwhois


def lookup(domain):
    query = pythonwhois.get_whois(domain)
    return query


def is_live(domain):
    results = lookup(domain)
    for key, value in results.items():
        if key == "status":
            if value[0]:
                return True
            else:
                return False