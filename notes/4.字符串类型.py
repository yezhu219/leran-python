# 字符串类型

'''
    字符串截取
    使用下标
'''

str1 = 'test string'

print(str1[1])
print(str1[2:6])
print(str1[0:6])
print(str1[:6])  # 省略0

# 字符串运算符

'''
    + 拼接字符串
    * 重复字符串
    [n] 通过下标获取字符串
    [n:n] 获取指定范围下标的字符串
    in  成员运算符  返回布尔值  如果字符串中包含给定的字符返回 True
    not in  成员运算符 返回布尔值  如果字符串中不包含给定的字符返回 True
    % 格式字符串
'''

print('字符串%s格式化测试%s' % ('bac', 'bbb'))
print('字符串%s格式化测试%d' % ('bac', 123))

'''
    字符格式化符号
    
    %s 格式化字符串
    %d 格式化数字
    %u 格式化无符号整型
    %o 格式化无符号八进制数
    %c 格式化字符及其ASCII码
    
    
    三引号自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的
'''

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

'''
    f-string 称之为字面量格式化字符串，是新的格式化字符串的语法
'''
name = '张三'
print(f'名字：{name}')

obj = {
    'id': 1,
    'name': '测试'
}
print(f"{obj['id']}----{obj['name']}")


# 内建函数

'''
    capitalize()  将字符串的第一个字母转换为大写
    encode(encoding='UTF-8',errors='strict') 
    以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace
    bytes.decode(encoding="utf-8", errors="strict")
    
    join(seq) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    
'''

testStr = 'test str'
print(testStr.capitalize())
print('.'.join(testStr))

estr = '编码'
encodestr = estr.encode(encoding='gbk', errors='strict')
print(encodestr, 'encodestr---')
