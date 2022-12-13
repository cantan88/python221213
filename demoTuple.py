# demoTuple.py
tp =( 1, 2, 3)
print( len(tp))
print( type(tp))
print( tp[0])

# 함수 정의
def calc(a,b):
    return a+b, a*b

result = calc(3,4)
print(result)    
print(result[0])

print('id: %s, name: %s' % ('kim', '김유신') )

args = (5,6)
print( calc(*args))

a = (10, 20, 30)
b = list(a)
b.append(40)
print(b)

print('---dict---')
device = {'아이폰':5, '아이패드':10, '윈도우':20}
print( type(device))
print( device)

# 디버길할 때 중단점(break point)

for itm in device.items():
    print(itm)

for k,v in device.items():
    print(k,v)

# 검색
print( device['아이폰'])

# 입력
device['맥북'] = 15

# 수정
device['아이폰'] = 6

# 삭제
del device['윈도우']
print( device)