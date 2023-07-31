# Rolling the dice LPU 09
# Description
# A die is rolled n times. You have to find the probability that a number i is rolled at least j times(up to four decimal places)
# The input will contain the integers n, i and j in three lines respectively. You can assume that j<n and 0<i<7.
# The output should be rounded off to four decimal places.
# Sample Input:
# 4
# 1
# 2
# Sample Output:
# 0.1319

# Execution Time Limit
# 10 seconds

import scipy.stats as ss

n=int(input())
i=int(input())
j=int(input())

dist = ss.binom(n,1/6)
print(round(1-dist.cdf(j-1),4))