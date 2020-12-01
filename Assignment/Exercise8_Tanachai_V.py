Username = input("Username is :")
Password = input("Password is :")
if Username == "admin" and Password == "333":
    print("****Welcome****")
    print("---J-Shop---")
    print("1.Pencil 20THB")
    print("2.Eraser 10THB")
    UserChoose = int(input("Item="))
    if  UserChoose == 1 :
        M = int(input("How many = "))
        price = M * 20
        print("---Total(THB)---")
        print(price)
    elif  UserChoose == 2 :
            M = int(input("How many = "))
            price = M * 10
            print("---Total(THB)---")
            print(price)
