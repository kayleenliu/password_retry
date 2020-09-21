# test password
password = 'a123456'
p = input ('input your password please:')
n = 0
while p != password and n < 3:
    j = 2 - n
    print('password is not correct! you have', j, 'trials left')
    n = n + 1
    if j > 0:
        p = input('input your password please:')
    elif j <= 0:
        print('access denied')
        break

while p == password:
    print('access successfully')
    break