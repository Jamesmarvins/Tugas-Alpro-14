import re
import random
import string

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def extract_usernames_and_generate_passwords(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    results = []
    
    for email in emails:
        username = email.split('@')[0]
        password = generate_random_password()
        result = f"{email} username: {username} , password: {password}"
        results.append(result)
    
    return results

text = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

results = extract_usernames_and_generate_passwords(text)
for res in results:
    print(res)