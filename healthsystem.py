#Exercise 5 - my solution
print("\nHEALTH MANAGEMENT SYSTEM\n")
def gettime():
    import datetime
    return datetime.datetime.now()
def lock():
        print("Enter the name for locking data\n1:Harry\n2:Rohan\n3:Sachin\n")
        n1=int(input())
        if n1==1:
            print("1:Locking diet\n2:Locking exercise\n")
            n2=int(input())
            if n2==1:
                data=input("Type here\n")
                f = open("harrydiet.txt","a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Diet locked successfully\n")
            elif n2==2:
                data=input("Type here\n")
                f = open("harryexercise.txt", "a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Exercise locked successfully\n")
            else:
                print("invalid input\n")
        elif n1==2:
            print("1:Locking diet\n2:Locking exercise\n")
            n2 = int(input())
            if n2 == 1:
                data = input("Type here\n")
                f = open("rohandiet.txt", "a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Diet locked successfully\n")
            elif n2 == 2:
                data = input("Type here\n")
                f = open("rohanexercise.txt", "a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Exercise locked successfully\n")
            else:
                print("invalid input\n")
        elif n1==3:
            print("1:Locking diet\n2:Locking exercise\n")
            n2 = int(input())
            if n2 == 1:
                data = input("Type here\n")
                f = open("sachindiet.txt", "a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Diet locked successfully\n")
            elif n2 == 2:
                data = input("Type here\n")
                f = open("sachinexercise.txt", "a")
                f.write(str([str(gettime())]) + ":" + data + "\n")
                f.close()
                print("Exercise locked successfully\n")
            else:
                print("invalid input\n")
        else:
            print("invalid input\n")

def retreive():
        print("Enter the name for retreiving data\n1:Harry\n2:Rohan\n3:Sachin\n")
        n1 = int(input())
        if n1 == 1:
            print("1:Retreive diet info\n2:Retrieve exercise info\n")
            n2 = int(input())
            if n2 == 1:
                with open("harrydiet.txt") as f:
                    content=f.read()
                    print("This is your retreivied data")
                    print(content)
            elif n2 == 2:
                with open("harryexercise.txt") as f:
                    content = f.read()
                    print("This is your retreivied data")
                    print(content)
            else:
                print("invalid input\n")
        elif n1 == 2:
            print("1:Retreive diet info\n2:Retrieve exercise info\n")
            n2 = int(input())
            if n2 == 1:
                with open("rohandiet.txt") as f:
                    content=f.read()
                    print("This is your retreivied data")
                    print(content)
            elif n2 == 2:
                with open("rohanexercise.txt") as f:
                    content = f.read()
                    print("This is your retreivied data")
                    print(content)
            else:
                print("invalid input\n")
        elif n1 == 3:
            print("1:Retreive diet info\n2:Retrieve exercise info\n")
            n2 = int(input())
            if n2 == 1:
                with open("sachindiet.txt") as f:
                    content=f.read()
                    print("This is your retreivied data")
                    print(content)
            elif n2 == 2:
                with open("sachinexercise.txt") as f:
                    content = f.read()
                    print("This is your retreivied data")
                    print(content)
            else:
                print("invalid input\n")
        else:
            print("invalid input\n")
while True:
    print("Do you want to lock or retreive the data..?\ntype 1 for Locking\ntype 2 to retreive\n")
    x=int(input())
    if x==1:
        lock()
    elif x==2:
        retreive()
    else:
        print("invalid input\n")
    continue

