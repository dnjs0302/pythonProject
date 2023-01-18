'''
Casting
    변수에 유형을 지정하려는 경우 캐스팅으로 가능
'''
# 정수형
x = int(1)
print(x)
y=int(2.8)
print(y)
z = int("3")
print(z)
print(type(z))
print(x+z)

#실수형
x = float(1)
print(x)
z = float("3")
print(z)

#문자형
x = str(1)
y = str(2)
print(x)
print(x+y)

# 아스키코드 변환
a = ord('A') #A라는 문자를  ord(아스키코드)로 변환
print(a)
b = chr(65) #65라는 아스키코드를 chr 문자로 변환
print(b)
