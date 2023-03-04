import sys
sys.path.append('.')
import shared as sh

def test_space_compress():
    test_str = " This! is      a ,test string  "

    assert "This! is a ,test string" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)
