#coding=utf-8
#从任意长度的可迭代对象中分解元素

#python的"*表达式"可以解决这个问题。
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print("name=%s,email=%s,phone_number=%s" % (name, email, phone_numbers))

#"*表达式"修饰的变量也可以位于列表的第一个位置
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print("trailing=%s, current=%s" % (trailing, current))

#做拆分操作"*表达式"测试
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('uname=%s,homedir=%s,sh=%s' % (uname, homedir, sh))

#使用"*表达式"做分解丢弃某些值测试
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print('name=%s,year=%s' % (name, year))

#使用"*表达式"做分解头部和尾部测试
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print('head=%s,tail=%s' % (head, tail))