game_continue = True
all_bid = []
while game_continue:
    bider_name = input("Enter a bider name :")
    bid_price = int(input("Enter a bid price :"))

    bid_history = {

    "name" : bider_name,
    "price" : bid_price}
    all_bid.append(bid_history)

    bid_stop =input("Do you want to continue the bid 'yes' or 'no'").lower()
    if bid_stop == 'yes':
        pass
    elif bid_stop == 'no':
        game_continue =False
        for i in all_bid["price"]:
            print(i)


        print("Bid ended")
    else:
        game_continue=False
        print("#404 error ")


print(all_bid)