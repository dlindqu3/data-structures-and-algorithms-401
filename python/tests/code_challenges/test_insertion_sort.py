import pytest

from code_challenges.insertion_sort import insertion_sort

def test_insertion_sort():
  list = [2,4,3,6,1]
  actual = insertion_sort(list)
  expected = [1,2,3,4,6]
  assert actual == expected

def test_insertion_sort2():
  list = [-5,10,3,5]
  actual = insertion_sort(list)
  expected = [-5,3,5,10]
  assert actual == expected
