import re
def is_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]
print(is_palindrome("Madam"))           
print(is_palindrome("Hello"))            
print(is_palindrome("A man a plan a canal Panama"))  
