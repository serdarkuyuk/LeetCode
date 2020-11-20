emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
countEmail = 0
for email in emails:
    numberDot = 0
    for i, ch in enumerate(email):
        if email[~i] == "+" or numberDot >= 2:
            break
    else:
        countEmail += 1
print(countEmail)
