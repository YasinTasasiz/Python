import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
randomNumber = random.randrange(0, x)
print(f"{names[randomNumber]} is going to buy the meal today!")