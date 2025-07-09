import pytest

@pytest.mark.simulation
class Test:

    def test_v1(self):
        assert 1 == 1

    def test_v2(self):
        assert 1 != 1