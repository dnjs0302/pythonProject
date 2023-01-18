'''
print() 함수 사용법
    sep : 출력할  value의 구분 문자
    end : value 출력 후 출력할 문자 (기본값 '\n')
    file : 출력 방향 지정
'''
print('재미있는', '파이썬') #sep=' '게 생략되어있다고 봄
print('Python', 'Java', 'C', sep=',')

print("안녕", end='')
print("하세요")
print("안녕\n", end='')
print("하세요")

#콘솔에만 출력이 가능한게아니라 파일에도 출력가능
fos = open('sample.py', mode='wt') #파일을 만들어 오픈했다 wt : write text
print('print("Hello World")', file=fos) #파일에 print("Hello World")를 담았다
fos.close() #파일을 클로즈했다