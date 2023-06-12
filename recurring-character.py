"""
First Recurring character

Given a string, return the first recurring character that appears. If there are no recurring characters, return none

Example:
Input: Qwertty
Output: t

Input: Qwerty
Output: None
"""

def first_reccuring_char(string):
    seen_so_far = set()

    for c in string:
        if c in seen_so_far:
            return c
        seen_so_far.add(c)

    return None


print(first_reccuring_char("Qwerty"))
print(first_reccuring_char("Qwertty"))