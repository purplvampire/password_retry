x = 0
password = 'a123456'
while x < 3:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功!')
        break
    else:
        x += 1
        y = 3 - x
        if y > 0:
            print('密碼錯誤!還有', y, '次機會!')
        else:
            print('密碼錯誤!帳戶已鎖定!')

