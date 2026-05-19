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
people = [
    {"name": "Albert Einstein", "age": 147},
    {"name": "Isaac Newton", "age": 383},
    {"name": "Nikola Tesla", "age": 170},
    {"name": "Leonardo da Vinci", "age": 574},
    {"name": "Mahatma Gandhi", "age": 157},
    {"name": "Nelson Mandela", "age": 108},
    {"name": "Martin Luther King Jr.", "age": 97},
    {"name": "Abraham Lincoln", "age": 217},
    {"name": "Julius Caesar", "age": 2126},
    {"name": "Alexander the Great", "age": 2382},
    {"name": "Galileo Galilei", "age": 462},
    {"name": "Charles Darwin", "age": 217},
    {"name": "Thomas Edison", "age": 179},
    {"name": "Stephen Hawking", "age": 84},
    {"name": "Marie Curie", "age": 159},
    {"name": "William Shakespeare", "age": 462},
    {"name": "Napoleon Bonaparte", "age": 257},
    {"name": "George Washington", "age": 294},
    {"name": "Muhammad Ali", "age": 84},
    {"name": "Pelé", "age": 86},
    {"name": "Diego Maradona", "age": 66},
    {"name": "Johan Cruyff", "age": 79},
    {"name": "Franz Beckenbauer", "age": 81},
    {"name": "Zinedine Zidane", "age": 54},
    {"name": "Ronaldinho", "age": 46},
    {"name": "Ronaldo Nazario", "age": 50},
    {"name": "David Beckham", "age": 51},
    {"name": "Cristiano Ronaldo", "age": 41},
    {"name": "Lionel Messi", "age": 39},
    {"name": "Neymar Jr", "age": 34},
    {"name": "Kylian Mbappe", "age": 27},
    {"name": "Erling Haaland", "age": 26},
    {"name": "Kevin De Bruyne", "age": 35},
    {"name": "Luka Modric", "age": 41},
    {"name": "Mohamed Salah", "age": 34},
    {"name": "Robert Lewandowski", "age": 38},
    {"name": "Vinicius Junior", "age": 26},
    {"name": "Jude Bellingham", "age": 23},
    {"name": "Harry Kane", "age": 33},
    {"name": "Sergio Ramos", "age": 40},
    {"name": "Karim Benzema", "age": 39},
    {"name": "Son Heung-min", "age": 34},
    {"name": "Pedri", "age": 24},
    {"name": "Bruno Fernandes", "age": 32},
    {"name": "Antoine Griezmann", "age": 35},
    {"name": "Bukayo Saka", "age": 25},
    {"name": "Jamal Musiala", "age": 18},
    {"name": "Elon Musk", "age": 55},
    {"name": "Bill Gates", "age": 71},
    {"name": "Steve Jobs", "age": 71},
    {"name": "Mark Zuckerberg", "age": 42},
    {"name": "Jeff Bezos", "age": 62},
    {"name": "Warren Buffett", "age": 96},
    {"name": "Oprah Winfrey", "age": 72},
    {"name": "Michael Jackson", "age": 68},
    {"name": "Freddie Mercury", "age": 80},
    {"name": "Elvis Presley", "age": 91},
    {"name": "Bruce Lee", "age": 86},
    {"name": "Jackie Chan", "age": 72},
    {"name": "Arnold Schwarzenegger", "age": 79},
    {"name": "Sylvester Stallone", "age": 80},
    {"name": "Tom Cruise", "age": 64},
    {"name": "Leonardo DiCaprio", "age": 52},
    {"name": "Brad Pitt", "age": 63},
    {"name": "Johnny Depp", "age": 63},
    {"name": "Keanu Reeves", "age": 62},
    {"name": "Robert Downey Jr.", "age": 61},
    {"name": "Chris Evans", "age": 45},
    {"name": "Scarlett Johansson", "age": 42},
    {"name": "Emma Watson", "age": 36},
    {"name": "Taylor Swift", "age": 37},
    {"name": "Adele", "age": 38},
    {"name": "Beyoncé", "age": 45},
    {"name": "Rihanna", "age": 38},
    {"name": "Drake", "age": 40},
    {"name": "Eminem", "age": 54},
    {"name": "Snoop Dogg", "age": 55},
    {"name": "Tupac Shakur", "age": 55},
    {"name": "The Notorious B.I.G.", "age": 54},
    {"name": "Virat Kohli", "age": 38},
    {"name": "MS Dhoni", "age": 45},
    {"name": "Sachin Tendulkar", "age": 53},
    {"name": "Usain Bolt", "age": 40},
    {"name": "Michael Jordan", "age": 63},
    {"name": "Kobe Bryant", "age": 48},
    {"name": "LeBron James", "age": 42},
    {"name": "Roger Federer", "age": 45},
    {"name": "Rafael Nadal", "age": 40},
    {"name": "Novak Djokovic", "age": 39},
    {"name": "Serena Williams", "age": 45},
    {"name": "Muhammad ibn Musa al-Khwarizmi", "age": 1246},
    {"name": "Confucius", "age": 2575},
    {"name": "Socrates", "age": 2497},
    {"name": "Plato", "age": 2454},
    {"name": "Aristotle", "age": 2410},
    {"name": "Genghis Khan", "age": 864},
    {"name": "Joan of Arc", "age": 614},
    {"name": "Wolfgang Amadeus Mozart", "age": 270},
    {"name": "Ludwig van Beethoven", "age": 256},
    {"name": "Vincent van Gogh", "age": 173},
    {"name": "Pablo Picasso", "age": 145},
    {"name": "Salvador Dalí", "age": 122},
    {"name": "Alan Turing", "age": 114},
    {"name": "Tim Berners-Lee", "age": 71},
    {"name": "Barack Obama", "age": 65}]

for i in range(len(people)):
    age.append(people[i]["age"])

max_age = max(age)
min_age = min(age)
for i in range(len(people)):

    user_founded = people[i]
    if max_age == people[i]["age"]:
        print(f"aged person is {user_founded['name']} with age of {user_founded['age']}")
    elif min_age == people[i]["age"]:
        print(f"lowest aged person is {user_founded['name']} with age of {user_founded['age']}")





