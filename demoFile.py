# domoFile.py

for x in range(1,6):
    print(x, '*', x, '=', x*x)

for x in range(1,6):
    print(x, '*', x, '=', str(x*x).rjust(3))

for x in range(1,6):
    print(x, '*', x, '=', str(x*x).zfill(3))    

print('{0:x}'.format(10))
print('{0:b}'.format(10))
print('{0:e}'.format(4/3))
print('{0:f}'.format(4/3))
print('{0:.2f}'.format(4/3))
print('{0:,}'.format(150000))


f = open(r'c:\work\demo.txt','wt',encoding ='utf-8')
f.write('첫번째\n두번째\n세번째\n')
f.close()

f = open(r'c:\work\demo.txt','rt',encoding ='utf-8')
result = f.read()
print(result)
print( f.tell())

#처음으로 리셋
f.seek(0)
lst = f.readlines()
print(lst)

for item in lst:
    print(item, end='')

f.seek(0)
print('---한줄씩---')
print( f.readline(), end='')
print( f.readline(), end='')

f.close()