'''
Set
    순서가 없다. 순서 구별하지 않음
    변경할 수 있다
    인덱싱되지 않는 컬렉션(인덱스값이 없음)
    중복값 없다
'''
thisset  = {"피카츄", "라이츄", "파이리"}
# 실행할 때마다 순서가 변경
print(thisset)
# 항목 가져오기 : this set 길이만 반복하여 가져옴 : 반복문
for x in thisset:
    print(x)

#값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거(동일하게 리무브하면 에러남)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
thisset.remove("피카츄")
print(thisset)
# 항목제거(디스카드는 동일한것 삭제해도 에러 안남)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.remove("피카츄")
print(thisset)
# 항목제거(랜덤으로 삭제)
thisset.pop()
print(thisset)

# 비우기
thisset.clear()
print(thisset)