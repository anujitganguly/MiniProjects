# strip() method is used in Python to remove or truncate the given characters from beginning or end of string
email = input("Enter your complete Email ID: ").strip()

# :email.index("@") is used to strip from front
uname = email[:email.index("@")]
# email.index("@")+1: is used to strip from back. Note position of ':'
dname = email[email.index("@")+1:]

outp = (f"Username is: '{uname}' \nDomain name is: '{dname}'")
print(outp)

### Future Scope: This can be merged in a database where we need to store a lot of domains that will result in saving memory