import re

def space_compress(stocomp):
    assert isinstance(stocomp, str), "Expected str but got {} instead".format(type(stocomp))
    
    comp = re.sub(r'\s+', ' ', stocomp)
    
    #secondary boolean check for function input object type str
    if isinstance(stocomp,str) == False:
        print("Expected str but got {} instead".format(type(stocomp)))
    
    return comp.strip()
