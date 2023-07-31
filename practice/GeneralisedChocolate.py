# Generalised Chocolate
# Description
# Earlier, you solved the chocolate problem where Sanjay had m rupees, and the cost of each chocolate was c rupees. The shopkeeper gave away one chocolate for three wrappers. In this problem, let's generalise the question by saying, Sanjay has m rupees, each chocolate costs c rupees, the shopkeeper will give away k chocolates for w wrappers. Can you find now how many chocolates Sanjay will be able to eat?



# Input: 4 integers separated by space in order m c w k

# integers c and w will be >0

# integers m and k will be >=0

# integer k will be <w



# Output: An integer denoting the number of chocolates Sanjay will be able to get.





# Sample input:

# 15, 2, 3, 1



# Sample output:

# 10



# Explanation:

# Sanjay has 15 ₹, buys 7 chocolates for ₹ 2 each.

# Sanjay now has 7 wrappers, exchanges 6 of them for 2 more chocolates.

# Sanjay now has 3 wrappers and exchanges them for 1 more chocolate making a total of 10 chocolates.



# Sample input:

# 15, 2, 3, 2



# Sample output:

# 17



# Explanation:

# Sanjay has 15 ₹, buys 7 chocolates for ₹ 2 each.

# Sanjay now has 7 wrappers, exchanges 6 of them for 4 more chocolates.

# Sanjay now has 5 wrappers and exchanges 3 of them for 2 more chocolates.

# Sanjay now has 4 wrappers and exchanges 3 of them for 2 more chocolates.

# Sanjay now has 3 wrappers and exchanges them for 2 chocolates making a total of 17 chocolates.

# Execution Time Limit
# 10 seconds

#take input here
inp = input()
l =inp.split(',')
money = int(l[0])
cost = int(l[1])
wapper_for_exchange = int(l[2])
give_away_choc = int(l[3])


#start writing your code here
chocolates = money//cost
wrappers = money//cost
while (wrappers//wapper_for_exchange)*give_away_choc > 0:
    chocolates = chocolates + (wrappers//wapper_for_exchange)*give_away_choc
    wrappers = (wrappers//wapper_for_exchange)*give_away_choc + wrappers%wapper_for_exchange
print(chocolates)