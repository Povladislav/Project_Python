my_str = input('Введите строку: ')
my_str = my_str.split()
count_of_digit = 0
for i in my_str:
    if i.isdigit():
        count_of_digit+=1

print(count_of_digit)