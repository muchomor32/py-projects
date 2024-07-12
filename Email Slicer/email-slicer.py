#EMAIL SLICER
import re

#Email validation
email = "_"

while not re.match("^[A-Za-z0-9]+[@]+[A-Za-z]+[.]+[A-Za-z]+$", email):
    email = input("Enter a valid email: ")

#Email slicer
emSplit = email.split("@")
print("Username: " + emSplit[0])
print("Domain: " + emSplit[1])
