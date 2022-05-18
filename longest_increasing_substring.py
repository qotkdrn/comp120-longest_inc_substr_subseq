"""
File: longest_increasing_substring.py 
Author: COMP 120 class
Date: March 23, 2021
Description: Has function for longest_increasing_substring.
"""
def longest_increasing_substring(s):
    """
    Returns the longest substring in s.  In case of
    ties, returns the first longest substring.
    """
    #Want to return input str as is when empty or has length of 1
    if len(s) == 0 or len(s) == 1:
        return s     
    #Empty to store all substrings
    #keys are the lengths of the substrings
    #values are the substrings
    s_dict = {} 
    sub_s = "" #empty string to temporarily hold each substring
    for i in range(len(s)):
        if i == 0:
            sub_s += s[i]
        elif s[i] > s[i-1]:
            sub_s += s[i]
        else:
            s_dict[len(sub_s)] = sub_s
            sub_s = s[i]
    s_dict[len(sub_s)] = sub_s
    return s_dict.get(max(s_dict))

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Maximum consecutive increasingly ordered substring is: {longest_increasing_substring(s)}")


