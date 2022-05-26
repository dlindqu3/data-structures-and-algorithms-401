# from data_structures.hashtable import Hashtable


def first_repeated_word(string):
    words = string.split(' ')
    dict = {}
    for word in words:
        if word not in dict.keys():
            dict[word] = 1
        if dict[word] == 2:
            return word
        else:
            dict[word] += 1
    return 'no doubles'


string1 = 'hello how are you how'
string2 = 'I am good am and you'
string3 = 'this has no repeats'
print(first_repeated_word(string1))
print(first_repeated_word(string2))
print(first_repeated_word(string3))
