def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) == len(str2):
        new_str1 = str1.lower()
        new_str2 = str2.lower()
        common_letters = []
        for letter in new_str1:
            if letter in new_str2 and letter not in common_letters:
                common_letters.append(letter)
        if len(common_letters) == len(new_str1):
            return True
        if len(common_letters) != len(new_str1):
            return False 
print(is_anagram('charm', 'march'))

def anagram_for(test_word, list):
    anagram_list = []
    non_anagram_list = []
    for word in list:
        if len(word) != len(test_word):
            non_anagram_list.append(word)
        if len(word) == len(test_word):
            new_word = word.lower()
            new_test_word = test_word.lower()
            common_let = []
            for letter in new_word:
                if letter in new_test_word and letter not in common_let:
                    common_let.append(letter)
            if len(common_let) == len(test_word):
                anagram_list.append(word)
            if len(common_let) != len(test_word):
                non_anagram_list.append(word)
    return anagram_list
print(anagram_for("saliter", ["cognac", "saltier", "realist", "retails"]))


