import random
num1 =  int(input('Введите число от 1 до 20: '))
num2 =  int(input('Введите число от 1 до 20: '))
rand_num1 = 0
rand_num2 = 0
count_of = 0
iter = 0
while iter < 7:
    rand_num1 = random.randint(1,20)
    rand_num2 = random.randint(1,20)
    if iter == 4 :
        print(f'Рандомные числа: {rand_num1}, {rand_num2}')
    if num1 + num2 > rand_num1 + rand_num2:
        count_of +=1

    iter+=1
print(f'Введеных пар больше рандомных: {count_of}')