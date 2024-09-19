owner= {
    "name": "irfan",
    "id": 1432
    }
accounts={"user_name": "ali",
          "user_id": 15423
          }


def owner_main(owner):
    print("....owner athentication....")
    owner_name=input("enter your name")
    owner_id  =int(input("enter your id"))
    if owner_name == owner["name"] and owner_id == owner["id"]:
        print(f"welcome {owner_name} sir")
        return True
    else:
        print("please check your details carefully")
        
# owner_main(owner)


def create_account(accounts):
    print("for owner authentication purpose")
    if owner_main(owner)==True:
        print("create accounts for user: ")
        user_name=input("enter user name")
        user_id= int(input("enter user id"))
        company_name=input("enter company name")
        accounts["user_name"]=user_name
        accounts["user_id"]=user_id
        accounts["company_name"]=company_name
        file=open("database.txt","+a")
        file.write(str(accounts))
    else:
        print("only owner create more account")
    print(accounts)



def income_manage():
    balance=[100]
    if owner_main(owner)==True:
        run=True
        while run==True:
            print("1: add balance \n2: See balance \n3: withdrow")
            u_choice=int(input("enter your choice"))
            if u_choice==1:
                money=int(input("enter money"))
                balanc=balance[0]+money
                balance[0]=balanc
            elif u_choice==2:
                print(f"your balance is {balance}")
            elif u_choice==3:
                w=int(input("enter money you want to withdrow"))
                if w<balance[0]:
                    balance[0]=balance[0]-w
            else:
                print("invalid input")
                run=False
    else:
        print("athyentication denaid")


        


def manage_reports():
    # Reports only see owner
    
    if owner_main(owner)==True:
        print("....reports in time duration....\n..1: one years..\n..2: six..\n..3: one day..")
        
        choice=int(input("Enetr your choice"))
        if choice==1:
            print("data filter of 1 year")
        elif choice==2:
            print("data filter of 6 moths")
        elif choice==3:
            print("data filter of one day")
        else:
            print("data filter of defoult days")


running=True
while running==True:
    print("Account managemnet system: \n....1: owner athentication....\n....2: create accounts for user....\n....3: manage income....\n....4: manage reports....\n....0: stop operations....")
        
    choice= int(input("enter your choice"))
    
    
    if choice == 1:
        owner_main(owner)
    elif choice == 2:
        create_account(accounts)
    elif choice == 3:
        income_manage()
    elif choice == 4:
        manage_reports() 
    elif choice == 0:
        print("thanks for comming ")
        running=False
    else:
        print("invalid operation")
        running=False
        
        