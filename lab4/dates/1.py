# Python Dates

import datetime

x = datetime.datetime.now()
print(x)

# Date Output

print(x.year)
print(x.strftime("%A"))


# Creating Date Objects

x = datetime.datetime(2018, 1, 21)
print(x)

# The strftime() Method

print(x.strftime("%B"))