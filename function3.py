

def connectURI(server, port):
    strURL = "http://"+server + ":" + port
    return strURL

print( connectURI( 'credu.com', '80'))
print( connectURI( port='8080', server='credu.com'))

def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print( union('ham', 'egg'))
print( union('ham', 'egg', 'spam'))


def userURIBuilder(server, port, **user):
    strURL = 'http://'+ server + ":" + port + '/?' 
    for key in user.keys():
        strURL += key + '=' + user[key] + '&'
    return strURL

print( userURIBuilder('credu.com','80', id='kim', passwd='1234' ))
print( userURIBuilder('credu.com','80', id='kim', passwd='1234', age='30' ))


#람다함수-일회성 함수

g = lambda x, y:x*y
print( g(3,4))
print( g(5,6))

print((lambda x:x*x)(3))
print( globals())

