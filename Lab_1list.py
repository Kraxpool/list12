import random
s = int(input('size->'))
b = int(input('begin->'))
e = int(input('end->'))

my_list = list()
for i in range(s):
    my_list.append(random.randint(b, e))
    for i in my_list:
        print(f'{my_list.index(i)}{[i]}',end="")
print()
nul = 1
for i in range (0, len ( my_list ), 3):
 print(f'{nul} * {my_list[i]}{[i]}=', end='')
 nul += my_list[i]
 print(nul)
sum_list =[0]*3
for i in my_list:
    if i < 0:
        sum_list[0] += i
    if i % 2 == 0:
        sum_list[1] += i
    if i % 2 != 0:
        sum_list[2] += i
    print(f'Sun negative: {sum_list[0]}')
    print(f'Sum even: {sum_list[1]}')
    print(f'Sun odd: {sum_list [2]}')
    print(f'Nul even: {nul}')





