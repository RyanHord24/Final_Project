def card_number(num):
    card_number = str(num)
    list_card_num = []
    for n in card_number:
         n = int(n)
         list_card_num.append(n)
    for n in list_card_num:
        if n * 2 >= 10 and list_card_num.index(n) % 2 != 0:
            str1 = str(n * 2)
            n = int(str1[0]) + int(str1[1])
        if n * 2 < 10 and list_card_num.index(n) % 2 != 0:
            n = n * 2
        card_sum = 0
    print(list_card_num)
    for n in list_card_num:
        n = int(n)
        card_sum+= n
    if card_sum % 10 == 0:
        return True
    if card_sum % 10 != 0:
        return False
print(card_number(5541808923795240))