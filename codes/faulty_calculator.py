# faulty calculator

num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))

operand = input("Addition(+), multiply(*) , subtract(-) ,divide(/):::")

# def calculator(num1,num2):
if operand=="+" and num1==56 and num2==9:
        print("77 -->your calculator is faulty")
elif operand=="*" and num1==45 and num2==3:
        print("555 -->your calculator is faulty")
elif operand=="/" and num1==56 and num2==4:
    print("4 -->your calculator is faulty")
elif operand=="+":
    print(num1+num2)
elif operand=="/":
    print(num1/num2)  
elif operand=="*":
    print(num1*num2)
else:
    print("enter valid operand!!")
    
