# Pattern Printing
# Description
# Given a positive integer n. Print the pattern as shown in sample outputs.

# A code has already been provided. You have to understand the logic of the code on your own and try and make changes to the code so that it gives the correct output.



# Input: A positive integer n

# 1<= n <=9



# Output: Pattern as shown in examples below





# Sample input:

# 4



# Sample output:

# 4444444

# 4333334

# 4322234

# 4321234

# 4322234

# 4333334

# 4444444



# Sample input:

# 5



# Sample output:

# 555555555

# 544444445

# 543333345

# 543222345

# 543212345

# 543222345

# 543333345

# 544444445

# 555555555



# Execution Time Limit
# 10 seconds

#input n taken here
n=int(input())

#we will make a list of lists with just [1] in it. We will run a for loop from i= 2 to n and in each iteration
#we will add [i]*(2i-3) in top of the list and and in bottom
#then add i on both sides of all sub_lists 

answer=[['1']]
for i in range(2, n+1):
    #print("i= "+str(i))
    t=[str(i)]*((2*i)-3)
    t2=[str(i)]*((2*i)-3)
    answer.insert(0, t2)
    answer.append(t)
    for a in answer:
        a.insert(0,str(i))
        a.append(str(i))

answerfinal=[]
for a in answer:
    answerfinal.append("".join(a))
for a in answerfinal:
    print(a)