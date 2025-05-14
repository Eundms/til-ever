# 올바른 tuple 생성 방식
x = {'a': 10, 'b':20}

# range
cnt = 0
for i in range(1, 10, 1):
    cnt+=1
print(cnt)

# 숫자 배열 -> 문자 배열
a = list(map(str, [4.7, 3.5, 2.9]))
print(a)

# scores 배열의 평균, 최소, 최대
scores = list(map(int, input().split()))

for score in scores:
    if score < 0 or score > 100 :
        print("잘못된 점수")
        exit()
average = sum(scores) / len(scores)
if average >= 80:
    print("합격")
else:
    print("불합격")

# 트리 모양
x = int(input())
for i in range(1, x+1):
    print((2 * i - 1) * '*')

# prices
prices = list(map(int, input().split(';')))
prices.sort(reverse = True)

for price in prices:
    print(f"{price:>9,}")


# file 오픈
filename = 'abc.txt'

def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j] :
            return False
        i+=1
        j-=1
    return True

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if is_palindrome(line):
            print(line)
