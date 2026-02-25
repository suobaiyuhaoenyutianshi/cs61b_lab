# coding: gbk
class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25)  # 10 -> 10.2 -> 10.404
    2
    >>> a.balance                # Calling time_to_retire method should not change the balance
    10
    >>> a.time_to_retire(11)     # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """返回账户余额增长到 amount 所需的年数。"""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** 在此处编写你的代码 ***"
        year = 0
        copy_balance = self.balance
        while copy_balance <= amount:
            copy_balance = copy_balance * self.interest + copy_balance
            year += 1
        return year


class FreeChecking(Account):
    """一种银行账户，取款会收取费用，但前两次免费！
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # 第一次是免费的。即使取款不成功，仍然算作一次免费取款机会
    'Insufficient funds'
    >>> ch.withdraw(3)    # 第二次取款也是免费的
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # 好的，两次免费取款次数已经用完，因为 free_withdrawals 的值为 2
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # 免手续费
    7
    >>> ch.withdraw(3)  # ch 仍然会收取手续费
    5
    >>> ch.withdraw(5)  # 余额不足，无法支付手续费和取款金额
    'Insufficient funds'
    """
   
    withdraw_fee = 1
    free_withdrawals = 2

    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.used_free_withdrawals = 0  # 记录已使用的免费取款次数

    def withdraw(self, amount):
        # 判断本次取款是否免费
        if self.used_free_withdrawals < self.free_withdrawals:
            # 先增加免费次数（即使取款失败也要计入）
            self.used_free_withdrawals += 1
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance -= amount
            return self.balance
        else:
            # 收费取款，需检查余额是否足够支付取款金额 + 手续费
            total = amount + self.withdraw_fee
            if total > self.balance:
                return 'Insufficient funds'
            self.balance -= total
            return self.balance
    
    


# ch = FreeChecking('Jack')
# ch.balance = 20
# print(ch.withdraw(100))  # 第一次是免费的。即使取款不成功，仍然算作一次免费取款机会
# 'Insufficient funds'
# print(ch.withdraw(3))    # 第二次取款也是免费的
# # 17
# print(ch.balance)
# # 17
# print(ch.withdraw(3))    # 好的，两次免费取款次数已经用完，因为 free_withdrawals 的值为 2
# # 13



def duplicate_link(s, val):
    """Mutates s so that each element equal to val is followed by another val.

    >>> x = Link(5, Link(4, Link(5)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(5, Link(5)))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, (Link(2, Link(3)))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
    if s is Link.empty:          # 空链表直接返回空
        return Link.empty
    if s.first == val:
        new_piont = Link(val, s.rest)
        return Link(s.first, Link(val, duplicate_link(new_piont.rest, val)))
    else:
        return Link(s.first, duplicate_link(s.rest, val))
        
    
    
    


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
#     """
#     你的困惑很自然，因为这里既有 `str()` 这个内置函数，又有 `__str__` 这个方法，而且它们还会互相调用。让我帮你理清它们的关系，并解释在这个链表打印过程中到底发生了什么。

# ---

# ## 1. `str()` 和 `__str__` 是什么关系？
# - **`__str__`** 是一个**方法**（定义在类里的函数），它规定了“这个类的对象应该如何被转换成字符串”。
# - **`str()`** 是一个**内置函数**，当你调用 `str(x)` 时，Python 会自动去调用 `x` 的 `__str__` 方法，并把结果返回给你。

# 所以：
# ```python
# str(x)   <==>   x.__str__()
# ```
# 它们是等价的。只不过我们通常直接写 `str(x)` 更简洁。

# ---

# ## 2. 在 `__str__` 方法里，什么时候用 `str()`，什么时候递归调用 `__str__`？
# 在你的链表 `__str__` 方法中，有这样一行：
# ```python
# string += str(self.first) + ' '
# ```
# 这里的 `str(self.first)` 就是在调用内置函数 `str()`，而 `self.first` 是当前节点存储的值。

# - 如果 `self.first` 是一个普通整数（比如 `5`），`str(5)` 会返回字符串 `"5"`。
# - 如果 `self.first` 是另一个 `Link` 对象（比如子链表），`str(那个子链表)` 会去调用那个子链表的 `__str__` 方法，生成它的字符串表示（比如 `"<8 9>"`）。

# 所以这一行代码可以**递归**地处理嵌套的链表：当遇到一个子链表时，`str(self.first)` 就会触发子链表的 `__str__` 方法，子链表又按照同样的规则生成自己的字符串，然后返回给外层拼接。

