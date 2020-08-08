def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1

while True:
    try:
        n = int(input('Enter an integer: '))
        break
    except:
        print('Enter an integer!!!')

print(n)

while n != 1:
    n = collatz(n)
    print(n)
