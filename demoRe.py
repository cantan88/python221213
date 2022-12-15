# demoRe.py

import re

#숫자 th문자열 패턴

result = re.search('[0-9]*th', ' 35th')
print(result)
print( result.group() )

# result = re.match('[0-9]*th', ' 35th')
# print( result)
# print( result.group())

result = re.search('apple', 'this is apple')
print( result.group())

# result = re.match('apple', 'this is apple')
# print( result.group())

s = "Apple is big company and apple is very delicious"
c = re.compile('apple', re.I)
print( c.findall(s))


print('---연도---')
result = re.search( "\d{4}","올해는 2022년")
print( result.group())

result = re.search( "\d{5}","우리동네는 52300")
print( result.group())
