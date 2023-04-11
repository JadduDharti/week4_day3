# Write a function that accepts an integer n and a string s as parameters, 
# and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"


#before

def repeat_str(repeat, string):
    result = ""
    for i in range(repeat):
        result = result + string
    return result

print(repeat_str(6, "Hello"))


#After Time and space complexcity

def repeat_str2(repeat, string):
    return string * repeat

print(repeat_str2(6, "Hello"))