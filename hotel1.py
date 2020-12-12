hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

check = input("Welcome to Hotel Del Luna. Are you checking in or checking out with us today? ")

if check == ("checking in"):
    print(" ")
    checking_in()

elif check == ("checking out"):
    print(" ")
    checking_out()

else:
    exit()

def checking_in(dictionary):
    while True:
        occupants = int(input("How many are checking in today? "))
        if 0 < occupants <= 6:
            print("Wonderful!")
            floor = random.randrange(1, 10)
            room = random.randrange(00, 50)
            room = str(floor) + str(room)
            print(room)
            while True:
                for floor in dictionary:
                    if floor == floor and 
    while floor in or room in :
        floor = random.randrange(
        room = 

rc.append()
p.append()


def checking_out:







if check == ("checking in"):
    floor = input("Which floor are you on? ")
    room = input("What room number? ")
    number = input("Welcome to Hotel Del Luna. How many are checking in today? ")
    name = input("What is(are) your name(s)? ")
