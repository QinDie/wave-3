
a=int(input('integer'))
b=0

factor=2
if a < 2:
    print("invalid")
else :

    print (f'the factor is : {a}')
    factor =2
    while factor <= a :
        if a % factor ==0 :
            print(factor)
            a = a//factor
            b += 1
        else:
            factor += 1
    if b == 1 :
        print('is prime number')