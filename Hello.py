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
L = range(1, 101)

print L[-10:]
print L[-46::5]
