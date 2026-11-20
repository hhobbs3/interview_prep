import math

def hello_world():
    """Hello World function"""
    print("Hello, World!")

def int_to_binary_str(n: int) -> str:
    return bin(n, 32)[2:] 

def is_substring(s: str, t: str) -> bool:
    # s = 'abd'
    # t = 'abcde'
    i = 0
    for c in t:
        if len(s) <= i:
            return True
        if c == s[i]:
            i += 1
    return len(s) <= i

def fizz_buzz(n: int) -> list[str]:
    l = []
    for i in range(1, n + 1):
        s = ''
        if i % 3 == 0:
            s = 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        val =  s if len(s) > 0 else str(i) # len(s) > 0 ? s : str(i)
        l.append(val)
    return l

def third_max(nums: list[int]) -> int:
    nums_sorted = sorted(set(nums))
    if len(nums_sorted) > 2:
        return nums_sorted[-3]
    else:
        return nums_sorted[-1]


def constructRectangle(area: int) -> list[int]:
    w = int(math.sqrt(area))
    while area % w:
        w -= 1
    return [area//w, w]


def two_sum(nums: list[int], target: int) -> list[int]:
    # s = two_sum([2,11,7,15], 9)
    nums_index = [(v, index) for index, v in enumerate(nums)]
    INDEX = 1
    VAL = 0
    nums_index = sorted(nums_index)
    l = 0
    r = len(nums_index) - 1
    while l != r:
        current_sum = nums_index[l][VAL] + nums_index[r][VAL]
        if current_sum > target:
            r -= 1
        elif current_sum < target:
            l += 1
        else:
            return [nums_index[l][INDEX], nums_index[r][INDEX]]
    return None
 
def isValidParentheses(s: str) -> bool:
    compare = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if c in compare.values():          # opening bracket
            stack.append(c)
        elif c in compare:                 # closing bracket
            if not stack or stack[-1] != compare[c]:
                return False
            stack.pop()

    return not stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward

        return prev  # prev is the new head of the reversed list

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()  # Sort by start time
    merged_intervals = []
    l = intervals[0][0]
    r = intervals[0][1]
    for interval in intervals:
        if interval[0] <= r:
            r = interval[1] if interval[1] > r else r # set upper boundary
        elif interval[0] > r:
            merged_intervals.append([l,r])
            l = interval[0]
            r = interval[1]
    merged_intervals.append([l,r])
    return merged_intervals

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
        return list(anagrams.values())

def maxProfit(prices: list[int]) -> int:
        low = prices[0]
        high = prices[0]
        max_profit = 0
        for price in prices:
            if price < low: # always set lowest price
                low = price
            if price - low > max_profit:
                high = price
                max_profit = high - low # only apply profit when math works
        return max_profit

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr
    

def main():
    """Main function"""
    s = two_sum([2,7,11,15], 9)

    print(s)



if __name__ == "__main__":
    main()