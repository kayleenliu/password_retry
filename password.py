# test password
password = 'a123456'
p = input ('input your password please:')
n = 3
while n > 0:
    n = n - 1
    if p == password:
        print('access successfully')
        break
    else:
        if n > 0:
            print('password is not correct! you have', n, 'trials left')
            p = input ('input your password please:')
        else:
            print('access denied')       