n = int(input("첫번째 수 입력 :"))
m = int(input("두번째 수 입력 :"))


def find_even_number(n, m):
    numbers = [i for i in range(n, m+1)]
    count = 0
    for i in numbers:
        count = count + 1

        if i % 2 == 0 and (count == (m-n+2)/2):
            print(i, '중앙값')

        elif i % 2 == 0:
            print(i, '짝수')

        else:
            continue


find_even_number(n,m)