# ---

# ## 3. 那 `self = self.rest` 又是干什么的？
# ```python
# self = self.rest
# ```
# 这是在**遍历链表**，让当前指针 `self` 指向下一个节点，这样下一次循环就能处理下一个节点的值。

# 它和递归没有直接关系，只是用来沿着链表往后移动。这个赋值只影响当前方法里的局部变量 `self`，不会改变原来的链表。

# ---

# # ## 4. 用一个例子把整个过程走一遍
# 假设我们有链表：
# ```python
# lst = Link(7, Link(Link(8, Link(9)), Link(1)))
# ```
# 它的结构：
# - 节点1：`first = 7`，`rest` → 节点2
# - 节点2：`first = 子链表(8,9)`，`rest` → 节点3
# - 节点3：`first = 1`，`rest` = empty

# 当我们执行 `print(lst)` 时，Python 调用 `lst.__str__()`：

# ### 第一层（节点1）
# - `string = '<'`
# - 进入 `while`：`self.rest` 不是 empty（指向节点2）→ 执行循环体：
#   - 需要 `str(self.first)`，此时 `self.first = 7`，是整数，所以 `str(7)` 直接返回 `"7"`。
#   - `string += "7 "` → `string = "<7 "`
#   - `self = self.rest` → 现在局部变量 `self` 指向节点2。

# ### 第二层（节点2）
# - 再次检查 `while`：`self.rest` 不是 empty（指向节点3）→ 继续循环：
#   - 现在 `self.first` 是子链表 `Link(8, Link(9))`。
#   - 执行 `str(self.first)` → 这会调用**子链表的 `__str__` 方法**，我们称它为“子递归”。

# #### 子递归：子链表 `Link(8, Link(9))` 的 `__str__`
# - 进入子链表的 `__str__`：
#   - `string_sub = '<'`
#   - 循环：`self.rest` 不是 empty（指向 `Link(9)`）→ 处理：
#     - `str(self.first)`，此时 `self.first = 8` → 返回 `"8"`，拼上空格 → `string_sub = "<8 "`
#     - `self = self.rest` → 指向 `Link(9)`
#   - 再次检查循环：`self.rest` 是 empty → 结束循环
#   - 返回 `string_sub + str(self.first) + '>'`，此时 `self.first = 9` → 得到 `"<8 9>"`
# - 子递归结束，返回 `"<8 9>"`。

# 回到第二层：
# - 得到 `str(self.first)` 的结果是 `"<8 9>"`，所以：
#   - `string += "<8 9> "` → 此时外层 `string` 变成 `"<7 <8 9> "`
#   - `self = self.rest` → 局部变量 `self` 指向节点3。

# ### 第三层（节点3）
# - 再次检查 `while`：`self.rest` 是 empty → 不进入循环。
# - 执行最后一行：`return string + str(self.first) + '>'`
#   - `string` 当前是 `"<7 <8 9> "`
#   - `self.first = 1`，`str(1)` 返回 `"1"`
#   - 拼接：`"<7 <8 9> " + "1" + ">" = "<7 <8 9> 1>"`

# 最终输出：`<7 <8 9> 1>`

# ---

# ## 5. 关键点总结
# - **`str(self.first)` 中的 `str` 是函数**，它根据 `self.first` 的类型决定怎么转成字符串：
#   - 如果是数字、字符串等基本类型，直接转成对应的字符串。
#   - 如果是另一个 `Link` 对象，就调用那个对象的 `__str__` 方法（递归）。
# - **`__str__` 是方法**，它定义了“如何把当前对象变成字符串”。在它内部，可以通过 `str(...)` 调用其他对象的 `__str__`，从而形成递归。
# - **`self = self.rest`** 是循环遍历，让指针后移，处理下一个节点。它与递归是**两条不同的路径**：
#   - 递归发生在处理节点的值（`first`）时。
#   - 循环发生在处理完一个节点后，移动到下一个节点。

# 所以，你看到的现象是：在同一个方法里，既用 `str()` 递归地处理值，又用 `self = self.rest` 迭代地遍历链表，两者协同工作，最终生成整个链表的字符串。

# 希望这个解释能帮你解开困惑！如果还有哪里不清楚，欢迎继续问 ?
    
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

x = Link(5, Link(4, Link(5)))
print(duplicate_link(x, 5))

s = Link(5, Link(5, Link(4, Link(5, Link(5)))))
