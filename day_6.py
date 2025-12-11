import string, secrets

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def generate_password(length: int) -> str:
    lst=[]
    for i in range(length):
        if i==0:
            lst.append(secrets.choice(string.ascii_lowercase or string.ascii_uppercase))
        else:
            lst.append(secrets.choice(characters))
    return "".join(lst)


if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    print(generate_password(length))




