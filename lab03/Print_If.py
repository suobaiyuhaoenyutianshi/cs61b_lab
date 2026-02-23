# -*- coding: gbk -*-
def print_if(s, f):
    """Print each element of s for which f returns a true value.

    >>> print_if([3, 4, 5, 6], lambda x: x > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda x: x % 2 == 0)
    4
    6
    >>> print(result)  # print_if should return None
    None
    """
    for x in s:
        "*** YOUR CODE HERE ***"
        if f(x):
            print(x)


def close(s, k):
    """Return how many elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        if abs((i - s[i])) <= k:
            count += 1
    print(count)
    return count


def close_list(s, k):
    """返回 s 中与其索引相差在 k 以内的元素的列表。

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # 只有 3 等于它的索引
    [3]
    >>> close_list(t, 1)  # 元素 2、3 和 5 与它们的索引的差的绝对值小于等于 1
    [2, 3, 5]
    >>> close_list(t, 2)  # 元素 2、3、4 和 5 与它们的索引的差的绝对值小于等于 2
    [2, 4, 3, 5]
    """
    return [s[i] for i in range(len(s)) if (abs((s[i] - i) <= k))]


def make_onion(f, g):
    def can_reach(x, y, limit):
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(g(x), y, limit - 1) or can_reach(f(x), y, limit - 1) # noqa
    return can_reach



def double_eights(n):
    """ 返回 n 是否有连续两个数字为 8。 假设 n 至少有两位数字。

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # 禁止迭代
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** 你的代码在这里 ***"
    # if n == 0:
    #     return "False"
    # last_num = n % 10
    # lat_itm = n // 10
    
    # if last_num == 8:
    #     kaitou = double_eights(lat_itm)
    #     if kaitou == "1":
    #         return "True"
    #     elif kaitou == "True":
    #         return "True"
    #     else:
    #         return "1"
    # else:
    #     kaitou = double_eights(lat_itm)
    #     if kaitou == "True":
    #         return "True"
    #     else:
    #         return "False"
    # 太失败了
    
    """返回 n 是否有连续两个数字为 8。假设 n 至少有两位数字。"""
    if n < 10:          # 只剩一位数时不可能有连续两个8
        return False
    if n % 100 == 88:   # 最后两位都是8
        return True
    return double_eights(n // 10)  # 去掉最后一位继续检查
print(double_eights(880))
print(double_eights(78))
print(double_eights(284682))
print(double_eights(88888))