# 练习 1：温度转换
# 输入摄氏度，返回华氏度。公式：F = C × 9/5 + 32
def c_to_f(c):
    f = c * 9 / 5 + 32
    return f

c = int(input('请输入摄氏度'))
f =c_to_f(c)
print("华氏度是" , f)


# 练习 2：BMI 计算
# 输入身高(m)和体重(kg)，返回 BMI 值。公式：体重/身高²
def bmi(height, weight):
    bmi = weight / (height**2)
    return bmi

h = float(input("请输入身高(米)"))
w = float(input("请输入体重(kg)"))
BMi = bmi(h,w)
print("他的BMI是", BMi)


# 练习 3：判断奇偶
# 输入整数，返回 "奇数" 或 "偶数"
def odd_or_even(n):
    a = n % 2 
    if a == 0 :
        return "偶数"
    else :
        return "奇数"

a = int(input('请输入整数'))
b = odd_or_even(a)
print(b)

# 练习 4：字符串反转
# 输入字符串，返回反转后的结果
def reverse_str(s):
    return s[::-1]

text = input("请输入字符串：")
print("反转后：",reverse_str(text))








# 练习 5：列表求和与平均值
# 输入数字列表，返回 (总和, 平均值)
def sum_avg(numbers):
    tolal = sum(numbers)
    avg = tolal/len(numbers)
    return tolal,avg

my_list = [10,20,30,40]
s,a = sum_avg(my_list)
print("总和:",s,"平均值：",a)


# 练习 6：类型转换判断
# 输入任意值，返回其类型名称字符串（如 "int", "str", "float"）
def get_type(value):
    return type(value).__name__

print(get_type(100))
print(get_type("hello"))
print(get_type("3.14"))

# 练习 7：简单计算器
# 输入两个数和运算符(+ - * /)，返回计算结果
def calculator(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    else:
        return "不支持的运算"
    
x = float(input("第一个数："))
y = float(input("第二个数："))
op = input("运算符(+ - * /):")
print("结果：",calculator(x,y,op))

 

# 练习 8：FizzBuzz（经典题）
# 输入整数 n，如果能被3整除返回"Fizz"，被5整除返回"Buzz"，同时被3和5整除返回"FizzBuzz"，否则返回 n
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    if n % 5 == 0 and n % 3 != 0:
        return 'Buzz'
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    else:
        return n
    
n = int(input("请输入整数n"))
print(fizzbuzz(n))

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:  # 同时满足
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

num = int(input("请输入整数："))
print(fizzbuzz(num))


# 练习 10：类型转换陷阱
# 输入两个字符串数字（如 "5" 和 "3"），返回它们的：和（整数）、差、乘积、商（浮点数）
def str_calculate(a, b):
    sum = a + b
    de = a - b 
    c = a * b
    d = a/b
    return sum,de,c,d

a = int(input("请输入第一个数字"))
b = int(input("请输入第二个数字"))
h,c,j,s =str_calculate(a,b)
print(f"和：{h},差：{c},积：{j},商:{s}")


def str_calculate(a, b):
    # a 和 b 是字符串，比如 "5" 和 "3"
    x = int(a)
    y = int(b)
    he = x + y
    cha = x - y
    ji = x * y
    shang = x / y
    return he, cha, ji, shang

s1 = input("第一个数字：")
s2 = input("第二个数字：")
h, c, j, s = str_calculate(s1, s2)
print(f"和：{h}，差：{c}，积：{j}，商：{s}")
