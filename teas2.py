#Mr Philip,MrJide,and Mrs Bankole
#Mr Philip has 500k in his account.he bought 3 tv set
#at 50000 each and he gave his wife 30000. using python
# #function calculate the balance in his account

#mr Jide bought 4 houses at 250k each and he was able
#to sell them for 450k each. using python function. 
#calculate the percentage profit and actual profit.

#add together the profit of Mr jide and the balance of
#Mr Philip. the total will serve as the principal 
#for Mrs Bankole for loan.
#time is 2yrs, rate at 5%. Calculate the simple interest.

def philip():
    account=500000
    tv=3*50000
    wife=30000
    amount_spent=tv+wife
    amount_remaining=account-amount_spent
    print(amount_remaining)
    return amount_remaining


def jide():
    items_bought=4*250000 
    items_sold=4*450000
    profit=items_sold-items_bought
    percentage_profit=profit/items_bought*100
    print(profit)
    return profit


def loan(amount_remaining,profit):
    principal=float(amount_remaining+profit)
    rate=2
    time=5
    SI=principal*rate*time/100
    print("The simple interest is", SI)
loan(philip(),jide())    
    

