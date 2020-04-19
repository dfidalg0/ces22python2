# Exercício 3

def cleanword (string):
    s = ''
    for char in string:
        if char.isalpha():
            s += char

    return s

def has_dashdash (string):
    return '--' in string

def extract_words (string):
    s = ''
    for char in string:
        if char.isalpha():
            s += char.lower()
        else:
            s += ' '

    return s.split()

def wordcount (word, string_list):
    n = 0
    for string in string_list:
        if string == word:
            n += 1

    return n

def wordset (string_list):
    return sorted(set(string_list))

def longestword (string_list):
    n = 0
    for string in string_list:
        size = len(string)
        if size > n: n = size

    return n



def _tests ():
    # cleanword tests
    assert cleanword('what?') == 'what'
    assert cleanword("'now!'") == 'now'
    assert cleanword("?+='w-o-r-d!,@$()'") == 'word'

    # has_dashdash tests
    assert has_dashdash('distance--but')
    assert not has_dashdash('several')
    assert has_dashdash('spoke--')
    assert not has_dashdash('-yo-yo-')

    # extract_words tests
    assert extract_words("Now is the time! 'Now', is the time? Yes, now.") == \
        ['now','is','the','time','now','is','the','time','yes','now']
    assert extract_words('she tried to curtsey as she spoke--fancy') == \
        ['she','tried','to','curtsey','as','she','spoke','fancy']

    # wordcount tests
    assert wordcount(
        "now",
        ["now","is","time","is","now","is","is"]
    ) == 2
    assert wordcount(
        "is",
        ["now","is","time","is","now","the","is"]
    ) == 3
    assert wordcount(
        "time",
        ["now","is","time","is","now","is","is"]
    ) == 1
    assert wordcount(
        "frog",
        ["now","is","time","is","now","is","is"]
    ) == 0

    # wordset tests
    assert wordset(
        ["now", "is", "time", "is", "now", "is", "is"]
    ) == ["is", "now", "time"]
    assert wordset(
        ["I", "a", "a", "is", "a", "is", "I", "am"]
    ) == ["I", "a", "am", "is"]
    assert wordset(
        ["or", "a", "am", "is", "are", "be", "but", "am"]
    ) == ["a", "am", "are", "be", "but", "is", "or"]

    # longestword tests
    assert longestword(["a", "apple", "pear", "grape"]) == 5
    assert longestword(["a", "am", "I", "be"]) == 2
    assert longestword(["this","supercalifragilisticexpialidocious"]) == 34
    assert longestword([ ]) == 0

if __name__ == '__main__':
    _tests()
