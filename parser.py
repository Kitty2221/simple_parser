lst = []


def pars_file():
    with open("test.txt", encoding="utf8") as file:
        for string in file.readlines():
            pars_line(string)
    symbols_to_string = ''.join(lst)
    print(pars_word(symbols_to_string))


def pars_line(string):
    for word in string.split():
        if len(word) == len(set(word)):
            lst.append(word[0])
        else:
            lst.append(pars_word(word))


def pars_word(word):
    for symbol in list(word):
        if word.count(symbol) == 1:
            return symbol
    return ''


pars_file()