print("hello world!")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def result_addition (a, b):
    result = a + b
    return result
    
def result_subtraction (a, b):
    result = a - b
    return result

def result_division (a, b):
    result = a / b
    return result

def result_multiplication (a, b):
    result = a * b
    return result

x = result_addition(a,b)
print(x)
y = result_subtraction(a,b)
print(y)
v = result_division(a,b)
print(v)
b = result_multiplication(a,b)
print(b)


