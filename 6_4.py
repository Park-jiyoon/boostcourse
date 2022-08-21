# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"


def good_customer(information):
    li = information.split(',')
    n = 0
    data = dict()
    id = list()
    age = list()
    num = list()
    gender = list()
    area = list()
    count = list()

    while n < len(li):
        if li[n] == 'x':   #전화 번호 정보 없으면 000으로 변경
            li[n] = '000-0000-0000'
        #각각 리스트로 저장해주기 (dict의 value를 각각 넣어주려고)
        if n == 0 or n == 6 or n == 12 or n == 18 or n == 24 or n == 30:
            id.append(li[n])
        elif n == 1 or n == 7 or n == 13 or n == 19 or n == 25 or n == 31:
            age.append(li[n])
        elif n == 2 or n == 8 or n == 14 or n == 20 or n == 26 or n == 32:
            num.append(li[n])
        elif n == 3 or n == 9 or n == 15 or n == 21 or n == 27 or n == 33:
            gender.append(li[n])
        elif n == 4 or n == 10 or n == 16 or n == 22 or n == 28 or n == 34:
            area.append(li[n])
        elif n == 5 or n == 11 or n == 17 or n == 23 or n == 29 or n == 35:
            count.append(li[n])

        n = n + 1

    data['아이디'] = id
    data['나이'] = age
    data['전화번호'] = num
    data['성별'] = gender
    data['지역'] = area
    data['구매횟수'] = count

    n = 0
    vip = 0
    vip_count = 0

    vip_list = data['구매횟수']

    #구매횟수 제일 많은 수 찾기
    for i in vip_list:
        if vip < int(i):
            vip = int(i)
            vip_count = n
        n = n + 1

    final = list()
    #vip 새로 리스트로 저장
    for k, c in data.items():
        final.append((c[vip_count]))

    print('할인 쿠폰을 받을 회원정보 아이디:'+final[0] + ',', '나이:'+
          final[1] + ',','전화번호:' + final[2] + ',', '성별:' + final[3] + ',', '지역:' + final[4] + ',','구매횟수:' + final[
              5])


good_customer(info)
