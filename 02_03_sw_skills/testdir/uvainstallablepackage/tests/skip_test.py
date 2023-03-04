import sys
import pytest

sys.path.append('.')
import shared as sh

@pytest.mark.skip(reason="Failed test is expected and will be skipped")
def test_skip():

	fail_str = "This string,  is expected to fail the test."

	assert "This string is expected to fail the test." == sh.space_compress(fail_str), "String <{}> not compressed as expected".format(fail_str)
