import pytest

#
#
#
#
@pytest.fixture
def setup():
    print('launch browser')
    return "chrome"



@pytest.mark.sanity
@pytest.mark.regression
def test_one(setup):
    print('Test one')
    print('Browser is:', setup)


@pytest.mark.regression
def test_two(setup):
    print('Test two')
    print('Browser is:', setup)


@pytest.mark.sanity
def test_three(setup):
    print('Test three')
    print('Browser is:', setup)

@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("test_loginbyemail")
    assert True==True


@pytest.mark.regression
def test_loginbyfacebook():
    print("test_loginbyfacebook")
    assert True==True


@pytest.mark.regression
def test_loginbygoogle():
    print("test_loginbygoogle")
    assert True==True