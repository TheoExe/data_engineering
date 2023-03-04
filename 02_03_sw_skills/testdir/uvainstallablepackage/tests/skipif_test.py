import sys
import pytest

sys.path.append('.')
import shared as sh

@pytest.mark.skipif(sys.platform == 'linux', reason="This OS is running {} so this test must fail.".format(sys.platform))
def test_skipif():

	fail_str = "This string,  is expected to fail the test."

	print("My platform is", sys.platform)

	assert "This string is expected to fail the test." == sh.space_compress(fail_str), "String <{}> not compressed as expected".format(fail_str)


