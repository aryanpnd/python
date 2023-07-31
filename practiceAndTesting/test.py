
# def solve(date):
#     a = (int(date[5:7])-1)*30
#     b = (int(date[8:10]))+1
#     c = (a+b)*10
#     return c

# print(solve("2019-09-10"))

# --------------------------------------------------

# def solution(a,b):
#     sum1 = 0
#     for i in b:
#         sum1 += a[i]
#     return sum1

# --------------------------------------------------
# def solve(n):

#     a = [0] * (n+1)

#     a[1] = 1

#     for i in range(2, n+1):
#         if i % 2 == 0:
#             a[i] = a[i // 2]
#         else:
#             a[i] = a[i // 2] + a[i // 2 + 1]

#     return max(a)

# --------------------------------------------------

# def specialBinaryTree(arr):


#     count = 0
#     for i in range(3):
#         for j in range(i+1, 3):
#             if (arr[i] + arr[j]) % 2 == 0:
#                 k = (arr[i] + arr[j]) // 2
#                 if k in arr:
#                     count += 1

#     return count

# if __name__ == '__main__':
# 	arr_count = int(input().strip())

# 	arr = []

# 	for _ in range(arr_count):
# 		arr_item = int(input().strip())
# 		arr.append(arr_item)

# 	result = specialBinaryTree(arr)

# 	print(str(result))


# ---------------------------------------------------------


# def solution(num):

#     sqrt = num ** 0.5
#     if int(sqrt + 0.5) ** 2 == num:
#         return ('YES')
#     else:
#         return ('NO')

# print(solution(49))

# ---------------------------------------------------------
# def solution(k, n):

#     sum = 0
#     i = 1
#     while(i<=n):
#         if(i % k == 0):
#             sum = sum + i
#         i = i + 1

#     return ( sum)


# ------------------------------------------------------------

# def check_prefectness(string):
#     left_count = 0
#     right_count = 0

#     #Iterating through the string
#     for char in string:
#         if char == '(':
#             left_count += 1
#         elif char == ')':
#             right_count += 1
#         #If the character is the special character '?'
#         elif char == '?':
#             #Checking if the total number of left parenthesis is greater than the number of right parenthesis
#             if left_count > right_count:
#                 #Incrementing the right parenthesis count
#                 right_count += 1
#             #Otherwise
#             else:
#                 #Incrementing the left parenthesis count
#                 left_count += 1

#     #Checking if the left and right parenthesis counts are equal
#     if left_count == right_count:
#         return True
#     else:
#         return False

# ---------------------------------------------------------------

# def maximizeGCD(arr,n):

#     # Initialize result
#     res = 0

#     # Traverse array elements
#     for i in range(n):

#         # Calculate gcd of current
#         # array element
#         gcd = arr[i]
#         for j in range(i+1, n):
#             gcd = __gcd(gcd, arr[j])

#         # Update result if
#         # current gcd is greater
#         res = max(res, gcd)

#     return res

# # Driver code
# if __name__ == "__main__":

#     # input array size
#     n = int(input())

#     # input array elements
#     arr = list(map(int, input().split()))

#     print(maximizeGCD(arr, n))


# ---------------------------------------------------------------
# def findMinNumbers(arr):
#   count = 0
#   for i in range(len(arr)):
#     if arr[i] % 6 != 0:
#       count += 1
#   return count

# ---------------------------------------------------------------
# def CountWords(words):
#     n = len(words)
#     count = n
#     for i in range(n):
#         for j in range(n):
#             if (words[i] == words[j][::-1]):
#                 count -= 1
#                 words[i] = words[j] = '0'

#     return count


# ---------------------------------------------------------------

