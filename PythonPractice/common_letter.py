def common_letter_replace(string, letter):
    test_string = string.lower()
    test_string_actual = test_string.replace(" ","")
    seen_letters = []
    seen_letters_dict = {}

    for i in test_string_actual:
        if i not in seen_letters:
            seen_letters.append(i)
    for x in seen_letters:
        count = 0
        for i in test_string_actual:
            if x == i:
                count +=1
        seen_letters_dict[x] = count

    common_letter = max(seen_letters_dict, key=seen_letters_dict.get)

    test_string_final = list(string)
    for index, i in enumerate(test_string_final):
        if test_string_final[index] == common_letter:
            test_string_final[index] = letter
    res = "".join(test_string_final)
    return(res)


print(common_letter_replace('my mom loves me as never did', 't'))



