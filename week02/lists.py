
sales = [10, 8, 12, 15]
quarter = ['A', 'B', 'C', 'D']

for i in range(len(sales)):
    print(quarter[i], end=' ')
    for j in range(sales[i]):
        print('*', end='')
    print(' (', sales[i], ')')
