# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:43:44 2017

@author: hsing1
"""

import os
import subprocess
import sys
import itertools
import re
import shelve

print(len(sys.argv))
print(sys.argv[0])

"""
To activate virtual env : .\myenv\Scripts\activate
To launch python for Django : python .\mysite\manage.py shell
To get help : python .\Django\mysite\manage.py help

elif (case == 'django_template'):
    from django import template
    t = template.Tamplate('My name is {{ name }}.')

    c = template.Context({'name' : 'Nige'})
    print (t.render(c))

    t = Template('Hello, {{ name }}')
    for name in ('John', 'Juli', 'Pat'):
        print (t.render(Context({'name' : name}))

    #access to object attribute
    from django.template import Template, Context
    import datetime
    d = datetime.date(2017, 5, 2)
    t = Template('The mopnth is {{ date.month }} and the year is {{ date.year }}.')
    c = Context({'date' : d})
    t.render(c)


    #use custom class
    class Person(object):
        def __init__(self, first_name, last_name):
	    self.first_name, self.last_name = first_name, last_name
    t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
    c = Context({'person' : Person('John', 'Smith')})
    t.render(c)

    #refer to method of objects
    t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
    t.render(Context({'var' : 'hello'}))
    t.render(Context({'var' : '123'}))

    #access to list index
    t = Template('Item 2 is {{ item.2 }}.')
    c = Context({'items' : ['apples', 'bananas', 'carrots']})
    t.render(c)
"""
case = sys.argv[1]
print ("case = {}".format(case))

if (case == 'string'):
    if (1):
        x = "Item One : {} Item Two {}".format("dog", "cat")
        print(x)
        x = "Item One : {x} Item Two {y}{y}".format(x = "dog", y = "cat")
        print(x)
        x = 'Item One : {x} Item Two {y}{y}'.format(x = "dog", y = "cat")
        print(x)

    if (0):
        s = "Django"
        print (s[::-1]) #print string reversely

elif (case == "variable"):
    if 1:
        s = "GLOBAL VARIABLE"
        def my_func():
            x = 10
            print(locals())
            print(locals()['x'])
        my_func()

        print(globals()['s'])


elif (case == 'regx'):
    import re
    if (1):
        print(re.findall('match', 'test phrase match in match middle'))

        def multi_re_find(patterns, phrase):

            for pat in patterns:
                print("searching for pattern {}".format(pat))
                print(re.findall(pat, phrase))
                print("\n")

        test_phrase = 'sdsdfsdfsdfd...sdfsd...ddd.....ssddddsssddd123'
        test_patterns = ['sd+', 'sd?', 'sd*', 'sd{1,3}', '[a-z]+', r'\d+', r'\s+', r'\w+']

        print(multi_re_find(test_patterns, test_phrase))

    if (0):
        text = 'This is a string with term1, but not the other!'
        match = re.search('term1', text)
        print(type(match)) #<class '_sre.SRE_Match'>
        print(match.start())

        email = 'user@gmail.com'
        split_term = '@'
        print(re.split(split_term, email))
    if (0):
        patterns = ['term1', 'term2']

        text = 'This is a string with term1, but not the other!'

        for pattern in patterns:
            print("I'm searching for:" + pattern)

            if re.search(pattern, text):
                print("MATCH!")
            else:
                print("NO MATCH!")

elif (case == 'class'):
    if (1):
        class Book():
            def __init__(self, title, author, pages):
                self.title = title
                self.author = author
                self.pages = pages

            def __str__(self):
                return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

            def __del__(self):
                print("A book is delete")

        b = Book("Python", "jose", 200)
        print(b)

    if (0):
        class Animal():
            def __init__(self):
                print("ANIMAL CREATED")

            def whoAmI(self):
                print("ANIMAL")

            def eat(self):
                print("EATING")

        class Dog(Animal):

            def __init__(self):
                Animal.__init__(self)
                print("DOG CREATED")

            def bark(self):
                print("WOOF")

            def eat(self):
                print("DOG EATING")


    if (0):
        class Circle():
            pi = 3.14

            def __init__(self, radius = 1):
                self.radius = radius

            def area(self):
                return self.radius * self.radius * Circle.pi

            def set_radius(self, radius):
                self.radius = radius

        myc = Circle(3)
        print(myc.radius)
        print(myc.area)
        print(myc.area())
        myc.radius = 100
        print(myc.area())
        myc.set_radius(200)
        print(myc.area())

    if (0):
        class Dog():

            # CLASS OBJECT ATTRIBUTE
            species = "mammal"

            def __init__(self, breed, name):
                self.breed = breed
                self.name = name

        mydog = Dog(name = "Lucky", breed = "Lab")
        otherDog = Dog("Huskie", "John")

        print(mydog.breed)
        print(mydog.name)

    if (0):
        class Sample():
            pass
        x = Sample()
        print(type(x))

elif (case == 'list'):
    if (1):
        mylist = ['stinnn', 1, 2, True, [1,2,3]]
        print (mylist)
        mylist.append(['a', 'b', 1]) # appends object at end
        print (mylist)
        mylist.extend(['a', 'b', 1]) #extend list by appending elements from the iterable
        print (mylist)
        item = mylist.pop() #pop from last one
        print (mylist)
        print (item)
        item = mylist.pop(0) #pop from 1st index
        print (mylist)
        print (item)
        matrix = [[1,2,3], [4,5,6], [7,8,9]]
        first_col = [row[0] for row in matrix]
        print (first_row)
    if (0): #list comprehensions
        S = [x**2 for x in range(10)]
        print (S)
        M = [x for x in S if x % 2 == 0]
        print (M)
        words = 'The quick brown fox jumps over the lazy dog'.split()
        print(words)
        stuff = [[w.upper(), w.lower(), len(w)] for w in words]
        for i in stuff:
            print (i)
elif (case == "dictionary"):
   if (1):
      my_stuff = {"key" : 123, "key2" : "value2", 'key3' : {'123' : [1,2, 'grab me']}}
      print (my_stuff['key3']['123'][2])
      my_stuff['key4'] = "value4"
      print (my_stuff)

elif (case == 'tuple'):
   if (1):
      t = (1,2,3)
      print (t)
      print (t[0])
elif (case == "set"):
   if (1):
       x = set()
       x.add(1)
       x.add(2)
       x.add(3)
       print (x)
       x = set([1,1,1,2,2,3,3,4,4])
       print (x)

       mylist = [1,1,1,2,2,2,3,3,3,]
       x = set(mylist)
       print(x)
elif (case == "sqlserver"):
    if (1):
       import pyodbc
       server = '10.13.220.35'
       database = 'MAM'
       username = 'hsing1'
       password = '0123456789'
       connStr = 'DRIVER={{ODBC Driver 13 for SQL Server}};SERVER={s};PORT=1443;DATABASE={d};UID={u};PWD={p}'.format(s= server, d = database, u = username, p = password)
       cursor = cnxn.cursor()
       tsql = "select * from TBUSERS where FSUESR = 'hsing1';"
       with cursor.execute(tsql):
           row = cursor.fetchone()
           while row:
               print(str(row[0], " " + str(row[1])))
               row = cursor.fetchone()
elif (case == "for"):
    if (1):
        mypairs = [(1,2), (3,4), (5, 6)]
        for (tup1, tup2) in mypairs:
            print (tup1)
            print (tup2)


elif (case == "function"):
    if (1):
        def end_other(a, b):
            a = a.lower()
            b = b.lower()

            #return (b.endswith(a) or a.endswith(b))
            return a[-(len(b)):] == b or a == b[-len(a):]
        print (end_other("abcd", "cd"))
        mystr = "abcd"
        print (mystr[-5:])

    if (0):
        str1 = "0123456789"
        def stringBits(mystr):
            result = ""
            for i in range(len(mystr)):
                if i%2==0:
                    result = result + mystr[i]
            return result

        print(stringBits("0123456789"))
        print(str1[::2])
        print(str1[::3])

    if (0):
        def my_func():
            """
            THIS IS THE DOCSTRING
            """
            print("my function")

        my_func()
    if (0):
        def arrayCheck(nums):
            for i in range(len(nums) - 2):
                if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                    return True
            return False
        print (arrayCheck([0,1,2,3,4,5,6]))
        print (arrayCheck([0,1,3,4,5,6]))
        print (arrayCheck([0,0,1,2,3,4,5,6]))

elif (case == "lambda"):
    if (1):
        mylist = [1,2,3,4,5,6,7,8]

        def even_bool(num):
            return num%2 == 0

        evens = filter(even_bool, mylist)
        print (list(evens))

        evens2 = filter(lambda num:num%2==0, mylist)
        print (list(evens2))
elif (case == 'shelve'):
    if (False):
        dBase = shelve.open("myDbase")
        object1 = ['The', 'bright', ('side', 'of'), ['life']]
        object2 = {'name' : 'Brian', 'age' : 33, 'motto' : object1}
        dBase['brian'] = object2
        dBase['knight'] = {'name' : 'Knight', 'motto' : 'Nil'}
        print(len(dBase))

    if (True):
        dBase = shelve.open("myDbase")
        print(dBase.keys())
        for row in dBase.keys():
            print(row, "=>")
            for field in dBase[row].keys():
                print (fields, "=>", dBase[row][field])

elif (case == 'list'):
    book = ['Python', 'Development', 8]
    book.append(2008)
    print(book)
    book.insert(1, 'Web')
    print(book)
    print(book[:3])
    print('Django' in book)
    book.remove(8)
    print(book)
    print(book.pop(-1))
    print(book)
    print(book * 2)
    print(book)
    print(book.extend(['with', 'Django'])) #None
    print(book)

    print(book.sort()) #None
    print(book)

else:
    print ("nothng")
