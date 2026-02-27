# coding: gbk
class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """返回该交易是否导致余额发生变化"""
        "*** YOUR CODE HERE ***"
        # 即 return 真与假
        return self.before != self.after

    def report(self):
        """返回一个描述交易的字符串

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg = "no change"
        if self.changed():
            "*** YOUR CODE HERE ***"
            if self.before > self.after:
                msg = f"increased {self.before}->{self.after}"
            else:
                msg = f"decreased {self.before}->{self.after}"
        return str(self.id) + ": " + msg


class Account:
    """A bank account that tracks its transaction history.

    >>> a = Account('Eric')
    >>> a.deposit(100)    # Transaction 0 for a
    100
    >>> b = Account('Erica')
    >>> a.withdraw(30)    # Transaction 1 for a
    70
    >>> a.deposit(10)     # Transaction 2 for a
    80
    >>> b.deposit(50)     # Transaction 0 for b
    50
    >>> b.withdraw(10)    # Transaction 1 for b
    40
    >>> a.withdraw(100)   # Transaction 3 for a
    'Insufficient funds'
    >>> len(a.transactions)
    4
    >>> len([t for t in a.transactions if t.changed()])
    3
    >>> for t in a.transactions:
    ...     print(t.report())
    0: increased 0->100
    1: decreased 100->70
    2: increased 70->80
    3: no change
    >>> b.withdraw(100)   # Transaction 2 for b
    'Insufficient funds'
    >>> b.withdraw(30)    # Transaction 3 for b
    10
    >>> for t in b.transactions:
    ...     print(t.report())
    0: increased 0->50
    1: decreased 50->40
    2: no change
    3: decreased 40->10
    """

    # *** YOU NEED TO MAKE CHANGES IN SEVERAL PLACES IN THIS CLASS ***

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """将账户余额增加指定金额，将存款添加至交易记录中，并返回新的余额。
        """
        before = self.balance
        self.balance = self.balance + amount
        after = self.balance
        t = Transaction(len(self.transactions), before, after)
        self.transactions.append(t)
        return self.balance

    def withdraw(self, amount):
        """将账户余额减少指定金额，将取款操作添加至交易记录中，并返回新的余额。
        """
        before = self.balance
        if amount > self.balance:
            after = before
            t = Transaction(len(self.transactions), before, after)
            self.transactions.append(t)
            return "Insufficient funds"
        self.balance = self.balance - amount
        after = self.balance
        t = Transaction(len(self.transactions), before, after)
        self.transactions.append(t)
    
        return self.balance


# a = Account('Eric')
# a.deposit(100)    # Transaction 0 for a
# 100
# b = Account('Erica')
# a.withdraw(30)    # Transaction 1 for a
# 70
# a.deposit(10)     # Transaction 2 for a
# 80
# b.deposit(50)     # Transaction 0 for b
# 50 
# b.withdraw(10)    # Transaction 1 for b
# 40
# a.withdraw(100)   # Transaction 3 for a
# 'Insufficient funds'
# len(a.transactions)
# 4
# for t in a.transactions:
#     print(t.report())


class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name


class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """将邮件添加到目标客户端的收件箱里。"""
        self.clients[email.recipient_name].inbox.append(email)

    def register_client(self, client):
        """将客户端注册到服务器的客户端列表中。"""
        self.clients[client.name] = client


class Client:
    """客户端包含服务器、名称 (字符串) 和收件箱 (列表) 这些属性。

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name??????????
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message, recipient_name):
        """向指定收件人发送邮件，内容为给定消息。"""
        email = Email(message, self, recipient_name)
        self.server.send(email)
        


def make_change(amount, coins):
    """返回一个硬币列表，其总和为amount，优先使用可用的最小面额硬币，
    并将最小面额硬币放在返回列表的前面。

    coins 参数是一个字典，其键是正整数面额，值是正整数硬币数量。

    >>> make_change(2, {2: 1})
    [2]
    >>> make_change(2, {1: 2, 2: 1})
    [1, 1]
    >>> make_change(4, {1: 2, 2: 1})
    [1, 1, 2]
    >>> make_change(4, {2: 1}) == None
    True

    >>> coins = {2: 2, 3: 2, 4: 3, 5: 1}
    >>> make_change(4, coins)
    [2, 2]
    >>> make_change(8, coins)
    [2, 2, 4]
    >>> make_change(25, coins)
    [2, 3, 3, 4, 4, 4, 5]
    >>> coins[8] = 1
    >>> make_change(25, coins)
    [2, 2, 4, 4, 5, 8]
    """
    if amount == 0:
        return []
    if not coins:
        return None
    smallest = min(coins)
    if amount < smallest:
        return None
    "*** 你的代码写在这里 ***"
    # 分支1：尝试使用一枚最小面额硬币
    # 先得到去掉一枚smallest后的新字典
    new_coin_use = remove_one(coins, smallest)
    result = make_change(amount - smallest, new_coin_use)
    if result is not None:
        return [smallest] + result
    # 分支2：如果使用后失败，则尝试不使用这一枚硬币
    # 注意：这里也要去掉一枚，因为这一枚我们决定不用了，要从可用硬币中移除
    new_coins_skip = remove_one(coins, smallest)
    return make_change(amount, new_coins_skip)
        

