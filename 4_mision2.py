def count_word(word, check):
    fh = open("new.txt", 'w')
    fh.write(word)
    fh = open("new.txt", 'r')
    count = 0
    for lx in fh:
        if check in lx:
            count = count + 1
    return count

a = """
안녕하세요 정말 반갑습니다.
정말 감사합니다.
정말 죄송합니다.
그런데 정말 감사합니다.
"""

print(count_word(a, '정말'))
