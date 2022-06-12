#Create a email slicer that will give user name and domain name from the from which user has input.

#get user email address
print("What is your email address? ")
email = input()

#slice out user name
user_name = email[:email.index("@")]

#slice out domain name
domain_name = email[email.index("@")+1:]

#display message
print("Your user name is ",user_name," and your domain name is ", domain_name)





