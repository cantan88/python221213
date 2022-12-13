# function1.py

def times(a,b):
    return a*b

print( times(3,4))


def setValue(newValue):
    x= newValue
    print(x)

retValue = setValue(5)
print(retValue)

print('---불변형식---')
a = 1.2
print( id(a))
a = 2.3
print( id(a))

print('---가변형식---')
lst = [1, 2, 3]
print( id(lst))
lst.append(4)
print( id(lst))


print('---이름 해석 순서---')
def func1(a):
    x=1
    return x+a

#호출
print( func1(1))

x =5
def func2(a):
    return x+a

#호출
print( func2(1))



