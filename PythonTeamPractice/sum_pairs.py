def pairs(list1, num):
    success_list = []
    for x in list1:
        for y in list1:
            if x + y == num and list1.index(x) != list1.index(y):
                pair = []
                pair.append(x)
                pair.append(y)
                if [x, y] and [y, x] not in success_list:
                    success_list.append(pair)                
    return success_list
print(pairs([1,2,3,4,5], 9))

