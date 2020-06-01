#coding=utf-8
#我们有一个包含N个元素的元组或序列，现在想要将它分解为N个单独的变量。
#注意：元素的数量必须匹配！！！

#元组
p = (4, 5)
x, y = p
print("x=%s" %x)
print("y=%s" %y)

#序列
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name=%s,date=%s" % (name,date))

name, shares, price, (year, month, day) = data
print("name=%s,year=%s,month=%s,day=%s" % (name, year, month, day))

#字符串
s = 'Hello'
a, b, c, d, e = s
print("a=%s,b=%s,e=%s" %(a, b, e))

#测试丢弃某些特定的值,用一个用不到的变量名
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print('shares=%s,price=%s' % (shares, price))