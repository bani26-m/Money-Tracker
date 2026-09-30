from transaction import add_money, add_expense, show_balance
#range 2 is for cross verification 
for i in range (2):
    print("------Money Tracker--------")
    print("1.students")
    print("2.exit")
    option = input("enter your choice: ")
#adding student tracker
    print("------STUDENT MONEY TRACKER-------")
print("1.add salary")
print("2.food_expenses")
print("3.travel_expenses")
print("4.shopping_expenses")
print("5.others")
print("6.show balance")
print("7.monthly tracking")
print("8.exit")
def student_menu():
    balance = 0 
  
if option == "1" :
    student_menu()
else :
    print("THANKING YOU FOR VISITING MONEY TRACKER")

choice = input("enter your input-")
money = int(input("enter your money:"))
food_expenses = int(input("enter food expenses: "))
travel_expenses = int (input("enter travel expenses: "))
shopping_expenses= int(input("enter shopping expenses: "))
other= int(input("enter the other expenses: "))
total_expenses = food_expenses + travel_expenses + shopping_expenses + other

    
if choice == "1":
    MONTH = input("enter the month: ")
    print("MONTH:",MONTH)
    print("MONEY: ",money)
    add_money(month, money)
elif choice == "2":
     MONTH = input("enter the month: ")
     print("MONTH:",MONTH)
     print("food_expenses",food_expenses)
     add_expense(month,food,"Food")
elif choice == "3":
    MONTH = input("enter the month: ")
    print("MONTH:",MONTH)
    print("travel_expenses: ", travel_expenses)
    add_expense(month,travel,"Travel")
elif choice == "4":
    MONTH = input("enter the month: ")
    print("MONTH:",MONTH)
    print("shopping expenses: ",shopping_expenses)
    add_expense(month, shopping, "Shopping")
elif choice == "5": 
    MONTH = input("enter the month: ")
    print("MONTH:",MONTH)
    add_expense(month, other, "other")
elif choice == "6":
    MONTH = input("enter the month: ")
    print("MONTH:",MONTH)
    print("show balance: ",money - total_expenses)
else :
    print("print invalid!")
  
