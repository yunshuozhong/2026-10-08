A = int(input('A='))
B = int(input('B='))
if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("輸入錯誤")
else:
    if A == 1 or B == 1:
        or_ = 1
    else:
        or_ = 0

    if A == 1 and B == 1:
        and_ = 1
    else:
        and_ = 0

    if A != B:
        xor_ = 1
    else:
        xor_ = 0
        
    print(f"OR結果: {or_}")
    print(f"AND結果: {and_}")
    print(f"XOR結果: {xor_}")