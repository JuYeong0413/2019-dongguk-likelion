# -*- coding: utf-8 -*-
print("Hello Python")

# 파이썬이 갖고 있는 자료형
# 자료형 : 어떤 데이터의 특성을 담을 수 있는 데이터의 종류
# integer, float, string, boolean, list, dictionary, tuple, set, bytes

int_variable = 5
print(int_variable)

float_var = 2.5
boolean_var = True

print(type(boolean_var))
print(type(int_variable))

string_var = "hello world"
print(type(string_var))

my_list = ["hello", True, 2.5, []]
print(my_list)

my_tuple = ("hello", False, 1, (), [])
# 리스트와 튜플의 차이는 리스트는 대괄호로 되어있고 튜플은 그냥 괄호로 되어있음
# 집합 자료형으로 여러개의 데이터를 담을 수 있다는 건 동일하다

my_dictionary = {
    "name": "철수",
    "age": 25
}

# string
my_string = "python"
my_string2 = 'django'
# 파이썬에서는 차이가 없다. 둘 다 선언해도 된다
# 문자열은 리스트와 비슷한 특징을 갖는다 : 순서가 있고, 수정 삭제 가능

# 인덱싱
print(my_string[2]) # t
print(my_string[-2]) # -1번째는 뒤에서부터 오게 됨 o

# 슬라이싱
print(my_string[2:5]) # tho
print(my_string[:5])
print(my_string[1:])
print(my_string[::-1]) # 처음부터 끝까지 역순으로 출력해라

# 이스케이프 문자
# \t \n \" \'

escape_string = "\"hello\tworld"
print(escape_string)

r"\t\n\s"

print(len(escape_string))

my_str = "wowowow"
print(my_str * 100)

my_str2 = "hohoho"
print(my_str + my_str2)

fruit = "apple"
print(fruit.capitalize()) # 앞글자만 대문자로 Apple

print(fruit.replace('pl', 'ppl'))

print('a' in fruit)
print('a' not in fruit)

# 집합 자료형
# list
my_list = ["돌맹이", True, [1, 2, 3]]
my_list1 = list()
# 같은 것임, 위에 것을 많이 쓴다
# 리스트 함수는 형변환

print(my_list1)
print(my_list[1])
print(my_list[2][-1])

del my_list[2]
print(my_list)

num_list = [5, 3, 10, 7, 3]
num_list.sort()
print(num_list)

num_list.append(5)
# insert, pop, remove

# tuple
my_tuple = ('hello', True, (1, 2, 3), [])
# tuple은 안에 있는 값을 수정하거나 삭제 불가능, 중요한 데이터(시리얼 넘버)가 들어감

print(my_tuple[0])

my_dict = {
    "name": "철수",
    "age": 25,
    "phone": "112"
}

my_dict.get('name')
my_dict["address"] = "중구 필동 3가"
del my_dict["address"]
print(my_dict)

print(list(my_dict.keys()))
print(tuple(my_dict.keys()))
print(my_dict.values())
print(my_dict.items())

for key, value in my_dict.items():
    print(key, value)

# 조건문
if 3:
    print("hello")

# True, "값", ['hello], 3
# False, "", [], (), {}, 0

# 관계연산자 ==, !=, <=, >=, >, <
print(1==1)
print(1!=1)

# 논리연산자 and, or, not
print(True and True)

document_score = 80
interview_score = 90

if document_score >= 80:
    if interview_score >= 85:
        print("축하합니다 합격!")
    else:
        print("면접 탈락하셨습니다.")
else:
    print("서류 탈락하셨습니다.")

# 반복문
my_range = range(1, 5)
print(my_range)

for num in my_range:
    print(num)
    
my_range2 = range(5)
print(my_range2)

my_range3 = range(1, 6, 2) # 1부터 5까지 2개씩 건너뛰면서 출력하겠다
print(my_range3)

# 1부터 100까지 더하기
sum1 = 0
for num in range(1, 101):
    sum1 += num
    
print(sum1)

my_str = "python"
for alphabet in my_str:
    print(alphabet)
    
for alphabet in reversed(my_str):
    print(alphabet)

for i, alphabet in enumerate(my_str):
    print(i, alphabet)

var1 = "철수"
var2 = "영희"
print("안녕 {}야 나는 {}라고해".format(var1, var2))
print("안녕 %s야 나는 %s라고해" %(var1, var2))

for i, alphabet in enumerate(my_str):
    print("{}번째 알파벳: {}".format(i, alphabet))

# while
count = 0
while True:
    count += 1
    if count == 10:
        break
    # print('hello')
print(count)

# 함수
def hello(name):
    print("안녕 %s야" % name)
    
hello("철수")

def mul(num1, num2):
    return num1 * num2

result = mul(6, 5)
print(result)
