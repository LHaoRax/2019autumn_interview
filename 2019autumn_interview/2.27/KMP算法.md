### KMP算法

这个字符串定位问题让我想到了之前没理解的KMP问题，这次主要理解了KMP的整体思路。其精髓在于：

+ 主串的指针不动，仅移动模式串指针，模式串移动的方式按照next数据移动。

+ next数组对应的是模式串本身的性质，反映了模式串前缀及后缀最长公共子集的长度

+ KMP算法相较于朴素算法利用了前面遍历时的信息，结合模式串本身的匹配特性，将比较位置定位到主串后缀与模式串前缀，因此可使主串指针不动，仅移动模式串指针到后缀的下一位

```python
def KMP(main_str, model_str):
    i, j = 0, 0
    next_list = next_KMP(model_str)
    while i < len(main_str) and j < len(model_str):
        if j == -1 or main_str[i] == model_str[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]

    if j == len(model_str):
        return i - j
    else:
        return -1
```

+ next数组的求解是算法的关键，利用python的切片特性，通过比较前后缀的公共部分，很容易求解出next数组。但这样求解不算是一个好的求解思路，因为它使用到了python的特性。

```python
def next_KMP(model_str):
    next_list = list(range(len(model_str)))
    for i in range(len(model_str)):
        j = i
        while model_str[:j] != model_str[i + 1 - j:i + 1] and j > 0:
            j -= 1
        next_list[i] = j

    ret_list = next_list[:-1]
    ret_list.insert(0, -1)
    return ret_list
```

+ next数组正常求解的思路应该是**自身匹配自身**，但这里的**主串和模式串是不断变化的**。这里有两个指针，**第一个指针i代表的是字符串后缀的末尾**，指的是**主串**；指针j代表的是前缀的末尾，指的是**模式串**。跟前面的匹配一样，主串指针i不动，模式串指针j可以回溯。假设此时主串的位置为i，模式串的位置为j，字符串为str：
    + `str[i] == str[j]`，则后缀长度加1，前缀长度加1，且两者相等。根据`next[i -1 ] == j - 1`，那么`next[i] == j`
    + `str[i] != str[j]`，则此时位置上再增加的后缀和前缀发生失配，因此前缀指针j需要发生回溯，回溯的位置应该是`next[j]`，因为`next[j]`代表了这一段字符串内存在前缀后缀共有的最大长度，而**这一部分的前缀会对应刚才的失配后缀内的一个更小的后缀**，**回溯后的j**再和**刚才的i**继续进行匹配。

```python
def next_KMP(model_str):
    next_list = list(range(len(model_str)))
    print(next_list)
    next_list[0] = -1 # 配合KMP主程序
    i, j = 0, -1 # i为后缀指针，j为前缀指针
    while i < len(model_str) - 1:
        if j == -1 or model_str[i] == model_str[j]:
            i += 1
            j += 1
            next_list[i] = j
        else:
            j = next_list[j]
    print(next_list)
    return next_list
```

> 由于next[i]的值跟前面的值相关，因此初始对i，j值的定义会使整体的next数组值发生移动