# def solve(nums):
#   A = nums
#   n = len(A)
#   maxLen = 0
#   S = set(A)
#   for i in range(0, n):
#     for j in range(i + 1, n):
#       x = A[j]
#       y = A[i] + A[j]
#       length = 2
#       while y in S:
#         z = x + y
#         x = y
#         y = z
#         length += 1
#         maxLen = max(maxLen, length)
#   if maxLen > 2:
#     return maxLen
#   else:
#     return 0

# ---------------------------------------------------------------

# def greaterString(s, k): 
     
#     # new string
#     X = ""
 
#     # Remove characters until
#     # the string is empty
#     while (len(s) > 0):
#         temp = s[0]
 
#         # Traverse to find the smallest
#         # character in the first k characters
#         i = 1
#         while(i < k and i < len(s)):
#             if (s[i] < temp):
#                 temp = s[i]
 
#             i += 1
         
#         # append the smallest character
#         X = X + temp
 
#         # removing the lexicographically
#         # smallest character from the string
#         for i in range(k):
#             if (s[i] == temp):
#                 s = s[0:i] + s[i + 1:]
#                 break
         
#     return X

# ---------------------------------------------------------------

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'greaterString' function below.
# # 
# # The function is expected to return an STRING.
# # The function accepts following parameters:
# # 1. STRING s
# # 2. CHARACTER k
# #
# def greaterString(s, k): 
     
#     # new string
#     X = ""
 
#     # Remove characters until
#     # the string is empty
#     while (len(s) > 0):
#         temp = s[0]
 
#         # Traverse to find the smallest
#         # character in the first k characters
#         i = 1
#         while(i < k and i < len(s)):
#             if (s[i] < temp):
#                 temp = s[i]
 
#             i += 1
         
#         # append the smallest character
#         X = X + temp
 
#         # removing the lexicographically
#         # smallest character from the string
#         for i in range(k):
#             if (s[i] == temp):
#                 s = s[0:i] + s[i + 1:]
#                 break
         
#     return X
	
	

# if __name__ == '__main__':
# 	s = input()

# 	k = input()[0]

# 	result = greaterString(s, k)

# 	print(result)

# -------------------------------------------------------------------------


# def max_kill_anthills(arr, t): 
#     max_ants = 0
#     for i in range(len(arr)): 
#         if(arr[i] <= t): 
#             max_ants = max(max_ants, arr[i]) 
#     return max_ants 
  
# n = int(input()) 
# arr = [] 
# for i in range(n): 
#     arr.append(int(input())) 
# t = int(input()) 

# print(max_kill_anthills(arr, t))

# ---------------------------------------------------------------------------------

# def solve(k, a):
#     newK = []
#     for i in str(k):
#         newK.append(i)
#     nosBuy = newK[0]
#     sortedA = sorted(a,reverse=True)
#     sum1 = sortedA[0:int(nosBuy)]
#     return sum(sum1)


	

# if __name__ == '__main__':
# 	k = int(input().strip())

# 	a_count = int(input().strip())

# 	a = []

# 	for _ in range(a_count):
# 		a_item = int(input().strip())
# 		a.append(a_item)

# 	result = solve(k, a)

# 	print(str(result))

# ------------------------------------------------------------------------------------
# def neoTriSeries(n):
#   if n == 0:
#     return 0
#   elif n == 1 or n == 2:
#     return 1
#   else:
#     return neoTriSeries(n-3) + neoTriSeries(n-2) + neoTriSeries(n-1)

# n = int(input("Enter the nth number of the series: "))
# print("The nth number of the series is:", neoTriSeries(n))

# ------------------------------------------------------------------------------------

# def solve(friends, a): 
#     # Initialize the variables 
#     total_candies = 0
#     flag = True
#     middle_index=len(a)//2
#     candies_required = a[middle_index:]
#     candies_available = a[:middle_index]
#     # Calculate the total number of candies 
#     for i in range(0, len(candies_available)): 
#         total_candies += candies_available[i] 
  
