# -------------------
strings = "abcdefghijklmnopqrstuvwxyz"
print(strings[1]) # b
print(strings[-2]) # y
print(strings[1:4:1]) # 1-3까지의 글자 가져오기 # bcd

# -------------------

print(dir(str))
print(help(str.strip))

# msg의 좌우 공백을 제거하고 모두 대문자로 치환하고자 하는 경우
msg = " HelloWorld "
msg = msg.strip().upper() # 메서드 연쇄 호출 가능
print(msg)

# -------------------
ar = [100, 200, 300]
doublearray = [ar, 300, 400] # ar을 참조하고 있음
doublearray[0] # ar이 됨

ar[0] = 0 # ar 원본을 바꿨더니
print(doublearray[0]) # 변경되어서 나옴

doublearray[0][0] = 2000 # list 안에 있는 list의 데이터를 변경하면 원본이 변경
print(ar)

# ------------------
datas = ["Hi", "hello", "Morning", "afternoon"]
print(datas)
# datas.sort(key=str.upper, reverse=True)
datas.sort(key=lambda s: s.upper(), reverse=True) # key에 설정된 함수 가지고 데이터 변환해서 정렬
print(datas)

datas = ["Hi", "hello", "Morning", "afternoon"]
print(sorted(datas))

# -----------------
from time import time
li = []
start = time()
for i in range(10**2):
    li.append(i)
end = time()
listime = end - start

print(f"list를 이용한 경우: {listime}")

from collections import deque
deq = deque()
start = time()
for i in range(10**2):
    deq.append(i)
end = time()
deqtime = end - start

cnt = 0
if deqtime > listime:
    cnt = cnt + 1
print(cnt)
print(f"list를 이용한 경우: {listime}")
print(f"deque를 이용한 경우: {deqtime}")

# deque ----------
history = deque(maxlen = 3)
history.append("축구")
history.append("야구")
history.append("배구")
history.append("농구") # maxlen을 설정해뒀기 떄문에 저장 안됨
# print(dir(deque)) #함수 확인
for imsi in history:
    print(imsi)

# Tuple ---------
tp = (1, 2, 3)
for imsi in tp:
    print(imsi)
# tp[0] = 200 #tuple은 재할당 안됨