def remove_one(coins, coin):
    """从硬币字典中移除一枚硬币。返回一个新字典，
    保持原始字典 coins 不变。

    >>> coins = {2: 5, 3: 2, 6: 1}
    >>> remove_one(coins, 2) == {2: 4, 3: 2, 6: 1}
    True
    >>> remove_one(coins, 6) == {2: 5, 3: 2}
    True
    >>> coins == {2: 5, 3: 2, 6: 1} # 未改变
    True
    """
    copy = dict(coins)
    count = copy.pop(coin) - 1  # 移除该面额的硬币
    if count:
        copy[coin] = count      # 如果还有剩余，重新添加该面额
    return copy


coins = {1: 2, 2: 1, 3: 1}
print(make_change(6, coins))


class ChangeMachine:
    """一个兑换机持有一定数量的硬币，最初都是便士。
    change 方法添加一个面值为 X 的硬币，并返回一个总价值为 X 的硬币列表。
    机器倾向于返回可用的小硬币。机器中的总价值永远不会改变，
    并且它始终可以兑换任何硬币（可能通过返回传入的硬币）。

    coins 属性是一个字典，其键是正整数面额，值是正整数硬币计数。

    >>> m = ChangeMachine(2)
    >>> m.coins == {1: 2}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.coins == {2: 1}
    True
    >>> m.change(2)
    [2]
    >>> m.coins == {2: 1}
    True
    >>> m.change(3)
    [3]
    >>> m.coins == {2: 1}
    True

    >>> m = ChangeMachine(10) # 10 便士
    >>> m.coins == {1: 10}
    True
    >>> m.change(5) # 投入一个五美分硬币，并找回 5 个一美分硬币
    [1, 1, 1, 1, 1]
    >>> m.coins == {1: 5, 5: 1} # 剩余 5 个便士和一个镍币
    True
    >>> m.change(3)
    [1, 1, 1]
    >>> m.coins == {1: 2, 3: 1, 5: 1}
    True
    >>> m.change(2)
    [1, 1]
    >>> m.change(2) # 剩余的一美分硬币不够了，所以直接返回一个两美分硬币
    [2]
    >>> m.coins == {2: 1, 3: 1, 5: 1}
    True
    >>> m.change(8) # 没有足够的两美分硬币来凑出 8 美分，所以用一个 3 美分硬币和一个 5 美分硬币来代替。
    [3, 5]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(1) # 直接返回投入的一美分硬币（因为它是最小面值的）。
    [1]
    >>> m.change(9) # 直接返回投入的 9 美分硬币（因为没有其他硬币可以组合成 9 美分）。
    [9]
    >>> m.coins == {2: 1, 8: 1}
    True
    >>> m.change(10)
    [2, 8]
    >>> m.coins == {10: 1}
    True

>>> m = ChangeMachine(9)

    >>> [m.change(k) for k in [2, 2, 3]]
    [[1, 1], [1, 1], [1, 1, 1]]
    >>> m.coins == {1: 2, 2: 2, 3: 1}
    True
    >>> m.change(5) # 倾向于使用 [1, 1, 3] 而不是 [1, 2, 2] (因为有更多的 1 分硬币)
    [1, 1, 3]
    >>> m.change(7)
    [2, 5]
    >>> m.coins == {2: 1, 7: 1}
    True
    """
    def __init__(self, pennies):
        self.coins = {1: pennies}

    def change(self, coin):
        """返回找零, 并从 self.coins 中移除."""
        "*** YOUR CODE HERE ***"
# self.coins.get(coin, 0)：从字典中获取面额 coin 的当前数量。如果该面额不存在，返回 0。
        self.coins[coin] = 1 + self.coins.get(coin, 0)
        result = make_change(coin, self.coins)
        for c in result:
             self.coins = remove_one(self.coins, c)
        return result



# m = ChangeMachine(2)
# print(m.change(2))   # 预期输出 [1, 1]
# print(m.coins)       # 预期输出 {2: 1} 或 {1:0, 2:1} 取决于 remove_one 的实现