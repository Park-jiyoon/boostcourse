num = 0
tot = 0.0

while True:
    sval = input("Enter a number" )
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue
    print(fval)
    num = num+1
    tot = num + fval

print('끝')
print(tot, num, tot/num)