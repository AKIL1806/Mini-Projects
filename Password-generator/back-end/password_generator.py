import random
import string

def generate_password(length=12):
    if length < 4 :
        return "The length should be atleat 4"
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    if length > 4:
        all_chars = upper + lower + digits + symbols
        password += random.choices(all_chars,k=length-4)

    random.shuffle(password)
    return ''.join(password)

if __name__ =="__main__":
    length = int(input("Enter desired password length: "))
    print("Generate Password:",generate_password(length))