def gugudan(num):
    print(num, '단')
    i = 1
    tot = 1
    while i <= 9:
        tot = num * i
        if tot <= 50:
            print(num, 'x', i)
            i = i+2
        else:
            break


numbers = int(input("몇 단 ? :"))

gugudan(numbers)
