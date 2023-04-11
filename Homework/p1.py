# Sum all the numbers of a given array ( cq. list ), except the highest 
#and the lowest element ( by value, not by index! ).
# The highest or lowest element respectively is a single element at each edge, 
#even if there are more than one with the same value.
# Mind the input validation.
# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6


#before

def sum_array(arr):
  
  if arr is None or len(arr) < 2:
    return 0
  
  mi, ma, s = arr[0], arr[0], 0
  
  for x in arr:
    if x > ma:
      ma = x
    elif x < mi:
      mi = x
    
    s += x
  
  return s - mi - ma

print(sum_array([6, 2, 1, 8, 10]))


#After time complexcity

def sum_array2(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0

print(sum_array2([6, 2, 1, 8, 10]))
