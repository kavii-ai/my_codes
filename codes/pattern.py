
n = int(input("Enter the number:"))
boolean = input("true or false :").capitalize()

for i in range(n):
    if boolean== "True":
        print("*" * (i))
    else:
        print("*" * (n-i-1))

# true       

# *
# **
# ***
# ****

# false

# ****
# ***
# **
# *
