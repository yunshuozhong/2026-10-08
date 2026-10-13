x = int(input())
if x<0 or x>15:
    print('輸入錯誤')
else:
    print(f"二進制表示:{x//8}{(x%8)//4}{(x%4)//2}{x%2}")
    print(f"八進制表示:{x//8}{x%8}")
    
    if x == 10:
        a = 'A'
    elif x == 11:
        a = 'B'
    elif x == 12:
        a = 'C'
    elif x == 13:
        a = 'D'
    elif x == 14:
        a = 'E'
    elif x == 15:
        a = 'F'
    else:a = x
    
    print(f"十六進制表示:{a}")