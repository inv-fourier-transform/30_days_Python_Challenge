# Function to validate Gmail addresses from a text string using regex
import re

def gmail_validate(text_string: str):
    valid_gmails = []

    # Google enforces 6-64 characters, @google.com or @googlemail.com are both valid
    pattern = re.compile(
        r'\b'
        r'(?=[a-zA-Z0-9.]{6,64}(?:\+[^@]+)?@)'
        r'[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*'
        r'(?:\+[^@]+)?'
        r'@(?:gmail|googlemail)\.com'
        r'\b',
        re.IGNORECASE
    )

    for email in text_string.split():
        if re.findall(pattern, email):

            if email.endswith(".com"):

                # Remove dots in the email before the final dot
                email = "".join(email.split(".")[:-1])+"."+email.split(".")[-1]

                # Remove all + in the email before the final dot
                email = "".join(email.split("+"))

                valid_gmails.append(email)

            elif email.endswith(".com."):
                if email.split(".")[-2] == "com":
                    email = "".join(email.split(".")[:-2]) + "." + email.split(".")[-2]
                    email = "".join(email.split("+"))

                    valid_gmails.append(email)

            else:
                print("Invalid email address: ", email)


    return valid_gmails


if __name__ == "__main__":
    text_input_string = input("Enter the text string: ")
    print(gmail_validate(text_input_string))