string1 = input("enter the string 1: ")
str_len = len(string1)
reversed = string1[::-1]
if reversed == string1:
    palindrome = " is  palindrome"
else:
    palindrome ="string is not palindrome"

string2 = input("enter the string2: ")

if string1 == string2:
    equality = "is palindrome"
else:
    equality = "is not palindrome"
sub_str = input("enter the sub string: ")

if sub_str in string1:
    sub_str_result = "substring found in the original string1"
else:
    sub_str_result = "substring is not found in the original string1"

print("length of string1: ",str_len)
print("reversed of string1 is: ",reversed)
print("string:",palindrome)
print("equality check of str 1 and 2: ",equality)
print("sub string check in string 1: ",sub_str_result)