def numerals(num):
    output = ''
    while num / 1000 >= 1:
        output+= 'M'
        num-= 1000
    while num / 900 >= 1:
        output+= 'CM'
        num-= 900
    while num / 500 >= 1:
        output+= 'D'
        num-= 500
    while num / 400 >= 1:
        output+= 'CD'
        num-= 400
    while num / 100 >= 1:
        output+= 'C'
        num-= 100
    while num / 90 >= 1:
        output+= 'XC'
        num-= 90
    while num / 50 >= 1:
        output+= 'L'
        num-= 50
    while num / 40 >= 1:
        output+= 'XL'
        num-= 40
    while num / 10 >= 1:
        output+= 'X'
        num-= 10
    while num / 9 >= 1:
        output+= 'IX'
        num-= 9
    while num / 5 >= 1:
        output+= 'V'
        num-= 5
    while num / 4 >= 1:
        output+= 'IV'
        num-= 4
    while num > 0:
        output+= "I"
        num-= 1
    return output
print(numerals(944))