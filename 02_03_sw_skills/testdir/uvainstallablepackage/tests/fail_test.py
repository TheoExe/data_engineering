import sys
import pytest

sys.path.append('.')
import shared as sh

@pytest.mark.xfail
def test_fail():

	fail_str = "This string,  is expected to fail the test."

	assert "This string is expected to fail the test." == sh.space_compress(fail_str), "String <{}> not compressed as expected".format(fail_str)
