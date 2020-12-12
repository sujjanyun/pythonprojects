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

check = input("Hello. Are you checking in or checking out with us today? ")

if check == ("checking in"):
    floor = input("Which floor are you on? ")
    room = input("What room number? ")
    number = input("Welcome to Hotel Del Luna. How many are checking in today? ")
    name = input("What is(are) your name(s)? ")

STOP = 50
occupants = 0

while occupants > 0:
    if (occupants) <= 50:
        print(occupants)
    occupants += 1

hotel[name][]


else:
    print("bloop")