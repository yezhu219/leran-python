import math
import random

# 数字类型

'''
    数字类型转换
    int() 转换为整数
    float()  转换为浮点数
    complex() 转换为复数
    
    常量 
    pi 圆周率
    e  数学常量e
'''

a = '10'
print(int(a))
print(float(a))
print(complex(a))

# print(a/1)  # 报错


'''
    数学函数
    abs(x)  返回绝对值
    ceil(x)  向上取整
    floor(x) 向下取整
    math.log(x)  
    max(x,y,z) 返回最大值
    min(x,y,z) 返回最小值 
    round(x)  四舍五入
'''

print(abs(-40))
print(math.log(40))
print(max(1, 2, 3, 4))
print(min(1, 2, 3, 4))
print(round(3.14))


'''
    随机数 
    
    random() 随机生成[0,1]之间实数
    choice() 
'''
print(random.random())
print(random.choice(range(10)))
print(math.e)
print(math.pi)
print(math.sin(30))