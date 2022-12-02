def getdate():
    import datetime
    return datetime.datetime.now()


def health_management():
    print("hello!!,welcome to the health management system :)")
    a = int(input("lock(1) or retrive(0)::"))
    
    if a==1:
        name = input("Enter : archi,rohan,hammad:")
        choose = int(input("food(1) or exercise(2):"))

        if name.lower() == "archi":
            if choose==1:
                food = input("Enter food::")
                with open("archi_food.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open("archi_food.txt","r") as f:
                    x = f.readline()
                    print(x)
            elif choose==2:
                food = input("Enter exercise::")
                with open("archi_exercise.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open("archi_exercise.txt","r") as f:
                    x = f.readline()
                    print(x)
            else:
                return "kindly Enter 1 or 2"
        elif name.lower() == "rohan":
            if choose==1:
                food = input("Enter food::")
                with open("rohan_food.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open("rohan_food.txt","r") as f:
                    x = f.readline()
                    print(x)
            elif choose==2:
                food = input("Enter exercise::")
                with open("rohan_exercise.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open("rohan_exercise.txt","r") as f:
                    x = f.readline()
                    print(x)
            else:
                return "kindly Enter 1 or 2"

        elif name.lower() == "hammad":
            if choose==1:
                food = input("Enter food::")
                with open("hammad_food.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open("hammad_food.txt","r") as f:
                    x = f.readline()
                    print(x)
            elif choose==2:
                food = input("Enter exercise::")
                with open("hammad_exercise.txt","w") as f:
                    f.write(f"{getdate()}+ :: {food}")
                with open(f"hammad_exercise.txt","r") as f:
                    x = f.readline()
                    print(x)
            else:
                return "kindly Enter 1 or 2"
        else:
            return"Enter valid name"
    elif a==0:
        retive_data = input("retrive data of archi,rohan or hammad???::")

        if retive_data=="archi":
            with open("archi_food.txt","r") as f:
                x = f.readline()
                print("food-->",x)            
            with open("archi_exercise.txt","r") as f:
                x = f.readline()
                print("exercise-->",x)
        elif retive_data=="rohan":
            with open("rohan_food.txt","r") as f:
                x = f.readline()
                print("food-->",x)            
            with open("rohan_exercise.txt","r") as f:
                x = f.readline()
                print("exercise-->",x)
        elif retive_data=="hammad":
            with open("hammad_food.txt","r") as f:
                x = f.readline()
                print("food-->",x)            
            with open("hammad_exercise.txt","r") as f:
                x = f.readline()
                print("exercise-->",x)
        else:
            return"Enter valid name"        
    else:
        return "please Enter 1 or 0 !!"

print(health_management())
