import  random
digit = (input('Введите искомую цифру: '))
count_of_numbs = int(input('Введите количество чисел: '))
list_of_nums = ""
iter_num = 0
count_of_meet = 0
if count_of_numbs!=0:
    while iter_num < count_of_numbs:
       list_of_nums+=str(random.randint(1,100)) +','
       iter_num+=1
    for i in list_of_nums:
        if i in digit:
            count_of_meet+=1

print(f"Числа:{list_of_nums}")
print(f"Количетсво встреч:{count_of_meet}")