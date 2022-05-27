word = input('Введите слово: ')
glas_letters = ['ё','у','е','ы', 'а','о','э','я','ю']
soglas_letters = ['й','ц','к','н','г','ш','щ','з','х','ъ','ф','в','п','р','л','д','ж','ч','с','м','т','ь','б']
checkpair_lower = 0
checkpair_upper = 0
pairs_of_lower = 0
pairs_of_upper = 0
num_of_glas = 0
numb_of_soglas  = 0
for i in word:
    if i.lower() in glas_letters:
        num_of_glas+=1
    elif i.lower() in soglas_letters:
        numb_of_soglas+=1

    if i.isupper() and checkpair_upper>0:
        pairs_of_upper+=1
        checkpair_upper = 0
    elif i.isupper() and checkpair_upper == 0:
        checkpair_upper+=1
        continue
    else:
        checkpair_upper = 0



    if i.islower() and checkpair_lower >0:
        pairs_of_lower+=1
        checkpair_lower = 0
    elif i.islower() and checkpair_lower == 0:
        checkpair_lower+=1
        continue
    else:
        checkpair_lower = 0

print(f'Количество пар нижнего регистра: {pairs_of_lower},\n'
      f'Количество пар верхнего регистра: {pairs_of_upper},\n'
      f'Количество букв в слове: {len(word)},\n'
      f'Количество гласных букв в слове: {num_of_glas},\n'
      f'Количество согласных букв в слове: {numb_of_soglas}.')