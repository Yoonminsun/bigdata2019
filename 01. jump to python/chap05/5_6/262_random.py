import random

# print(random.random())
# print(random.randint(1,10))

def random_choice(data):
    number = random.choice(data)
    return number

print(random_choice([3,5,7,2,1,8]))