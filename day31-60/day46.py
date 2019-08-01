"""
Good morning! Here's your coding 
interview problem for today.

This problem was asked by Amazon.

Given a string, find the longest 
palindromic contiguous substring. 
If there are more than one with the
 maximum length, return any one.

For example, the longest palindromic 
substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of 
"bananas" is "anana".
"""


def day46(string):
    result = []

    def substrings(string, n):
        # n = length of substring
        for _i in range(len(string) - n + 1):
            if (checkPalindrome(string[_i:_i+n])):
                result.append(string[_i:_i+n])

    def checkPalindrome(str):
        for _i in range(len(str)):
            if str[_i] != str[-(_i+1)] : return False
        return True


    for i in range(3, len(string)):
        substrings(string, i)
    
    print(result[-1])

day46('aabcdcb')