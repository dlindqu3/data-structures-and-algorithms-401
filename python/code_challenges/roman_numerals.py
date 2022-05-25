matches = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convert_roman(r):
  int = 0
  for i in range(len(r)):
    current_val = matches[r[i]]
    if i + 1 < len(r) and matches[r[i+1]] > current_val:
      int -= current_val
    else:
      int += current_val
  return int

test_romans = 'XIV'
expected_num = 14
actual_num = convert_roman(test_romans)
print(expected_num == actual_num)
