#sender email address
#recipient email address
#email subject
#email body
import re
email = 'email.txt'
with open(email, 'r', encoding="utf-8") as file:
    email = file.read()
semder_pattern= '^From.(<.>)'
sender = re.match(semder_pattern, email)
print(sender)