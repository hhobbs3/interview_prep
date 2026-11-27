# Interview question outlines – one from each section
# -----------------------------------------------------------
# 1. Arrays & Strings – Two Sum
#    Premise: Given an array of integers ``nums`` and an integer ``target``,
#    return the indices of the two numbers such that they add up to ``target``.
#    Example input:
#        nums = [2, 7, 11, 15]
#        target = 9
#    Expected output: [0, 1]  # because nums[0] + nums[1] == 9

# Critique:
# 1. Uses a list of tuples instead of a simple dictionary; 
# 2. Variable names like `total_nums`, `l`, `r`, `index`, `value` are unclear. 
# 3. The algorithm effectively performs a double‑loop with O(n²) worst‑case time. 
# 4. Returns `None` implicitly when no pair is found; a more explicit `[]` would be clearer. 
# 5. The loop logic for moving `l` and `r` is fragile and may skip valid pairs. 
#

def two_sum(nums: list[int], target: int) -> list[int]:
    total_nums = len(nums)
    if total_nums <= 1:
        # less than 2 to sum
        return
    nums_map = [(i, val) for i, val in enumerate(nums)]
    l = 0
    r = 1
    index = 0
    value = 1
    while l != r:
        if nums_map[l][value] + nums_map[r][value] == target:
            return [nums_map[l][index], nums_map[r][index]]
        elif r < total_nums - 1:
            r += 1
        elif l < r:
            l += 1
            r = ((l + 1) if l + 1 < total_nums else l)
    return 

# 2. Linked Lists – Reverse a Linked List
#    Premise: Given the head of a singly linked list, reverse the list in place
#    and return the new head.
#    Example input:
#        1 -> 2 -> 3 -> 4 -> 5 -> None
#    Expected output: 5 -> 4 -> 3 -> 2 -> 1 -> None
#
# 3. Stacks & Queues – Balanced Parentheses
#    Premise: Given a string containing only parentheses characters
#    ``()[]{}``, determine if the input string is valid:
#      • Every opening must have a matching closing in the correct order.
#    Example input:
#        "{[()]()}"  # valid
#    Expected output: True
#    Example input:
#        "{[(])}"  # invalid
#    Expected output: False
#
# 4. Trees & Graphs – Lowest Common Ancestor (LCA) in a Binary Tree
#    Premise: Given a binary tree and two nodes ``p`` and ``q``, find
#    their lowest common ancestor – the deepest node that has both ``p``
#    and ``q`` as descendants (a node can be a descendant of itself).
#    Example input: binary tree represented by its root node
#        p = node with value 5
#        q = node with value 1
#    Expected output: node with value 3  # assuming tree shape from book example
#
# 5. Dynamic Programming – Edit Distance (Levenshtein Distance)
#    Premise: Given two strings ``word1`` and ``word2``, compute the minimum
#    number of operations (insert, delete, replace) required to convert
#    ``word1`` into ``word2``.
#    Example input:
#        word1 = "intention"
#        word2 = "execution"
#    Expected output: 5
#
# 6. Sorting & Searching – Quick Sort
#    Premise: Implement the quick sort algorithm to sort an array of
#    comparable elements in place.
#    Example input:
#        arr = [3, 6, 8, 10, 1, 2, 1]
#    Expected output after sorting: [1, 1, 2, 3, 6, 8, 10]
#
# 7. Miscellaneous – LRU Cache
#    Premise: Design an LRU (Least Recently Used) cache with O(1)
#    operations for get and put, given a fixed capacity.
#    Example input:
#        capacity = 2
#        operations = [
#            ("put", 1, 1),
#            ("put", 2, 2),
#            ("get", 1),
#            ("put", 3, 3),
#            ("get", 2),
#            ("put", 4, 4),
#            ("get", 1),
#            ("get", 3),
#            ("get", 4)
#        ]
#    Expected output: [1, None, 2, None, 3, 4]
#    (None indicates a cache miss)

# These concise outlines reflect the kind of question you might see in a real interview.
# The examples illustrate the input and the expected output.
def test(x: int) -> int:
    return x

def main():
    """Main function"""
    # 1. two sums
    nums = [11, 2, 11, 7, 15]
    target = 9
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()