# -*- coding: utf-8 -*-
# 11주차 과제
# 1. 문자열 my_str = "wow hello world"의 길이를 구해보시오
my_str = "wow hello world"
print(len(my_str))

# 2. print 함수를 이용해서 아래와 같이 출력하시오
#    \nhelloworld\s
print(r"\nhelloworld\s")

# 3. 화면에 '#' 을 1000번 출력하시오
print('#' * 1000)

# 4. 문자열 '30' 을 정수, 실수로 변환해보시오
str_30 = '30'
print(int(str_30)) # 정수로 변환
print(float(str_30)) # 실수로 변환

# 5. "Hello world"에서 "world"만 슬라이싱 해보시오
my_str = "Hello world"
print(my_str[6:])

# 6. "Django" 문자열을 거꾸로 출력해보시오
my_str = "Django"
print(my_str[::-1])

# 7. "010-9790-2095"에서 '-'만 제거하고 출력하시오
phone_number = "010-9790-2095"
print(phone_number.replace("-", ""))

# 8. 다음주소 "https://dongguk.likelion.org"에서 "https://" 만 제거해보시오
my_domain = "https://dongguk.likelion.org"
print(my_domain.replace("https://", ""))

# 9. 다음 문자열 "dsjflhdsfad" 에서 "sjfl"만 슬리이싱 해보시오
my_str = "dsjflhdsfad"
print(my_str[1:5])

# 10. 다음 문자열 "Apple"을 모두 대문자, 소문자로 각각 출력하시오
apple_str = "Apple"
print(apple_str.upper()) # 대문자로 출력
print(apple_str.lower()) # 소문자로 출력

# 11. 다음 리스트에서 "Apple"만 삭제하시오 [“Banana”, “Apple”, “Orange”]
fruits = ["Banana", "Apple", "Orange"]
del fruits[1]
print(fruits)

# 12. 다음 튜플을 리스트로 변환하시오 (1, 5, 7, 9)
my_tuple = (1, 5, 7, 9)
print(list(my_tuple))

# 13. 다음 항목을 딕셔너리로 선언하세요
#     제목 – 간장게장, 내용 – 밥도둑, 조회수 - 50
post = {
    '제목' : "간장게장",
    '내용': "밥도둑",
    '조회수': 50
}

# 14. 13번에서 생성한 딕셔너리에 글쓴이 – 장성원 을 추가해보시오
post['글쓴이'] = "장성원"

# 15. 리스트 [30, 40, 50, 60, 70]중 50이 넘는 값만 출력하시오 (조건문 사용)
my_list = [30, 40, 50, 60, 70]
for number in my_list:
    if number > 50:
        print(number)

# 16. 13번에서 생성한 딕셔너리에 key값만 반복문으로 출력하시오
for key in post.keys():
    print(key)

# 17. 13번에서 생성한 딕셔너리에 value값만 반복문으로 출력하시오
for value in post.values():
    print(value)

# 18. 13번에서 생성한 딕셔너리에 key와 value를 하나의 반복문으로 아래와 같은 형태로 출력하시오
#     제목은 간장게장이다
#     내용은 밥도둑이다
#     조회수는 50이다
#     글쓴이는 장성원이다
for key, value in post.items():
    print("{}은(는) {}이다".format(key, value))

# 19. 두 수의 합과 곱을 리턴하는 다중리턴 함수를 만들 하나의 변수에 튜플형태로 담아서 반복문으로 출력하시오.
result_tuple = ()

def function(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    
    return sum, mul

for result in function(3, 4):
    result_tuple += (result,) # 튜플로 담기

# 출력
for result in result_tuple:
    print(result)

# 20. N 번째 피보나치 수를 알 수 있는 함수를 구현하시오 (선택)
def fibo(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibo(num - 2) + fibo(num - 1)

print(fibo(10))
