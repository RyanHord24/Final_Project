def ninetyninebottles(num):
    while num > 1:
        num_minus_one = num - 1
        print(f'{num} bottles of beer on the wall, {num} bottles of beer.')
        print(f'Take one down and pass it around, {num_minus_one} bottles of beer on the wall.\n')
        num -= 1
    
    # Handle the case when there's only one bottle left
    if num == 1:
        print(f'{num} bottle of beer on the wall, {num} bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.\n')

    # End of the song
    print('No more bottles of beer on the wall, no more bottles of beer.')
    print('Go to the store and buy some more, 99 bottles of beer on the wall.')
ninetyninebottles(99)