
N = int(input('введите колличество элементов списка A  '))
A_incoming = input('введита элементы списка через пробел   ').split()
A_num = list(map(int, A_incoming))
if len(A_num) != N:
    print('введённые элементы не соответвует заявленному колличеству  ')
else:
    X = int(input('введите число Х, которое надо найти   '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'число X встречается в списке A {count} раз')









