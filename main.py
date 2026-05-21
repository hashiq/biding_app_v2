loop_run = True
bid = {}

def highest_bider(bid):
    max_bid = 0
    for i in bid:
       if max_bid < bid[i]:
           max_bid=bid[i]
    return max_bid


while loop_run:
    bider = input("enter your name :")
    price = int(input("enter bid price :"))
    bid[bider]=price
    stop_bid = input("does any other bider need to join :")
    if stop_bid== "yes":
        pass
    elif stop_bid =="no":
        print(highest_bider(bid))
        loop_run=False
    else:print("Wrong input")
