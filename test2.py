def findMax(a, b, c):
    if a > b :
        biggest = a
    else :
        biggest = b
        
        if c > biggest :
            biggest = c
        return biggest
    
a = int(input("첫번째 숫자 입력: "))
b = int(input("두번째 숫자 입력: "))
c = int(input("세번째 숫자 입력: "))

biggest = findMax(a, b, c)

print(a, b, c, "중에 가장 큰 수는", biggest, "입니다.")