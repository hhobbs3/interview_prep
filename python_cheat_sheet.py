"""
PYTHON INTERVIEW CHEAT SHEET
Run this file to see examples printed out.

Focus areas:
- list vs set vs dict
- enumerate
- zip
- sorting
- list comprehensions
- common string ops
- collections
- basic algorithms patterns
"""

from collections import Counter, defaultdict, deque
import heapq

print("=== EMPTY DATA TYPES ===")

empty_list = []
empty_list_alt = list()

empty_dict = {}
empty_dict_alt = dict()

empty_set = set()       # IMPORTANT: {} is NOT a set
empty_tuple = ()        # immutable
empty_string = ""

print("List:", empty_list, type(empty_list))
print("Dict:", empty_dict, type(empty_dict))
print("Set:", empty_set, type(empty_set))
print("Tuple:", empty_tuple, type(empty_tuple))
print("String:", empty_string, type(empty_string))

print("\nNote: {} creates a dict, not a set")
print("Type of {}:", type({}))
print()

print("=== LISTS ===")
nums = [1, 2, 3]
nums.append(4)
nums.pop()
nums.insert(0, 99)
print("List:", nums)
print("Slice [1:3]:", nums[1:3])
print("Reverse:", nums[::-1])
print()


print("=== SETS ===")
s = {1, 2, 3}
s.add(4)
s.remove(2)   # error if not exists
s.discard(10) # no error
print("Set:", s)
print("Is 3 in set?", 3 in s)
print()


print("=== DICTS ===")
d = {"a": 1, "b": 2}
d["c"] = 3
print("Dict:", d)
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

# Safe access
print("Get missing key:", d.get("z", 0))
print()


print("=== LOOPING ===")
nums = [10, 20, 30]

# Basic loop
for n in nums:
    print("Value:", n)

# Enumerate (index + value)
for i, val in enumerate(nums):
    print("Index:", i, "Value:", val)

nums_index = [(index, v) for index, v in enumerate(nums)]

# Zip
letters = ["a", "b", "c"]
for num, letter in zip(nums, letters):
    print(num, letter)

print()


print("=== LIST COMPREHENSIONS ===")
squares = [x * x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print("Squares:", squares)
print("Evens:", evens)
print()


print("=== STRING OPS ===")
s = "hello world"
print("Upper:", s.upper())
print("Split:", s.split())
print("Join:", "-".join(["a", "b", "c"]))
print("Replace:", s.replace("world", "python"))
print()


print("=== SORTING ===")
nums = [5, 1, 4, 2]
nums.sort()  # in place
print("Sorted:", nums)

nums = [5, 1, 4, 2]
sorted_nums = sorted(nums, reverse=True)
print("Sorted reverse:", sorted_nums)

# Sort by second value
pairs = [(1, 3), (2, 1), (4, 2)]
pairs.sort(key=lambda x: x[1])
print("Sorted by second value:", pairs)
print()


print("=== COUNTER ===")
arr = [1, 1, 2, 3, 3, 3]
count = Counter(arr)
print("Counter:", count)
print("Most common:", count.most_common(1))
print()


print("=== DEFAULTDICT ===")
dd = defaultdict(int)
dd["a"] += 1
print("Defaultdict:", dict(dd))
print()


print("=== STACK (use list) ===")
stack = []
stack.append(1)
stack.append(2)
print("Pop:", stack.pop())
print()


print("=== QUEUE (use deque) ===")
queue = deque()
queue.append(1)
queue.append(2)
print("Popleft:", queue.popleft())
print()


print("=== HEAP (MIN HEAP) ===")
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
print("Heap pop:", heapq.heappop(heap))
print()


print("=== TWO POINTER PATTERN ===")
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
while left < right:
    print("Pair:", arr[left], arr[right])
    left += 1
    right -= 1
print()


print("=== SLIDING WINDOW ===")
arr = [1, 2, 3, 4, 5]
window_sum = 0
k = 3
for i in range(len(arr)):
    window_sum += arr[i]
    if i >= k - 1:
        print("Window sum:", window_sum)
        window_sum -= arr[i - (k - 1)]
print()


print("=== COMMON PITFALLS ===")

# [] is list
print(type([]))

# {} is dict, NOT set
print(type({}))

# empty set:
print(type(set()))

# tuple (immutable)
print(type((1, 2)))

print("\n=== DONE ===")

class BankAccount:
    # Class variable (shared by all instances)
    bank_name = "Interview National Bank"

    def __init__(self, owner, balance=0):
        """
        Constructor
        Called automatically when creating a new object
        """
        self.owner = owner        # instance variable
        self.balance = balance    # instance variable

    def deposit(self, amount):
        """Instance method"""
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def __repr__(self):
        """What prints when you print(object)"""
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    @classmethod
    def change_bank_name(cls, new_name):
        """Class method (affects all accounts)"""
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        """Static method (no access to self or cls)"""
        return amount > 0


# ---- Using the class ----

print("=== Creating Objects ===")
acct1 = BankAccount("Harlen", 100)
acct2 = BankAccount("Alice")

print(acct1)
print(acct2)

print("\n=== Using Instance Methods ===")
acct1.deposit(50)
acct1.withdraw(30)

print("\n=== Accessing Class Variable ===")
print("Bank name:", BankAccount.bank_name)

BankAccount.change_bank_name("Senior Engineer Credit Union")