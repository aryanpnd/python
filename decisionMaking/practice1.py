# If-Else
# Description
# Write a code to check if the string in a starts with a vowel or not. Print capital YES or NO.



# For example, if a = 'analytics' then, your output should print 'YES'.



# Sample Input:

# alpha



# Sample Output:

# YES

# ----------------------------------------------------------------------------------------------

input_str = "Alpha"
a = input_str.lower()
if a.startswith("a") or a.startswith("e") or a.startswith("i") or a.startswith("o") or a.startswith("u") == True:
    print("YES")
else: print("NO")
