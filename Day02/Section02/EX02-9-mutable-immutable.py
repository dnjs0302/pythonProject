'''
mutable - 메모리 값(주소값)을 변경 가능 객체
    리스트(list), 세트(set), 딕셔너리(dict)
'''
me = [1,2,3]
print(id(me)) # 실행하면 값이 바뀜
me.append(4)
print(id(me)) # 2355627622016

'''
immutable - 메모리 값 변경 불가
    정수(int), 실수(fload), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me)) #1734035963520
me += 1 #me = me + 1
print(id(me)) #1734034942576

#튜플테스트
thistuple = ("피카츄", "라이츄", "파이리")
print(id(thistuple))
thiscast = list(thistuple) #casting or 형변환 : 타입을 바꿔줌
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(id(thistuple))