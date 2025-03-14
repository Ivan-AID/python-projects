import random
names = input("Please enter your names, with each seperated by comma: ").split(",")
name_list = [name.strip() for name in names]
random_payer = random.choice(name_list)
print(f"{random_payer} is paying the bill")