import sys
from menu_view import menuView
from menu1_view import menuView_1
from menu2_view import menuView_2
from book_transactions import bookList,addBook,removeBook,searchBook
from member_transactions import memberList, addMember,searchMember,deleteMember,bookRental,returnBook,bookTracking

def menu():
    while True:
        try:
            decision = int(input("\n<- back to menu     =>1 \nX Exit              =>0\n(1/0): "))
            if decision in (0,1):
                break
            else:
                print("please enter a valid number!")
        except ValueError:
            print("please enter a number!")
    if decision == 1:
        mainMenu()
    elif decision == 0:
        print('exiting the program...')
        sys.exit()
        

def mainMenu():
    while True:
        menuView()
        while True:
            try:
                choice = int(input("please make a choice: "))
                if 0 <= choice <3:
                    break
                else:
                    print("please enter a valid number!")
            except ValueError:
                print("please enter a number!")
        if choice == 0:
            print("exiting the program...")
            sys.exit()

#------------1-) Membership operations --------------- 
    #            
        if choice == 1: # => membership operations (function start here!)
            menuView_1()
            while True:
                try:
                    choice1 = int(input("please make a choice: "))
                    if 0 <= choice1 <8:
                        break
                    else:
                        print("please enter a valid number!")
                except ValueError:
                    print("please enter a number !")
            if choice1 == 0:
                print("exiting the program...")
                sys.exit()
            elif choice1 == 1:
                memberList()
                menu()
            elif choice1 == 2:
                addMember()
                menu()
            elif choice1 == 3:
                searchMember()
                menu()
            elif choice1 ==4:
                deleteMember()
                menu()
            elif choice1 == 5:
                bookRental()
                menu()
            elif choice1 == 6:
                returnBook()
                menu()
            elif choice1 == 7:
                bookTracking()
                menu()

#------------2-) Book operations ---------------
        if choice == 2:
            menuView_2()
            while True:
                try:
                    choice2 = int(input("please make a choice: "))
                    if 0 <= choice2 <5:
                        break
                    else:
                        print("please enter a valid number!")
                except ValueError:
                    print("please enter a number !")
            if choice2 == 0:
                print("exiting the program...")
                sys.exit()
            elif choice2 == 1: # 1. choice
                bookList()
                menu()
            elif choice2 == 2:
                addBook()
                menu()
            elif choice2 == 3:
                searchBook()
                menu()
            elif choice2 == 4:
                removeBook()
                menu()
        break


mainMenu()
        
        
        

        


