#To reverse string or array
# by using sclicing

def reverselist(A):
    print("The reverse list is",A[::-1])
    A=[]
    n=int(input("enter the size of list:"))
    for i in range(0,n):
        element=int(input())
        A.append(element)
print(A)
reverselist(A)
