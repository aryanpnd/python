# Rename Columns
# You have been given a dataset called 'heart'. Here are its first few rows:﻿

# image.png 12.76 KB
# ﻿
# As you can see, the column names are all lowercase. Your task is to capitalize the first character of every column present in it such that your dataframe looks like the following:﻿

# image.png 13.78 KB
# ﻿
# You just need to write the code for capitalizing; you need not print anything as the print statement has already been provided in the stub.

# Importing the pandas package
import pandas as pd

# Reading the dataframe
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/XWvQjYY4LZWdxLvPWOj2pPwn/heart.csv')

# Access the columns of the dataframe using df.columns and apply the following
# function which uses the ASCII values of the first character to capitalise the 
# first character of each word. As you know, the ASCII value of the lower cased 
# letters start with 97 (for 'a') and for upper case letters, it starts with 65
# (for 'A'). So you just need to subtract 32.
df.columns = df.columns.map(lambda x: x.replace(x[0], chr(ord(x[0]) - 32), 1))

# Printing the final columns. Do not edit this part.
print(df.columns)