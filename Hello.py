# -*- coding: utf-8 -*-
# print ('Please enter your Weight: ')
# weight = (float)( input())
# print ('Please enter your Height: ')
# height = (float)( input())
#
# ratio = (weight / height) * (weight / height)
#
# if ratio < 18.5:
#     print ('Too light!')
# elif 25 > ratio >= 18.5:
#     print ('formal')
# elif 28 > ratio >= 25:
#     print ('More Heavy')
# elif 32 > ratio >= 28:
#     print ('Fatter')
# else:
#     print ('Heavily fat!')
# print ("hello world!")
# print 2.5 + 10.0/4
# a = 'python'
# print 'hello,', a or 'world'
# b = ''
# print 'hello,', b or 'world'
# L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
# L.insert(2,'Paul')
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# L.pop(2)
# L.pop(2);
# print L;
# L = ['Adam', 'Lisa', 'Bart']
# L[-1] = 'Adam'
# L[0] = 'Bart'
# print L
# t= (0,1,2,3,4,5,6,7,8,9)
# print t
# t = ('Adam',)
# print t
# d = {
#     95: 'Adam',
#     85: 'Lisa',
#     59: 'Bart'
# }
# d['Paul'] = 72
# print d;

#Function1 in Python
# L = []
# x = 1
# while x <= 100:
#     L.append(x*x);
#     x = x + 1
# print sum(L)

#Function2 in Python
# def square_of_sum(L):
#     sum = 0
#     for x in L:
#         sum = sum + x * x
#     return sum
# print square_of_sum([1,2,3,4,5])
# print square_of_sum([-4,0,5,15,25])

#Function3 in Python
# import math
#
# def quardratic_equation(a,b,c):
#     t = math.sqrt(b * b - 4 * a * c)
#     return (-b + t) / (2 * a), (-b - t) / (2 * a)
# print quardratic_equation(2,3,0)
# print quardratic_equation(1,-6,5)

#切片
# L = range(1,101)
#
# print L[0:10]
# print L[2::3]
# print L[5:50:5]

#切片2
# L = range(1, 101)
#
# print L[-10:]
# print L[-46::5]

# 切片3
# 编写一个函数，可以把字符串的首字母变成大写
# def firstChartUpper(s):
#     return s[0].upper() + s[1:]
#
# print firstChartUpper('hello')

# L = range(1, 101)
# for i in L:
#     if i % 7 == 0:
#         print i

#python高阶函数
# import math
# def sA(x,y,f):
#     return f(x) + f(y)
#
# print sA(25,9,math.sqrt)

# def format_name(s):
#     return s[0].upper() + s[1:].lower()
#
# print map(format_name,['adam', 'LISA', 'barT'])

# def f(x,y):
#     return x*y
#
# print reduce(f,[2,4,5,7,12])

# import math
#
# def is_sqrt(x):
#     r = int(math.sqrt(x))
#     return r*r == x
# print filter(is_sqrt, range(1,101))

# def cmp_ignore_case(s1,s2):
#     u1 = s1.upper()
#     u2 = s2.upper()
#     if u1 < u2:
#         return -1
#     if u1 > u2:
#         return 1
#     return 0
#
# print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# 匿名函数 lambda

#Moudle
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 'a test moudle'
#
# __author__ = 'Jacob lee'
#
# import sys
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print ('Hello, world!')
#     elif len(args) == 2:
#         print ('Helllo, %S!' % args[1])
#     else:
#         print ('Too many argumnts!')
#
# if __name__=='__main__':
#     test()

# __slots__
# class Student(object):
#     pass
#
# s = Student()
# s.name = 'Michale'
# print (s.name)

# class Student(object):
#     __slots__ = ('name', 'age')
#
# s = Student() #创建新的实例
# s.name = 'Michale'
# s.age = 25

# class Screen(object):
#     @property
#     def width_heigth(self, width, height):
#         return self.width_heigth
#     @width_heigth.setter
#     def width_height(self, width, height):
#         self._width = width
#         self._height = height

#读文件
# f = open('Users/Jacob/text.txt', 'r')
with open('path/to/file', 'r') as f:
    print (f.read())

#读取二进制文件 图片、视频等
f = open('Users/jacob/test.jpg', 'rb')
f.read()

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
f = open('Users/jacob/gbk.txt', 'r', encoding='gbk')
f.read()