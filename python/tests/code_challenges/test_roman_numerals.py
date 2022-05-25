from code_challenges.roman_numerals import convert_roman

def test_14():
  actual = convert_roman('XIV')
  expected = 14
  assert actual == expected


def test_103():
  actual = convert_roman('CIII')
  expected = 103
  assert actual == expected
