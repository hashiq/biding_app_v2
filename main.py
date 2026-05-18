# game_continue = True
# bidding = {}
# while game_continue:
#     bider_name = input("Enter a bider name :")
#     bid_price = int(input("Enter a bid price :"))
#     bidding["name"]=bider_name
#     bidding["price"] = bid_price
#     bid_stop =input("Do you want to continue the bid 'yes' or 'no'").lower()
#     if bid_stop == 'yes':
#         pass
#     elif bid_stop == 'no':
#         game_continue =False
#     else:
#         game_continue=False
#         print("#404 error ")
#
# print(bidding)

age = []

student = [
    { "name": "vesttapen", "age":30},
    { "name": "Lewis", "age":36},
    { "name": "ronaldo", "age":42},
]
# for key in student:
#     print(student["age"])

for i in range(len(student)):
    age.append(student[i]["age"])