#     # Check if the total number of candies is 
#     # greater than the required number of candies 
#     if total_candies >= sum(candies_required): 
#         # Check if each friend can get the 
#         # required number of candies 
#         for i in range(0, len(str(friends))): 
#             # Calculate the remaining candies 
#             remaining = total_candies - candies_required[i] 
  
#             # Check if the remaining number of 
#             # candies is greater than or equal to 0 
#             if remaining >= 0: 
#                 total_candies = remaining 
#             else: 
#                 # Set flag to False 
#                 flag = False
#                 break
#     else: 
#         flag = False
  
#     # Check if the flag is True or False 
#     if flag: 
#         return "Yes"
#     else: 
#         return "No"
  
# # Driver code 
# if __name__ == '__main__':
# 	a_count = int(input().strip())

# 	a = []

# 	for _ in range(a_count):
# 		a_item = int(input().strip())
# 		a.append(a_item)

# 	b_count = int(input().strip())

# 	b = []

# 	for _ in range(b_count):
# 		b_item = int(input().strip())
# 		b.append(b_item)

# 	result = solve(a, b)

# 	print(result)

# -------------------------------------------------------------------------------

# def solve(s, k): 
#     for i in range(k):
#         for j in range(len(s)):
#             if s[j] != s[len(s)-1-j]:
#                 s = s[:j] + s[j+1:]
#     for i in range(len(s)):
#         if s[i] != s[len(s)-1-i]:
#             return "No"
#     return "Yes"
	

# if __name__ == '__main__':
# 	s = input()

# 	k = int(input().strip())

# 	result = solve(s, k)

# 	print(result)

# ----------------------------------------------------------------------------
# def palindrome_check(s, k): 
#   for _ in range(k): 
#     for i in range(len(s)): 
#       if s[i] != s[-i-1]: 
#         s = s[:i] + s[i+1:] 
#         break 
#   for i in s: 
#     if i != i[::-1]: 
#       return "No"
#   return "Yes"
  
# if __name__ == '__main__':
# 	s = input()

# 	k = int(input().strip())

# 	result = palindrome_check(s, k)

# 	print(result)

# ---------------------------------------------------------------------------
# def diff_chars(s,t): 
#   count = 0
#   for i in range(len(s)):
#     if s[i] != t[i]:
#       count += 1
#   return count

# s = input("Enter string S: ")
# t = input("Enter string T: ")

# print("Total number of positions where both the strings differ in character:",diff_chars(s,t))

# -------------------------------------------------------------------------------------
# def solution(s,t): 
#   count = 0
#   for i in range(len(s)):
#     if s[i] != t[i]:
#       count += 1
#   return count
	
	

# if __name__ == '__main__':
# 	S = input()

# 	T = input()

# 	result = solution(S, T)

# 	print(str(result))

# --------------------------------------------------------------------------------------

# def findSumOfMultiplesOfFive(array): 
#   result = [] 
  
#   # Iterate through the array 
#   for i in range(len(array)): 
  
#     # Sum of multiples of 5 
#     # before the current element 
#     sum = 0
  
#     # Iterate through all numbers 
#     # less than equal to the current element 
#     for j in range(i+1): 
  
#       # If the number is divisible by 5 
#       if array[j] % 5 == 0: 
  
#         # Add it to the sum 
#         sum += array[j] 
  
#     # Append the sum to the result array 
#     result.append(sum) 
  
#   # Return the result array 
#   return result 
  
# # Driver code 
# arr = [8, 5, 15, 23, 10] 
# print(findSumOfMultiplesOfFive(arr))

# -----------------------------------------------------------------------------------
# def find_best_pair(arr):
#   max1 = 0
#   max2 = 0
#   id1 = 0
#   id2 = 0
#   for i in range(len(arr)):
#     if arr[i] > max1:
#       max2 = max1
#       max1 = arr[i]
#       id2 = id1
#       id1 = i
#     elif arr[i] > max2:
#       max2 = arr[i]
#       id2 = i
  
