# Python基础

## 1.文件操作

### 1.1 有一个jsonline格式的文件file.txt 大小约为10K，按行读入这个文件

```python
def get_lines():
	l = []
	with open('file.txt','rb') as f:
		for eachline in f:
			l.append(eachline)
	return l

if __name__ == '__main__':
	for e in get_lines():
		process(e) #处理每一行数据
```

现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？

```python
def get_lines():
	l = []
	with open('file.txt','rb') as f:
		data = f.readlines(60000)
        l.append(data)
	yield l
```

要考虑的问题有：内存只有4G无法一次性读入10G文件，需要**分批读入**，分批读入数据要记录每次读入数据的位置。分批**每次读取数据的大小**，太小会在读取操作花费过多时间。

### 1.2接收文件夹名称，返回文件夹中文件的路径以及文件夹中文件的路径

```python
import os
def print_dictionary_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_dictionary_contents(sChildPath)
        else:
            print(sChildPath)
```

> 使用递归

### 1.3输入日期，判断这一天是这一年的第几天

```python
import datetime
def dayofyear():
    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入天：")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1-date2).days+1
```

## 2.数据类型

### 2.1 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?

```python
sorted(d.items(), lambda x:x[1])
```

### 2.2 字典推导式

```python
{key:value for (key, value) in iterable}
```

### 2.3 请反转字符串 "aStr"?

```python
print(astr[::-1])
```

### 2.4 将字符串 "k:1|k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}

```python
str1 = "k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1 = {}
    for items in str1.split('|'):
        key, value = items.split(':')
        dict1[key] = value
    return dict1
```

### 2.5 请按alist中元素的age由小到大排序

```python
 alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
 def sort_list(alist):
    return sorted(alist, key = lambda x: x['age'], reverse=True)
```

### 2.6 下面代码的输出结果将是什么？

```python
list = ['a','b','c','d','e']
print(list[10:])
```

代码将输出`[]`,不会产生`IndexError`错误，就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。**例如，尝试获取list[10]和之后的成员，会导致IndexError**。然而，**尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表**。

### 2.7 写一个列表生成式，产生一个公差为11的等差数列

```python
[x*11 for x in range(10)]
```

### 2.8 给定两个列表，怎么找出他们相同的元素和不同的元素？

```python
list1 = [1,2,3]
list2 = [3,4,5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 ^ set2) # &交集 |并集 ^差集合
```

### 2.9 请写出一段python代码实现删除list里面的重复元素？

```python
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)
```

用list类的sort方法:

```python
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
```

### 2.10 给定两个list A，B ,请用找出A，B中相同与不同的元素

```python
A,B 中相同元素：print(set(A)&set(B))
A,B 中不同元素: print(set(A)^set(B))
```