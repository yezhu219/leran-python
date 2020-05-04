# 运算符

"""
    运算符分类
    1.算数运算符
    2.关系运算符
    3.赋值运算符
    4.逻辑运算符
    5.位运算符
    6.成员运算符
    7.身份运算符
    8.运算符优先级
"""

# 算数运算符

'''
    + 加
    - 减
    * 乘
    / 除
    % 取余
    ** 幂
    // 向下取整
    
'''

a = 100
b = 3

print(a + b, '+')
print(a - b, '-')
print(a * b, '*')
print(a / b, '/')
print(a % b, '%')
print(a ** b, '**')
print(a // b, '//')

# 比较运算符
'''
    == 等于 不会默认转换数据类型
    >= 大于等于
    <= 小于等于
    != 不等于
    >  大于
    <  小于
    
    逻辑运算符不会进行默认数据转换
'''
c = '3'
print(b == c, '等于')
# print(b >= c, '>=')  # 报错


# 赋值运算符
'''
    = 
    +=
    -=
    *=
    /=
    %=
    **=
    //=
    :=   海象运算符
'''

l = len('12112312')
print(l, 'l')

# 逻辑运算符

'''
    and  与
    not  非
    or   或
'''

# 成员运算符

'''
    in 
    not in
'''
num1 = '3'
num2 = '8'
arr = ['1', '2', '3', '4']

if num1 in arr:
    print(num1, 'is in arr')
else:
    print(num1, 'is not in arr')

if num2 not in arr:
    print(num2, 'is not in arr')
else:
    print(num2, 'is  in arr')

# 身份运算符

'''
    身份运算符用于比较两个对象的存储单元
    is 
    not is
    
    id()函数用于获取对象内存地址
    
    is 与 == 区别：

    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
if a is b:
    print('相同')
else:
    print('不同')

print(id(a), id(b), '内存地址')

list1 = [1, 2, 3]
list2 = list1
list3 = list1[:]
print(list1 == list2)
print(list1 is list2)
print(list3 == list1, list3 is list1)