#   print("The best pair of students for the coding competition are:", id1, "and", id2)

# arr = [int(i) for i in input("Enter the coding skills of the students: ").split()]
# find_best_pair(arr)

# -----------------------------------------------------------------------------------
# def solve(box): 
#     max_candies = 0
#     for i in range(0, len(box)-2, 3): 
#         curr_candies = max(box[i], box[i+1], box[i+2]) 
#         max_candies += curr_candies
#     return max_candies-1
	
	

# if __name__ == '__main__':
# 	a_count = int(input().strip())

# 	a = []

# 	for _ in range(a_count):
# 		a_item = int(input().strip())
# 		a.append(a_item)

# 	result = solve(a)

# 	print(str(result))

# ----------------------------------------------------------------------------------------
# from collections import Counter
# ph1= ["Robocalls are on the rise. Be wary of any pre-recorded messages you might receive"]
# ph2=["our access to your library account is expiring soon due to inactivity. To continue to have access to the library services account, you must reactivate your account. For this purpose, click the web address below or copy and paste it into your web browser. A successful login will activate your account and you will be redirected to your library profile"]
# ph3=["We detected unknown IP access on our date base computer system our security requires you to verify your account for secure security kindly Click Here and verify your account"]
# ph4=["Password will expire in 2 days  Click Here To Validate E-mail account"]
# ph5=["As we prepare to start the 2016 Tax filling season, we have undergone slight changes in the filling process to make filling for your refund easier and to prevent unnecessary delays."]
# ph6=["Hello, You have an important email from the Human Resources Department with regards to your December 2015 Paycheck"]
# ph7=["Your parcel (shipping document) arrived at the post office. Here is your Shipping Document/Invoice and copy of DHL receipt for your tracking which includes the bill of lading and DHL tracking number, the new Import/Export policy supplied by DHL Express. Please kindly check the attached to confirm accordingly if your address is correct, before we submit to our outlet office for dispatch to your destination"]
# ph8=["Your Itunes-ID has been disabled .You've place your account under the risk of termination by not keeping the correct informations .Please verify your account as soon as possible.Ready to check ?Click here to get back your account."]
# ph9=["Hello,  Please refer to the vital info I've shared with you using Google Drive.  Click https://www.google.com/drive/docs/file0116 and sign in to view details.."]
# ph10=["I recently read your last article and it was very useful in my field of research. I wonder, if possible, to send me these articles to use in my current research:This email is enclosed in the Marquette University secure network, hence access it below.Access the documents here <http://gabrielramon.be/<link removed>,***Ensure your login credentials are correct to avoid cancellations** Part of the changes include updating our database with your information."]
# words1=ph1[0].split()+ph2[0].split()+ph3[0].split()+ph4[0].split()+ph5[0].split()+ph6[0].split()+ph7[0].split()+ph8[0].split()+ph9[0].split()+ph10[0].split()
# stopwords=['to','the','and','or','you','your','with','have','had','has','of','in','our','is','for','it','will'] 
# words=[]
# for i in words1:
#     if i not in stopwords:
#         words.append(i)

# word_counts = Counter(words)
# top_five = word_counts.most_common(5)
# print(top_five)

# -----------------------------------------------------------------------------------------------------------------------
# a = int(input())
# c = input().split()

# list1 = []
# if "50" in c:
#     list1.append(50)
# print(len(list1))

# --------------------------------------------------------------------------------
# import ast,sys

# input_str = input()
# input_list = ast.literal_eval(input_str)

# sorting_choice = input()

# --------------------------------------------------------------------------------
# common_elements in two list
# import numpy as np

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [3, 5, 7, 9]

# common_elements = np.intersect1d(list1, list2)
# print(common_elements)

# list(set(list_1).intersection(list_2))

# --------------------------------------------------------------------------------
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
a = sorted(set(input_list))
if a==input_list:
    print("yes")
else:print("no")