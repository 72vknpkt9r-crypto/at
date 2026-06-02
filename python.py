print('Hello, world')

answer = input('What programming language are we learning?\n')
if answer == 'Python':
    print('Yep!')
    print('U cool!')
else:
    print('No way')

# compare two number
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'less then', num2)
if num1 > num2:
    print(num1, 'more then', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'equals', num2)
if num1 != num2:
    print(num1, 'not equal', num2)