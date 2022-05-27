my_str = input('Введите строку: ')
glas = ['у','е','а','о','э','ё','я','и','ю','ы']
soglas = ['й','ц','к','н','г','ш','щ','з','х','ъ','ф','в','п','р','л','д','ж','ч','с','м','т','ь','б']
count_of_glas = 0
count_of_soglas = 0
list_of_glas =  []

for i in my_str:
    if i in glas:
        count_of_glas+=1
        list_of_glas.append(i)
    elif i in soglas:
        count_of_soglas+=1
print(count_of_glas,count_of_soglas)
if count_of_glas == count_of_soglas:
    print(list_of_glas)