# Sets Practice
# Description
# Let’s say you have two lists, A and B. Identify the elements which are common in the two lists, A and B and return them in a sorted manner. For example 



# Sample Input :

# A = [5,1,3,4,4,5,6,7]

# B = [3,3,5,5, 1 ,7 ,2]



# Sample Output:

# [1,3,5,7]



# If you observe the sample output here, you can see that:

# Though value 5 is repeated twice in both lists, in the final output, it is present only once.
# The values are returned in a sorted manner with values increasing.

# ------------------------------------------------------------------------------------------------------

import ast,sys

from cv2 import sort

list_1 = [5, 5, 5, 5, 5, 5, 5, 3]
list_2 = [3, 3, 5, 5, 1, 7, 2]


A = set(list_1)
B = set(list_2)
C =A.intersection(list_2)
answer = list(C)
answer.sort()

print(answer)