fhand = open("data-short.txt")
email = dict()
for line in fhand:
    if line.startswith("From "):
        words = line.split()
        if words[1] not in email:
            email[words[1]] = 1
        else:
            email[words[1]] += 1
print(email)
print(f"Total Akun Email: {len(email)}")