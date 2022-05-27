number = input('Введите семизначное число: ')
numb_of_even = 0
numb_of_uneven = 0
numb_list = []
sum = 0
mult = 1
for i in number:
    i = int(i)
    numb_list.append(i)
    if i%2 == 0:
        numb_of_even+=1

    else:
        numb_of_uneven+=1


if numb_of_even > numb_of_uneven:
    print('Четных чиcел больше!')
    for i in numb_list:
        sum+=i
    print(sum)
elif numb_of_uneven > numb_of_even:
    print('Нечетных чиcел больше!')
    mult = mult* numb_list[0] * numb_list[2]* numb_list[5]
    print(mult)