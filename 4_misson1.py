def make_comma(num):
    index = 0
    new_num = num  # 새로운 문자열로 생성
    pivot = 3
    while index < len(num)+1:  # 인덱스가 num문자열 길이 + 1보다 작은 동안 while문 실행
        if index == pivot:  # 피봇 : 천단위로 끊어지는 피봇으로 문자열을 뒤집어서 3,7,11,15.. 인덱스인 경우 컴마가 추가되어야 함
            new_num = new_num[:index] + ',' + new_num[index:]
            # 새로운 문자열에 인덱스 전까지 문자열 자르고 컴마 삽입 해준 후 인덱스 부터 문자열 끝까지 더해주기

            pivot = pivot + 4 # 피봇은 4를 더해줌

            # 새로운 문자열에 인덱스 전까지 문자열 자르고 컴마 삽입 해준 후 인덱스 부터 문자열 끝까지 더해주기
        index = index + 1
    return new_num


number = input("숫자를 입력하세요 : ")
number_reverse = number[::-1]    #문자열을 리버스로 변경
new = make_comma(number_reverse)
print(new[::-1]) #다시 리버스해서 출력