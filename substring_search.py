"""
File: substring_search.py 
Author: COMP 120 class
Date: March 18, 2021
Description: Has function for substring_search.
"""
def substring_search(s1, s2):
    """
    Returns the index in s1 of s2, or
    None if s2 is not a substring of s1.
    """
    # Check if even possible.
    if len(s2) > len(s1):
        return None

    # Look for s2 in s1.
    current_start = 0 # The current starting point of s2 in s1 being tested.
    found = False  # Will change to True if s2 and found in s1
    while not found and current_start <= len(s1) - len(s2):
        # Try starting at current_start
        s1_index = current_start
        s2_index = 0
        match_so_far = True  # Will change to False if characters don't match
        while match_so_far and s2_index < len(s2):
            if s1[s1_index] == s2[s2_index]:
                s1_index += 1
                s2_index += 1
            else:
                match_so_far = False

        # Did we find a match.
        if match_so_far:
            # Yes, get out of outer loop
            found = True
        else:
            # No, try the next starting point
            current_start += 1

    # Return the answer
    if found:
        return current_start
    else:
        return False

print(substring_search("abcdefg", "cde"))
print(substring_search("abcdefg", "defg"))
print(substring_search("abcdefg", "defgh"))