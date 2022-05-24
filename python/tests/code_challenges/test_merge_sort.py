import pytest

from code_challenges.merge_sort import merge_sort

def test_merge_sort():
  list = [2,4,3,6,1]
  actual = merge_sort(list)
  expected = [1,2,3,4,6]
  assert actual == expected

def test_merge_sort2():
  list = [-5,10,3,5]
  actual = merge_sort(list)
  expected = [-5,3,5,10]
  assert actual == expected
