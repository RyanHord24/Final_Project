def fibonacci_sequence(num):
    list = [0, 1]
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num > 1:
        count = num - 1
        while count > 0:
            next_num = list[len(list) - 1] + list[len(list) - 2]
            list.append(next_num)
            count-= 1
    return list[len(list) - 1]
print(fibonacci_sequence(7))
