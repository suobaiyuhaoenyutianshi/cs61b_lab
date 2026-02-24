# coding: gbk
HW_SOURCE_FILE = __file__


def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    num = 0
    while num < len(s):
        if s[num] == before:
            s.insert((num + 1), after)
        num += 2
    else:
        num += 1
    return s


def group_by(s, fn):
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for num in range(len(s)):
        key = fn(s[num])
        if key in grouped:
            grouped[key].append(s[num])
        else:
            grouped[key] = [s[num]]
    return grouped


def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    # count = 0
    # step = 0
    # for i in t:
    #     if i == x:
    #         count += 1
    #     if step == n - 1:
    #         break
    #     step += 1
    # return count

    count = 0
    for _ in range(n):
        if next(t) == x:
            count += 1
    return count


def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    count = 1
    first = None
    for i in t:

        if i == first:
            count += 1
        if i != first:
            count = 1
        if count == k:
            return i
        first = i


# 9
def sprout_leaves(t, leaves):
    """Sprout new leaves containing the labels in leaves at each leaf of
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        # 当前是叶子：生成新分支，每个分支是一个叶子节点，标签取自 leaves
        return tree(label(t), [tree(leaf) for leaf in leaves])
    else:
        # 当前不是叶子：递归处理每个分支，然后构建新树
        return tree(label(t), [sprout_leaves(b, leaves) for b in branches(t)])
             
def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"


# Tree Data Abstraction

# 树的数据抽象实现，使用列表表示树，第一个元素为节点值，后续元素为子节点（分支)
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), "branches must be trees"
    return [label] + list(branches)

# 返回树的根节点标签。
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

#  返回树的子节点列表。
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise.
    `is_tree` 函数中的条件 `if type(tree) != list or len(tree) < 1` 用于**初步筛选**：它要求树必须是一个**非空列表**。这是因为在我们的树抽象中，每个节点都用一个列表表示，列表的第一个元素是标签，后续元素是子节点。如果传入的对象不是列表，或者列表为空（没有标签），那肯定不是一棵合法的树。

以你构造的 `t2` 为例：

```python
t2 = tree(1,
          [tree(2),
           tree(3, [tree(4), tree(5)]),
           tree(6, [tree(7)])])
```

这个 `t2` 是通过 `tree` 构造函数生成的，它的实际列表结构是：

```
[1,
 [2],
 [3, [4], [5]],
 [6, [7]]]
```

现在，我们来模拟 `is_tree(t2)` 的执行过程：

1. **检查根节点**：
   - `type(t2) != list`：`t2` 是列表，不成立。
   - `len(t2) < 1`：`t2` 的长度至少为 1（实际上是 4），不成立。
   - 所以第一个条件通过，进入下一步：**遍历每个分支**。

2. **遍历分支**：
   - `branches(t2)` 返回 `[[2], [3, [4], [5]], [6, [7]]]`。
   - 对第一个分支 `[2]` 递归调用 `is_tree`：
     - 它是列表，长度≥1 → 继续检查它的分支（为空）→ 递归返回 `True`。
   - 对第二个分支 `[3, [4], [5]]` 递归调用：
     - 是列表，长度≥1 → 它的分支是 `[[4], [5]]`。
       - 对 `[4]` 递归：是列表，长度≥1，无分支 → `True`。
       - 对 `[5]` 递归：同理 → `True`。
     - 所有子分支检查通过 → 返回 `True`。
   - 对第三个分支 `[6, [7]]` 递归：
     - 是列表，长度≥1 → 分支为 `[[7]]`。
       - 对 `[7]` 递归：是列表，长度≥1，无分支 → `True`。
     - 返回 `True`。

3. **所有分支都返回 `True`**，所以 `is_tree(t2)` 最终返回 `True`。

**如果数据不合法**，比如尝试构造 `tree(1, [2])`（`2` 不是树列表），`tree` 函数会调用 `is_tree(2)` 来验证分支：

- `type(2) != list` 成立 → 直接返回 `False`。
- 于是 `assert is_tree(branch)` 触发 `AssertionError`，阻止非法树的生成。

**总结**：`if type(tree) != list or len(tree) < 1` 是递归验证的**基础守卫条件**，
它确保当前节点至少具有“列表”形式和“有标签”这两个基本属性，为后续递归检查分支铺平道路。与 `tree` 构造函数配合，
保证了每次创建的树都严格符合递归定义。
    """
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    branches(tree) 返回树的子节点列表。如果树有子节点，返回一个非空列表；如果树没有子节点（是叶子），返回空列表 []。

在 Python 中，空列表在布尔上下文中被视为 False，非空列表被视为 True。

not 是逻辑取反运算符：not True 得 False，not False 得 True。

因此：

如果 branches(tree) 是空列表（False），not False 就是 True，表示是叶子。

如果 branches(tree) 是非空列表（True），not True 就是 False，表示不是叶子。
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """ 以缩进形式打印树的层次结构。
    参数:
        t: 要打印的树
        indent: 当前缩进级别（每级两个空格），用于递归时传递深度
    目的:
        直观展示树的形状，便于调试和理解。
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
