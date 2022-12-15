# demoSrt.py

# print( dir(str))

strA=' python is very powerful'
strB= '파이썬은 강력해'
print( len(strA))
print( len(strB))
print( strA.capitalize())
print( strA.count('p'))
print( strA.count('p',7))

print( 'MBC2580'.isalnum())
print( 'MBC:2580'.isalnum())
print( '2580'.isdecimal())
print( 'aaa.ppt'.endswith('ppt'))

print('---공백문자 제거---')
u = "<<< spam and ham >>>"

result = u.strip('<> ')
print(u)
print( result)
result = result.replace('spam', 'spam and egg')
print( result)
lst = result.split()
print( lst)
print('----다시 합치기--- ')
print(':'.join(lst))

#반복적 문구 작성

names= ['aaa', 'bbb', 'ccc']
for nm in names:
    print('hello {0} hey.'.format(nm))
    print('='*40)

