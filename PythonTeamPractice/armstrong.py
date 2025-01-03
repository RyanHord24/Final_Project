list_of_numbers = list(range(0, 1000))
armstrong_list = []
for n in list_of_numbers:
    string = str(n)
    sum = 0
    for i in string:
        exponent = len(string)
        i = int(i)
        sum+= i ** exponent
    if sum == n:
        armstrong_list.append(n)
print(armstrong_list)