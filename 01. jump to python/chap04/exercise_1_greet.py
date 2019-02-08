import sys

def greet_users(usernames):
    for i in usernames:
        print("Hello, %s%s!" % (i[0].upper(), i[1:]))

args = sys.argv[1:]
greet_users(args)
