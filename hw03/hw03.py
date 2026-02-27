# coding: gbk
LAB_SOURCE_FILE=__file__


HW_SOURCE_FILE=__file__


def num_eights(n):
    """编写一个递归函数 num_eights，该函数接受一个正整数 n 并返回数字 8 在 n 中出现的次数.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    return (1 if n % 10 == 1 else 0) + num_eights(n // 10)


# print(num_eights(88888888))
# # 8
# print(num_eights(2638))
# # 1
# print(num_eights(86380))
# # 2
# print(num_eights(12345))
# # 0
# print(num_eights(8782089))
# # 3

def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n // 10 == 0:
        return 0
    # two_num = n % 100
    two_first_num = (n % 100) // 10
    two_sec_num = (n % 100) % 10
    return abs(two_first_num - two_sec_num) + digit_distance(n // 10)


# print(digit_distance(31415926535)) # 32


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.
编写一个名为 interleaved_sum 的函数，该函数接受一个数字 n 以及两个单参数函数 odd_func 和 even_func。
此函数将 odd_func 应用于 1 到 n（包括 n）之间的每个奇数，将 even_func 应用于每个偶数，并返回总和。

例如，执行 interleaved_sum(5, lambda x: x, lambda x: x * x) 返回 1 + 2*2 + 3 + 4*4 + 5 = 29。

实现此函数，无需使用任何循环或直接判断数字的奇偶性——不允许使用模数 (%)！ 应该从 1 开始，因为它是一个奇数。

提示：引入一个内部辅助函数，该函数接受一个奇数 k 并计算从 k 到 n（包括 n）的交错和。
    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod'])
    # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(k):
        if k > n:
            return 0
        total = odd_func(n)
        if k + 1 <= n:
            total += even_func(n + 1)
        return total + helper(n + 2)
    return helper(1)
    # 直接调用并返回结果，不是返回函数本身a，而是a()运行结果
# identity = lambda x: x
# square = lambda x: x * x
# print(interleaved_sum(5, identity, square))


# 给定一个正整数 total，如果硬币值的总和为 total，则一组硬币可以兑换 total。 在这里，我们将使用标准美国硬币值：
# 1、5、10、25。 例如，以下集合可以兑换 15：

# 15个1美分的硬币
# 10个1美分的硬币，1个5美分的硬币
# 5个1美分的硬币，2个5美分的硬币
# 5个1美分的硬币，1个10美分的硬币
# 3个5美分的硬币
# 1个5美分的硬币，1个10美分的硬币
# 因此，15 有 6 种兑换方式。编写一个递归函数 count_coins，它接受一个正整数 total 作为输入，
# 并返回用硬币凑出总金额 total 的组合数。
# 你可以使用以下给定的函数：
# next_larger_coin 函数会返回比输入面额更大的下一种硬币面额。例如，next_larger_coin(5) 的返回值是 10。
# next_smaller_coin 函数会返回比输入面额更小的下一种硬币面额。例如，next_smaller_coin(5) 的返回值是 1。
# 如果不存在更大或更小的硬币面额，则任一函数将返回 None。
# 解决这个问题主要有两种思路：一种是使用 next_larger_coin 函数，另一种是使用 next_smaller_coin 函数。
# 重要：必须使用递归方法；使用循环会导致测试失败。


def next_larger_coin(coin):
    """next_larger_coin 函数会返回比输入面额更大的下一种硬币面额。例如，next_larger_coin(5) 的返回值是 10。
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """next_smaller_coin 函数会返回比输入面额更小的下一种硬币面额。例如，next_smaller_coin(5) 的返回值是 1。
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


# 每次递归都会考虑“用当前硬币”和“不用当前硬币”两种情况，覆盖所有可能的组合
# 由于我们始终限制使用的最大面额，不会产生重复（例如先10后5 和 先5后10 被视为同一种，因为这里我们强制面额不递增）
# 这两点很重要
def count_coins(amount):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(amount, max_coin):
        if amount == 0:
            return 1
        if amount < 0 or max_coin is None:
            return 0
        with_coin = helper(amount - max_coin, max_coin)
        without_coin = helper(amount, next_smaller_coin(max_coin))
        return with_coin + without_coin
    return helper(amount, 25)
# print(count_coins(20))    


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

