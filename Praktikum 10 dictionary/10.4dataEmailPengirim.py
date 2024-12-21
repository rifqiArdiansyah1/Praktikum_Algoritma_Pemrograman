fhand = open('data-short.txt')
domain = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        domainName = words[1].split('@')
        if domainName[1] not in domain:
            domain[domainName[1]] = 1
        else:
            domain[domainName[1]] += 1
print(f"Nama Domain Pengirim:\n{domain}")
print(f"Total Domain: {len(domain)}")
