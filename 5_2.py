def grader(s, a):
    score = 0
    newlist = list()
    for i in range(len(s)):
        grade = s[i]
        grade = grade.split(',')  # ','로 구분
        grade = grade[1:]  # 이름 자르기
        grade = "".join(grade)  # 문자열로 변환
        # print(grade)
        for j in range(len(a)): # 값 비교
            if a[j] == int(grade[j]):
                score = score + 10 # 스코어 계산
        s[i] = s[i] + ',' + str(score) # s[i]에 score 더해주기
        score = 0
        s[i] = s[i].split(',') # ','로 요소 나누기

    s.sort(reverse=True, key=lambda s: s[2]) # 점수로 내림 차순 정렬
    for i in range(len(s)):
        print("학생:"+s[i][0], "점수:"+s[i][2]+"점",i+1,"등")



s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]
grader(s, a)
