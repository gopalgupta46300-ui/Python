""" First Segment of Lambda Function """
def square(x):
    return x * x

def functionApply(fx, val0, val1):
    return power(val0,val1)
    
power = lambda x, y : x ** y

print(square(5))
print(power(2,10))
# lambda function is anonymizes function
print(functionApply(power, 5,3))

''' Second Segment '''

print("''' Second Segment '''")

string = lambda x , y : x + y
compare = lambda x , y : x == y
hello = lambda x : "Hello! " + x

print(string("Siya","Ram"))
print(compare("Radhe", "Radhe"))
print(hello("Gopal"))
