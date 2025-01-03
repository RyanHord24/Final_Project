def factorial(num):
    if num == 0:
        return 1
    if num < 0:
        return "Error! Factorials do not apply to numbers less than zero."
    if num > 0:
        factorial_list = [num]
        while num >= 2:
            num-= 1
            factorial_list.append(num)
        product = 1
        for x in factorial_list:
            product*= x
        return product
print(factorial(5))