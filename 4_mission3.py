def wrong_guest_book(book):
    fh = open('guestbook.txt', 'w')
    fh.write(book)
    fh = open('guestbook.txt', 'r')
    for lx in fh:
        lx = lx.strip()
        if len(lx[3:]) == 13 and "010" in lx and "-" in lx:
            continue

        else:
            print("잘못 쓴 사람:", lx[0:2])
            print("잘못 쓴 번호:", lx[3:])


guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)
