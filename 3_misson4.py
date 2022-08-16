def count_prime_numbers(first, last ):
    count = 0
    for i in range(first, last+1):
        num = 0

        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    num = num + 1
            if num == 0:
                count = count + 1
    print('소수 개수 : ', count)


n = int(input("첫번 째 수 입력 :"))
m = int(input("두번 째 수 입력 :"))

count_prime_numbers(n, m)