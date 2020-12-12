# hotel dictionary
dictionary = {
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

# my functions
def checking_in(dictionary):

  if check == ("checking in") or ("1"):
    x = input("Yay! And how many will be checking in today? ")
    if int(x) <= 6:
      print("Perfect. We can accommodate that.")
      y = input("Alright. And what is(are) your name(s)? ")

      print(f"Hello {y}, party of {x}. Give us one moment to assign you a room.")

    else:
      print("I'm sorry. We can only accommodate parties of less than 6!")

  room_assignment(dictionary)

def room_assignment(dictionary):
  for floor, room in dictionary.items():
    print(floor, room)
  from random import randrange
  dict.items()

int(floor) = random.randint(1,10)
int(room) = random.randint(1,50)

assignment = (floor + room)

def checking_out(dictionary):
    if check == ("checking out") or ("2"):
        print(" ")


check = input("Hello! Welcome to Hotel del Luna. Will you be checking in (1) or checking out (2) today? ")

checking_in(dictionary)

checking_out(dictionary)


