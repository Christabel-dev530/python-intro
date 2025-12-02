#A man had 500k in his account and he spent 250k to buy properties 
#out of it.how much will remain.
def property():
    amount_gotten=500000
    amount_spent=250000
    amount_remaining=amount_gotten-amount_spent
    return amount_remaining
    
def soldproperties():
    amount_received=3*100000
    amount_spent=50000
    amount_kept=amount_received-amount_spent
    return amount_kept
        










## a woman bought 3 tubers of yam at 1000 each. she later bought 6 onions
# at 100 each. finally, she bought 1 dozen of egg at 200 each per one. 
# if the woman had 20,000 with her. how much will she have left.
def woman():
    y=3*1000
    o=6*100
    e=12*200
    initial_amount=20000
    d=y+0+e
    amount_left=initial_amount-d
    print("the amount left is" ,amount_left)
    return amount_left
    
   # a man went to the market and bought 13 dozens of egg at 200 each.
# he sold all the egg at 250 per one. using python function, calculate
# his profile and percentage profile.
def market():
    cp=156*200
    sp=36*250
    profit=sp-cp
    perprofit=profit/cp*100
    return profit

def calculateloan(profit,amount_left,amount_remaining,amount_kept):
    principal=profit +amount_left+amount_remaining+amount_kept
    print(principal)
    rate=5
    time=2
    SI=float(principal*rate*time/100)
    print("the simple interest is" ,SI)
calculateloan(market(),woman(),property(),soldproperties())    
    
    
    
    
