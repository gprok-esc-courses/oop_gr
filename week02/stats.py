
c = 'y'

while c == 'y':
    x = int(input("Sales: "))

    if x > 100:
        print("Very big value")
    else:
        for i in range(x):
            print('*', end='')
        print()

    c = input("Continue y/n: ")
