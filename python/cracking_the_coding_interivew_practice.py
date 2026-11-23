# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
import numpy as np


def isUnique(s: str) -> bool:
    """Determine if a string has all unique characters."""
    # Using a set to track seen characters
    if len(s) > 128:  # Assuming ASCII character set
        return False
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

def checkPermutation(s1: str, s2: str) -> bool:
    """Check if one string is a permutation of the other."""
    if len(s1) != len(s2):
        return False
    counter = {}
    for ch in s1:
        counter[ch] = counter.get(ch, 0) + 1
    for ch in s2:
        if ch not in counter or counter[ch] == 0:
            return False
        counter[ch] -= 1
    return True

def urlify(s: str, length: int) -> str:
    """Replace spaces in a string with '%20'."""
    # from start to end of s, replace spaces
    return s[:length].replace(' ', '%20')

def palindromePermutation(s: str) -> bool:
    ch_count = {}
    for ch in s:
        if ch not in ch_count:
            ch_count[ch] = 1
        else:
            ch_count[ch] += 1
    for _ch, count in ch_count.items():
        if count % 2 != 0:
            return False
    return True

def oneAway(s1: str, s2: str) -> bool:
    longer, shorter = (s1, s2) if len(s1) > len(s2) else (s2, s1)   
    len_delta = len(longer) - len(shorter)
    if len_delta > 1:
        # more than one edit away, invalid
        return False
    if len_delta == 0:
        # check for single replacement
        found_difference = False
        for i in range(len(longer)):
            if longer[i] != shorter[i]:
                if found_difference:
                    return False
                found_difference = True
        return True
    else:
        # check for single insertion/deletion
        longer_index = 0
        shorter_index = 0
        found_difference = False
        while longer_index < len(longer) and shorter_index < len(shorter):
            if longer[longer_index] != shorter[shorter_index]:
                if found_difference:
                    return False
                found_difference = True
                longer_index += 1
            else:
                longer_index += 1
                shorter_index += 1
        return True

    
def stringCompression(s: str) -> str:
    c = ''
    count = 0
    compressed = []
    for ch in s:
        if ch != c:
            compressed.append(c)
            if count > 0:
                compressed.append(str(count))
            c = ch
            count = 1
        else:
            count += 1
    compressed.append(c)
    if count > 0:
        compressed.append(str(count))
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

def rotateMatrix(matrix: list[list[int]]) -> list[list[int]]:

    pass

# Execution
def main():
    """Main function"""
    s = stringCompression('aaa')
    print(s)

if __name__ == "__main__":
    main()
