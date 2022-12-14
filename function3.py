# function3.py

wordlist=['j','a', 'm']

def change(x):
    x1 = x[:]
    x1[0]='h'
    print('내부:', x1)

change(wordlist)
print(wordlist)

g=1
def testScope(a):
    global g
    g = 2
    return g+a

print(testScope(1))
print('전역변수 g:', g)


def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print( intersect("ham","spam"))


def times(a=10, b=20):
    return a*b

print( times())
print( times(5))
print( times(5,6))


def connectURI(server, port):
    strURL = "http://"+server + ":" + port
    return strURL

print( connectURI( 'credu.com', '80'))
print( connectURI( port='8080', server='credu.com'))
