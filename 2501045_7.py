# 과제 11
num1 = map(int,input('<과제 11번> 임의의 숫자 5개 입력 : ').split())
list_num1 = list(num1)
print(list_num1)

num2 = int(input('끝에 추가할 숫자 1개 입력 : '))
list_num1.append(num2)
print(list_num1)


# 과제 12
num1 = map(int,input('<과제 12번> 임의의 숫자 5개 입력 : ').split())
list_num1 = list(num1)
del list_num1[-2:]
print(list_num1)


# 과제 13
num = map(int,input('<과제 13번> 임의의 숫자 5개 입력 : ').split())
for index, value in enumerate(num, start=101):
    print(index, value)


# 과제 14
a = [10, 20, 30, 40, 30, 20, 10]
b = a.count(20)
print("20의 개수는 : ",b)


# 과제 15
num = list(map(int,input('<과제 15번> 임의의 숫자 10개 입력 : ').split()))
max_num = max(num)
min_num = min(num)
print(min_num, ' and ', max_num)


# 과제 16
num = list(map(int,input('<과제 16번> 임의의 숫자 10개 입력 : ').split()))
num.remove(max(num))
num.remove(min(num))
print(sum(num))


# 과제 17
a = [10, 20, 30, 40, 30, 20, 10]
a.remove(20)
a.remove(20)
print(a)


# 과제 18
a = [i for i in range(1,6)]
print(a)


# 과제 19
a = [i for i in range(1,21) if i % 2 == 1]
print(a)


# 과제 20
while True:
    a, b = map(int, input("<과제 20번> 1부터 20 사이의 정수 2개를 입력하세요 (첫 번째 값 < 두 번째 값): ").split())

    if 1 <= a <= 20 and 1 <= b <= 20:
        if a < b:
            break
        else:
            print('(첫 번째 값 < 두 번째 값)이 되게 다시 작성하세요')
    else:
        print("1부터 20 사이의 정수 2개를 입력하세요")
    
c = [2**i for i in range(a,b+1)]
del c[1]
del c[-2]
print(list(c))


# 과제 21번
str = 'Hello, world!'
str = str.replace('Hello', 'Hi')
print(str)


# 과제 22번
string = input('<과제 22번> 임의의 문자 4개 입력 : ')
string = " / ".join(string)
print(string)


# 과제 23번
name = input('<과제 23번> 본인의 성을 영어로 입력 : ')
name = name.rjust(10).lower()
print(name)


# 과제 24번
price = list(map(int,input('<과제 24번> 물품 가격 여러 개 입력 : ').split(';')))
price.sort(reverse=True)

for i in price:
    print("{0:9}".format(i))