cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

mydict = {}
for text in cpdomains:
    number, domain = text.split(" ")
    subdomain = domain.split(".")

    for item in range(len(subdomain)):
        mydict.setdefault(".".join(subdomain[item:]), int(number))


print(["{} {}".format(count, name) for name, count in mydict.items()])
