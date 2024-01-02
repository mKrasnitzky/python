from python import main
import pytest


def test_find_primes():
    assert main.find_primes(15) == [2, 3, 5, 7, 11, 13]


def test_find_primes():
    assert main.find_primes(5) == [2, 3]


@pytest.mark.parametrize("myList, result",
                         [([2, 5, 6, 8, 4, 3], [2, 3, 4, 5, 6, 8]), ([5, 9, 8, 6, 4, 3], [3, 4, 5, 6, 8, 9])])
def test_sort_list(myList, result):
    assert main.sort_list(myList) == result


@pytest.mark.skip(reason="dont computed")
def test_find_primes():
    assert main.find_primes(100) == []


