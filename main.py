
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = 0
while number < len(my_list):
    if my_list[number] > 0:
        print(my_list[number])
    if my_list[number] < 0:
        break
    number += 1