# You will be given an array a and a value x. 
# All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

#before

def present(arr, x):
    for i in arr:
        if i == x:
            return True
    else:
        return False
        
print(present([1,2,3,4,5,6,7,8,9],3))

#After

def present2(arr, x):
    if x in arr:
        return True
    else:
        return False
    
print(present2(["abc", "def", "ghi", "jkl"], "ghi"))
print(present2(["abc", "def", "ghi", "jkl"], "xyz"))
