import combi
import pytest

@pytest.fixture
def setUp():
    print("Test case started")
    yield
    print("test case closed.")


@pytest.mark.parametrize("a,b", [(64,8),(16,4),(25,5)])
def test_sqroot(a,b,setUp):
    r = combi.sroot(a)
    assert r == b

@pytest.mark.xfail
@pytest.mark.parametrize("a,b", [(64,8),(16,4),(25,5)])
def test_sqroot1(a,b,setUp):
    r = combi.sroot(a)
    assert not r == b

@pytest.mark.parametrize("a,b,c,d",[(1,5,6,(-3+0j,-2+0j)),(5,6,4,(-0.6-0.6633249580710799j,-0.6+0.6633249580710799j))])
def test_quar(a,b,c,d,setUp):
    r = combi.quadratic(a,b,c)
    assert r == d

@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c,d",[(1,5,6,(-3+0j,-2+0j)),(5,6,4,(-0.6-0.6633249580710799j,-0.6+0.6633249580710799j))])
def test_quar1(a,b,c,d,setUp):
    r = combi.quadratic(a,b,c)
    assert not r == d

@pytest.mark.skip
@pytest.mark.parametrize("a,b,c,d",[(1,5,6,(-3+0j,-2+0j)),(5,6,4,(-0.6-0.6633249580710799j,-0.6+0.6633249580710799j))])
def test_quar2(a,b,c,d,setUp):
    r = combi.quadratic(a,b,c)
    assert not r == d

@pytest.mark.parametrize("a,b",[(37,98.60000000000001),(29,84.2)])
def test_celfeh(a,b,setUp):
    r = combi.celtofah(a)
    assert r == b

@pytest.mark.parametrize("a,b",[(2,"Positive number"),(-1,"Negative number"),[0,"zero number"]])
def test_povneg(a,b,setUp):
    r = combi.povandneg(a)
    assert r == b

@pytest.mark.parametrize("a,b",[(16,136),(12,78)])
def test_sum(a,b,setUp):
    r = combi.recsum(a)
    assert r == b