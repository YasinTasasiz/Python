list1 = []
total = 0
for number in range(1, 101):
  if number % 2 == 0:
    list1.append(number)
    total += number
print(list1)
print(f"Total is : {total}")