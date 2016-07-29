def guess_list(char_set):
    lst = sorted(list(char_set))
    return ", ".join(lst)


def spaces(guessed, word):
    spaces = ""
    for char in word:
        if char == " " or char in guessed:
            spaces += char
        else:
            spaces += "_"
        spaces += " "
    return spaces


def check_word(word1, word2):
    return word1 == word2


def check_guesses(set1, word):
    set2 = set(word)
    sub = set2.issubset(set1)
    return sub