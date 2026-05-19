game_continue = True
value_star =0
age = []
bidders_list = []
print("Welcom to the grand bid")
while game_continue:
    bider_name = input("Enter a bider name :")
    bid_price = int(input("Enter a bid price :$"))
    bidders_list.append({ "name" : bider_name, "age":bid_price})
    bid_stop = input("Do you want to continue the bid 'yes' or 'no'").lower()
    if bid_stop == 'yes':
        pass
    elif bid_stop == 'no':
        game_continue = False
        for i in range(len(bidders_list)):
            age.append(bidders_list[i]["age"])
        max_age = max(age)
        min_age = min(age)
        for i in range(len(bidders_list)):
            user_founded = bidders_list[i]
            if max_age == bidders_list[i]["age"]:
                print(f"'{user_founded['name']}'age'{user_founded['age']}'")

            elif min_age == bidders_list[i]["age"]:
                print(f" Lowest bider :{user_founded['name']} -'{user_founded['age']}")
    else:
        game_continue = False
        print("#404 error ")



