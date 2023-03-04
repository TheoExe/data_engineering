import re

def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

import re
def space_compress(stocomp):
    assert isinstance(stocomp, str), "Expected str but got {} instead".format(type(stocomp))
        
    comp = re.sub(r'\s+', ' ', stocomp)
                
    #secondary boolean check for function input object type str
    if isinstance(stocomp,str) == False:
        print("Expected str but got {} instead".format(type(stocomp)))

    return comp.strip()


def string_upper(str_input):
    assert isinstance(str_input, str), "Expected str but got {} instead".format(type(str_input))

    #convert input string to uppercase and return
    return str_input.upper()

