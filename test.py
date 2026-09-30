from transaction import add_money
from transaction import  add_expense
from transaction import show_balance
print("-------TESTING MONEY TRACKER -----")
add_money("september",5000)
add_expense("september",700,"food")
add_expense("september",500,"travel")

print("testing completed!")