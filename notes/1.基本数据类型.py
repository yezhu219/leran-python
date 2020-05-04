# 单行注释

"""
    多行注释
    多行注释
"""

print('test 注释')

# 多行连接
langstr = 'qqqqqq' + 'sdfsdfsd' + \
          'sdfsadfsad'

print(langstr)

# 赋值

'''
    多个变量赋值
'''
a = b = c = 1
a, b, c = 1, 2, 'ccc'
print(a, b, c)

# 数据类型

# 数字
'''
    数字是不可改变数据类型，重新赋值是重新开辟内存 

数字类型

    整型： int
    浮点型： float
    长整型： long
    复数：complex
'''
numberA: int = 100
numberB = 200
print(numberA, 'numberA')
print(numberB, 'numberB')

# 字符串
'''
    + 是拼接
    * 是重复
    索引正向从0开始
    反向从-1开始到-字符串长度
'''
test_str = 'test hello world'
splice_str = test_str[0:4]


print(test_str, '字符串接', splice_str)
print(test_str+splice_str, '+号')
print(splice_str*2, '*操作')


# 列表
'''
    有序数据集合
'''
nameList = ['tony', 'tim', 'zhou']

print(nameList, '列表')

# 元组

'''
    相当于只读列表，不能修改
'''

nameTuple = ('tony', 'tim', 'zhou')
print(nameTuple, '元组')


# 字典

'''
    无序数据集合
    键值对形式存储

'''
names = {
    'id': 1,
    'name': 'tony'
}

print(names, '字典')


# 数据类型转换
'''
    int(x)       将x转换为一个整数
    long(x)      将x转换为一个长整数
    float(x)     将x转换到一个浮点数
    complex(x)   创建一个复数
    str(x)       将对象 x 转换为字符串
    repr(x)      将对象 x 转换为表达式字符串
    eval(str)    用来计算在字符串中的有效Python表达式,并返回一个对象
    tuple(s)     将序列 s 转换为一个元组
    list(s)      将序列 s 转换为一个列表
    set(s)       转换为可变集合
    dict(s)      创建一个字典。d 必须是一个序列 (key,value)元组。
    ord(s)       将一个字符转换为它的整数值
'''