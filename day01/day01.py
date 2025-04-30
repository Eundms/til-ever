import keyword

print("Hello Python")

print(dir(10))
help("안녕".__add__)
help(int.__add__)

# 안녕하세요
print("안녕" + "하세요")
print("안녕".__add__("하세요"))

# 안녕안녕안녕
print("안녕"*3)
help("안녕".__mul__)

# 파이썬 예약어
import keyword
print(keyword.kwlist)

# 파이썬에서 문자열 str이라고 하지만 str은 예약어 아님
print(str.upper("hello"))
# str = 10 # 이곳에서 기능이 바뀜
# print(str.upper("hello")) 여기서 에러 남


# 파이썬 여러개 설치되어 있어서 안 될 수도 있으므로 실행되는 환경을 확인해볼것
import sys
print(sys.path)

# 리터럴 프로그램 끝까지 남아 있음
print(1.0 - 8.0 == 0.2) # false

cnt = 1
temp = 0.01
while temp < 0.1 :
    temp += 0.01
    cnt += 1
    print(temp)
print(cnt)

# 파이썬은 위치를 기억하지 데이터를 직접 나타내지 않는다


# list : 열
# tuple : 행, 변경 불가능(Immutable)
# NaN : 가리키는 데이터가 없다

data = [1, 2, 3] # 리스트 생성
# list는 __iter__을 가지고 있으므로 for 사용 가능
print(dir(data))
for imsi in data:
    print(imsi)

# data = 10
# print(dir(data))
# for imsi in data:
#     print(imsi)


# 실수 외 문자열은 for을 사용할 수 있는지 확인
# 10.8, "Hello World"
data = ["KIA", "HYUNDAI", "DAEWOO"]
for d in data:
    print(d)

pan = 10 > 3
print("pan:", pan)

pan = 10 == 3
print("pan:", pan)

date = '2019-01-01'
print(date == '2019-01-01')
print(date == '2018-12-31')

#문자 크기 비교는 첫글자부터
print("레드밸벳" > "블랙핑크")

# 소문자가 대문자보다 큼
print("BlackPink" > "blackPink")

# 음수 구하기

year = 2025
if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    print (year, "는 윤년입니다.")
else:
    print(year, "는 윤년이 아닙니다.")
