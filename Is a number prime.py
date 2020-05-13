from b  import primenumber


a  = int(input('Please Input an Positive Int Number Greater Than One :'))
b = primenumber(a)
if b:
    print('is a Prime Number')
else:
    print(' is not a Prime Number')